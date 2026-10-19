#!/usr/bin/env python3
"""Check a sentence-analysis file against its episode.
Usage: check_analysis.py EPISODE.txt ANALYSIS.md"""
import re, sys

def turns(ep):
    lines = open(ep, encoding='utf-8').read().split('\n')
    a = lines.index('## 대화') + 1
    b = next(i for i, l in enumerate(lines) if l.startswith('## 주요 단어'))
    body = [l for l in lines[a:b] if l.strip()]
    return [(body[i], body[i + 1]) for i in range(0, len(body), 2)]

def entries(path):
    txt = open(path, encoding='utf-8').read()
    out = []
    for blk in re.split(r'\n(?=## T\d{3} \| )', '\n' + txt):
        blk = blk.strip()
        if not blk.startswith('## T'):
            continue
        d = {'head': blk.split('\n')[0]}
        for l in blk.split('\n')[1:]:
            m = re.match(r'(FR|KO|단어|문법|시제): ?(.*)', l)
            if m:
                d[m.group(1)] = m.group(2).strip()
        out.append(d)
    return out

def main(ep, an):
    t, e = turns(ep), entries(an)
    errs = []
    if len(t) != len(e):
        errs.append(f'entries={len(e)} turns={len(t)}')
    for i, ((fr, ko), d) in enumerate(zip(t, e), 1):
        if d['head'][:6] != f'## T{i:03d}':
            errs.append(f'T{i:03d}: bad header {d["head"][:20]}')
        if d.get('FR') != fr.strip():
            errs.append(f'T{i:03d}: FR mismatch')
        if d.get('KO') != ko.strip():
            errs.append(f'T{i:03d}: KO mismatch')
        for k in ('단어', '문법', '시제'):
            if not d.get(k):
                errs.append(f'T{i:03d}: missing {k}')
    print(an, 'OK' if not errs else errs[:15], f'[{len(errs)} errors]' if errs else '')
    return not errs

if __name__ == '__main__':
    sys.exit(0 if main(sys.argv[1], sys.argv[2]) else 1)
