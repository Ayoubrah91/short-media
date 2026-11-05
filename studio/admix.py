"""Mix the voice with light SFX placed from the resolved spec.
Usage: python3 admix.py spec.json voice.(mp3|wav) out.wav"""
import json, sys, subprocess, wave, numpy as np
SR = 44100
rng = np.random.default_rng(7)

def env_exp(n, tau):
    t = np.arange(n) / SR
    return np.exp(-t / tau)

def click():
    n = int(0.05 * SR)
    noise = rng.standard_normal(n)
    noise = np.diff(noise, prepend=0)              # brighten
    e = env_exp(n, 0.006)
    thump = np.sin(2 * np.pi * 170 * np.arange(n) / SR) * env_exp(n, 0.02)
    return 0.55 * noise * e / 2 + 0.5 * thump

def shutter():
    a = click(); b = click() * 1.2
    out = np.zeros(int(0.16 * SR)); out[:len(a)] += a
    o = int(0.075 * SR); out[o:o + len(b)] += b[:len(out) - o]
    return out

def whoosh(d=0.42):
    n = int(d * SR)
    x = rng.standard_normal(n)
    k = 24; x = np.convolve(x, np.ones(k) / k, mode='same')   # soft lowpass
    t = np.linspace(0, 1, n)
    e = np.sin(np.pi * t) ** 2
    return 2.2 * x * e

def sparkle(scale=1.0):
    n = int(0.75 * SR)
    t = np.arange(n) / SR
    out = np.zeros(n)
    for i, f in enumerate([2093.0, 2637.0, 3136.0, 4186.0]):
        o = int(i * 0.045 * SR)
        tt = t[:n - o]
        out[o:] += np.sin(2 * np.pi * f * tt * (1 + 0.002 * np.sin(2 * np.pi * 6 * tt))) * np.exp(-tt / 0.16) * (0.9 ** i)
    return 0.32 * scale * out

def pop():
    n = int(0.13 * SR)
    t = np.arange(n) / SR
    f = 620 - 380 * (t / t[-1])
    ph = 2 * np.pi * np.cumsum(f) / SR
    return 0.6 * np.sin(ph) * env_exp(n, 0.035)

def load_voice(p):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-ac', '1', '-ar', str(SR), '-f', 's16le', '-'], capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.int16).astype(np.float64) / 32768.0

def main(spec_p, voice_p, out_p):
    spec = json.load(open(spec_p, encoding='utf-8'))
    voice = load_voice(voice_p)
    dur = max(spec['duration'], len(voice) / SR)
    fx = np.zeros(int((dur + 1) * SR))
    def put(t, s, g=1.0):
        if t is None: return
        i = int(max(0, t) * SR)
        j = min(len(fx), i + len(s))
        fx[i:j] += g * s[:j - i]
    for b in spec['beats']:
        T = b['type']
        if T == 'hero':
            put(b.get('burstAt'), pop(), 0.8); put(b.get('burstAt'), sparkle(), 0.7)
        elif T == 'ba':
            rv = b.get('revealAt', b['at'] + 0.5)
            put(rv - 0.2, whoosh(0.35), 0.5); put(rv, sparkle(), 0.8)
        elif T == 'cam':
            put(b.get('zoomAt'), whoosh(0.5), 0.45); put(b.get('shootAt'), shutter(), 0.9)
        elif T == 'upload':
            d0 = b.get('dropAt', b['at'] + 0.3)
            for i in range(len(b.get('thumbs', []))): put(d0 + i * 0.16 + 0.3, pop(), 0.45)
            put(b.get('clickAt'), click(), 1.0); put(b.get('clickAt', 0) + 0.12 + b.get('barDur', 1.3), sparkle(), 0.6)
        elif T == 'logo':
            put(b.get('logoAt'), sparkle(1.2), 0.9); put(b.get('logoAt'), pop(), 0.6)
        elif T == 'grid6':
            put(b.get('endAt'), pop(), 0.7); put(b.get('endAt'), sparkle(), 0.5)
        elif T == 'offer':
            put(b['at'], pop(), 0.7); put(b.get('urlAt'), click(), 0.6)
        elif T in ('brand', 'subscribe'):
            put(b.get('clickAt'), click(), 1.0); put(b.get('brandAt'), sparkle(), 0.7)
        elif T == 'list':
            for it in b.get('items', []):
                if it.get('markAt') is not None: put(it['markAt'], pop(), 0.35)
    mix = np.zeros_like(fx)
    mix[:len(voice)] += voice
    # duck SFX a little under speech
    win = int(0.05 * SR)
    env = np.convolve(np.abs(np.pad(voice, (0, len(fx) - len(voice)))), np.ones(win) / win, mode='same')
    duck = 1.0 - 0.45 * np.clip(env / (env.max() + 1e-9) * 3, 0, 1)
    mix += 0.30 * fx * duck
    peak = np.abs(mix).max()
    if peak > 0.97: mix *= 0.97 / peak
    pcm = (mix * 32767).astype(np.int16)
    with wave.open(out_p, 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
    print('mixed', out_p, 'dur', round(len(mix) / SR, 2), 'voice_peak', round(float(np.abs(voice).max()), 3), 'fx_peak', round(float(np.abs(0.30 * fx).max()), 3))

if __name__ == '__main__':
    main(*sys.argv[1:4])
