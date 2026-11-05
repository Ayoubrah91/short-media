// Usage:
//   node render.mjs videos/cv.json out.mp4 [--audio voice.mp3] [--fps 30]
//   node render.mjs videos/cv.json stills --stills 2,10,25   (PNG previews)
import { createRequire } from 'module';
import { spawn } from 'child_process';
import fs from 'fs';
import path from 'path';
import url from 'url';
const require = createRequire(import.meta.url);
const { chromium } = require('playwright');

const args = process.argv.slice(2);
const opt = (k, d) => { const i = args.indexOf(k); return i >= 0 ? args[i + 1] : d; };
const specPath = args[0], out = args[1];
const fps = +opt('--fps', 30), audio = opt('--audio'), stills = opt('--stills');
const spec = JSON.parse(fs.readFileSync(specPath, 'utf8'));
const here = path.dirname(url.fileURLToPath(import.meta.url));

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
await page.goto(url.pathToFileURL(path.join(here, spec.engine || 'engine.html')).href);
await page.evaluate(async (s) => { await document.fonts.ready; window.init(s); await document.fonts.ready; }, spec);
await page.waitForTimeout(300);

if (stills) {
  fs.mkdirSync(out, { recursive: true });
  for (const t of stills.split(',').map(Number)) {
    await page.evaluate((t) => window.seek(t), t);
    await page.screenshot({ path: path.join(out, `t${String(t).padStart(5, '0')}.png`) });
  }
  await browser.close();
  console.log('stills ->', out);
  process.exit(0);
}

fs.mkdirSync(path.dirname(path.resolve(out)), { recursive: true });
const dur = +opt('--dur', spec.duration);
const n = Math.ceil(dur * fps);
const ff = ['-y', '-f', 'image2pipe', '-framerate', String(fps), '-i', '-'];
if (audio) ff.push('-i', audio);
ff.push('-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', '-r', String(fps));
if (audio) ff.push('-af', 'apad', '-c:a', 'aac', '-b:a', '192k', '-t', String(dur));
ff.push('-movflags', '+faststart', out);
const proc = spawn('ffmpeg', ff, { stdio: ['pipe', 'ignore', 'inherit'] });
const t0 = Date.now();
for (let i = 0; i < n; i++) {
  await page.evaluate((t) => window.seek(t), i / fps);
  const buf = await page.screenshot({ type: 'jpeg', quality: 92 });
  if (proc.exitCode !== null) throw new Error('ffmpeg exited'); if (!proc.stdin.write(buf)) await new Promise((r) => proc.stdin.once('drain', r));
  if (i % 150 === 0) console.log(`frame ${i}/${n} (${((Date.now() - t0) / 1000).toFixed(0)}s)`);
}
proc.stdin.end();
await new Promise((r) => proc.on('close', r));
await browser.close();
console.log('done ->', out, ((Date.now() - t0) / 1000).toFixed(0) + 's');
