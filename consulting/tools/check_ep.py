"""Validate consulting episodes: 120 turns, Korean line under each, scene markers, vocab 15, expressions 10-13, skill note, key expressions present.

usage: python3 consulting/tools/check_ep.py consulting/part1/ep01.txt ...
"""
import re, sys

TURNS = 120


def parse(t):
    head, rest = t.split("## 대화", 1)
    dlg, rest = rest.split("## 주요 단어", 1)
    vocab, rest = rest.split("## 표현·문법 정리", 1)
    gram, rest = rest.split("## 컨설팅 스킬 노트", 1)
    skill, _, end = rest.partition("## 완결")
    return head, dlg, vocab, gram, skill, end


bad = 0
for path in sys.argv[1:]:
    t = open(path, encoding="utf8").read()
    head, dlg, vocab, gram, skill, end = parse(t)
    hl = [l for l in head.strip().split("\n") if l.strip()]
    errs = []
    if len(hl) != 5 or not hl[1].startswith("수준:") or not hl[2].startswith("배경 현안:") or not hl[3].startswith("핵심 표현:") or not hl[4].startswith("💼"):
        errs.append("header format")
    lines = [l for l in dlg.strip().split("\n") if l.strip()]
    scenes = [l for l in lines if l.startswith("— ")]
    d = [l for l in lines if not l.startswith("— ")]
    if not scenes or not lines[0].startswith("— "): errs.append("scene marker missing")
    if len(d) != TURNS * 2: errs.append(f"turns={len(d)/2} (lines {len(d)})")
    for i in range(0, len(d) - 1, 2):
        if not re.match(r"^[A-ZÀ-Ý][\w .'’-]*: ", d[i]) or re.search(r"[가-힣]", d[i]): errs.append(f"speaker? {d[i][:50]}")
        if re.match(r"^\d+\.", d[i]): errs.append(f"numbered: {d[i][:30]}")
        if not re.search(r"[가-힣]", d[i + 1]) or re.match(r"^[A-Z][\w ]*: ", d[i + 1]): errs.append(f"bad Korean: {d[i+1][:50]}")
    nv = len([l for l in vocab.strip().split("\n") if l.strip()])
    ng = len([l for l in gram.strip().split("\n") if l.strip()])
    ns = len([l for l in skill.strip().split("\n") if l.strip()])
    if nv != 15: errs.append(f"vocab={nv}")
    if not 10 <= ng <= 13: errs.append(f"grammar={ng}")
    if ns < 3: errs.append(f"skill lines={ns}")
    body = " ".join(d[0::2]).lower().replace("’", "'")
    for e in hl[3].replace("핵심 표현:", "").split("·"):
        for k in re.split(r"…", e.strip().lower()):
            k = k.strip(" ?!.,").replace("’", "'")
            if k and k not in body: errs.append(f"expr missing: {e.strip()}")
    print(path, "OK" if not errs else errs[:8], f"[turns {len(d)//2}, scenes {len(scenes)}, vocab {nv}, expr {ng}, skill {ns}]")
    bad += bool(errs)
sys.exit(bad)
