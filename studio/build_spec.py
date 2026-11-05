"""Build a render spec from a scene plan + ElevenLabs Scribe words.

Usage: python3 build_spec.py plan.json words.json out_spec.json

In the plan, any value that is a string starting with "@" is a time anchor:
  "@كتلصق"      -> start time of the first word equal to (or starting with) كتلصق
  "@كتلصق#2"    -> second occurrence
  "@كتلصق+0.3"  -> offset in seconds (also -0.2)
  "@كتلصق#2/e"  -> end time instead of start
Anchors are searched from the previous anchor's position onward when the occurrence
is not given, so you can simply follow the script order.
"""
import json, re, sys

PUNCT = '،,.!?؟:…"«»'


def norm(s):
    return s.strip(PUNCT + ' ')


def main(plan_p, words_p, out_p):
    plan = json.load(open(plan_p, encoding='utf-8'))
    raw = json.load(open(words_p, encoding='utf-8'))
    if isinstance(raw, dict):
        raw = raw['words']
    words = [[w['text'], w['start'], w['end']] for w in raw if w.get('type', 'word') == 'word']
    toks = [norm(w[0]).lower() for w in words]
    cursor = [0]

    def resolve(a, move=True):
        m = re.match(r'^@(.+?)(?:#(\d+))?(/e)?([+-]\d+(?:\.\d+)?)?$', a)
        if not m:
            raise ValueError('bad anchor ' + a)
        q, occ, end, off = m.group(1), m.group(2), m.group(3), m.group(4)
        q = q.lower()
        hits = [i for i, t in enumerate(toks) if t == q or t.startswith(q)]
        if not hits:
            raise ValueError('anchor not found: ' + a)
        if occ:
            i = hits[int(occ) - 1]
        else:
            after = [i for i in hits if i >= cursor[0]]
            i = after[0] if after else hits[-1]
        if move:
            cursor[0] = i
        t = words[i][2] if end else words[i][1]
        return round(t + (float(off) if off else 0), 3)

    def walk(x, key=None):
        if isinstance(x, dict):
            return {k: walk(v, k) for k, v in x.items()}
        if isinstance(x, list):
            return [walk(v, key) for v in x]
        if isinstance(x, str) and x.startswith('@'):
            return resolve(x, move=(key not in ('end', 'happy', 'chapters')))
        return x

    spec = walk(plan)
    spec['words'] = words
    if spec.get('duration') in (None, 'auto'):
        spec['duration'] = round(words[-1][2] + 1.3, 2)
    json.dump(spec, open(out_p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('ok', out_p, 'duration', spec['duration'], 'words', len(words))


if __name__ == '__main__':
    main(*sys.argv[1:4])
