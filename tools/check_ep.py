"""Validate episode text files: N turns (default 100), Korean line under each, no turn numbers, vocab/grammar counts, key expressions present.

usage: python3 check_ep.py [--turns 150] [--vocab 15-18] [--grammar 10-15] ep01.txt [ep02.txt ...]
"""
import argparse, re, sys

ap = argparse.ArgumentParser()
ap.add_argument("--turns", type=int, default=100)
ap.add_argument("--vocab", default="12-16")
ap.add_argument("--grammar", default="8-15")
ap.add_argument("paths", nargs="+")
a = ap.parse_args()
vmin, vmax = map(int, a.vocab.split("-"))
gmin, gmax = map(int, a.grammar.split("-"))

bad = 0
for path in a.paths:
    t = open(path, encoding="utf8").read()
    head, rest = t.split("## 대화", 1)
    dlg, rest = rest.split("## 주요 단어", 1)
    vocab, gram = rest.split("## 문법·표현 정리", 1)
    gram = gram.split("## 완결")[0]
    d = [l for l in dlg.strip().split("\n") if l.strip()]
    errs = []
    if len(d) != a.turns * 2: errs.append(f"turns={len(d)//2} (lines {len(d)})")
    for i in range(0, len(d) - 1, 2):
        if not re.match(r"^[^\W\d_][^\W\d_ '’-]*(?:[ '’-][^\W\d_]+)*: ", d[i]): errs.append(f"speaker? {d[i][:40]}")
        if re.match(r"^\d+\.", d[i]): errs.append(f"numbered: {d[i][:30]}")
        if not re.search(r"[가-힣]", d[i + 1]): errs.append(f"no Korean: {d[i+1][:40]}")
        if re.search(r"[가-힣]", d[i]): errs.append(f"Korean in speaker line: {d[i][:40]}")
    nv = len([l for l in vocab.strip().split("\n") if l.strip()])
    ng = len([l for l in gram.strip().split("\n") if l.strip()])
    if not vmin <= nv <= vmax: errs.append(f"vocab={nv}")
    if not gmin <= ng <= gmax: errs.append(f"grammar={ng}")
    body = " ".join(d[0::2]).lower().replace("’", "'")
    for e in re.sub(r"^핵심 표현:", "", head.strip().split("\n")[2]).split("·"):
        for k in re.split(r"…", e.strip().lower().replace("’", "'")):
            k = k.strip(" ?!.,")
            if k and k.split("(")[0].strip() not in body: errs.append(f"expr missing: {e.strip()}")
    print(path, "OK" if not errs else errs, f"[vocab {nv}, grammar {ng}]")
    bad += bool(errs)
sys.exit(bad)
