"""Validate episode text files: 100 turns, Korean line under each, no turn numbers, vocab/grammar counts, key expressions present."""
import re, sys
bad = 0
for path in sys.argv[1:]:
    t = open(path, encoding="utf8").read()
    head, rest = t.split("## 대화", 1)
    dlg, rest = rest.split("## 주요 단어", 1)
    vocab, gram = rest.split("## 문법·표현 정리", 1)
    gram = gram.split("## 완결")[0]
    d = [l for l in dlg.strip().split("\n") if l.strip()]
    errs = []
    if len(d) != 200: errs.append(f"turns={len(d)//2} (lines {len(d)})")
    for i in range(0, len(d) - 1, 2):
        if not re.match(r"^[A-Z][A-Za-z ]+: ", d[i]): errs.append(f"speaker? {d[i][:40]}")
        if re.match(r"^\d+\.", d[i]): errs.append(f"numbered: {d[i][:30]}")
        if not re.search(r"[가-힣]", d[i + 1]): errs.append(f"no Korean: {d[i+1][:40]}")
    nv = len([l for l in vocab.strip().split("\n") if l.strip()])
    ng = len([l for l in gram.strip().split("\n") if l.strip()])
    if not 12 <= nv <= 16: errs.append(f"vocab={nv}")
    if not 8 <= ng <= 15: errs.append(f"grammar={ng}")
    body = " ".join(d[0::2]).lower()
    for e in re.sub(r"^핵심 표현:", "", head.strip().split("\n")[2]).split("·"):
        for k in re.split(r"…", e.strip().lower()):
            k = k.strip(" ?!.,")
            if k and k.split("(")[0].strip() not in body: errs.append(f"expr missing: {e.strip()}")
    print(path, "OK" if not errs else errs, f"[vocab {nv}, grammar {ng}]")
    bad += bool(errs)
sys.exit(bad)
