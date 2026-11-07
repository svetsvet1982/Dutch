"""Build a part .docx from episode text files, using tools/template.docx for styles.

usage (from repo root): python3 consulting/tools/build_docx.py OUT.docx "Title" "1부 ..." ep01.txt [...]
"""
import copy, re, sys
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

KO, LAT = "Malgun Gothic", "Calibri"


def run(p, text, size=10.5, bold=False, italic=False, color=None, font=LAT):
    r = p.add_run(text)
    r.bold, r.italic = bold, italic
    r.font.size = Pt(size)
    rpr = r._r.get_or_add_rPr()
    f = rpr.find(qn("w:rFonts"))
    if f is None:
        f = OxmlElement("w:rFonts"); rpr.insert(0, f)
    for a in ("w:ascii", "w:hAnsi", "w:cs"):
        f.set(qn(a), font)
    f.set(qn("w:eastAsia"), KO)
    if color:
        r.font.color.rgb = RGBColor.from_string(color)
    return r


def shade(el, fill):
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), fill)
    el.append(shd)


def rich(p, text, size=10.5):
    """**bold** segments in Latin font, the rest Korean font."""
    for i, seg in enumerate(re.split(r"\*\*", text)):
        if seg:
            run(p, seg, size, bold=(i % 2 == 1), font=KO)


def table(doc, rows):
    t = doc.add_table(rows=0, cols=3)
    t.style = "Table Grid"
    for k, row in enumerate(rows):
        cells = t.add_row().cells
        for c, txt in zip(cells, row):
            p = c.paragraphs[0]
            if k == 0:
                shade(c._tc.get_or_add_tcPr(), "DDE5F2")
            run(p, txt, 9.5, bold=(k == 0), font=LAT if (k and c is cells[0]) else KO)
    return t


def episode(doc, path, last=False):
    txt = open(path, encoding="utf8").read()
    head, rest = txt.split("## 대화", 1)
    dlg, rest = rest.split("## 주요 단어", 1)
    vocab, rest = rest.split("## 표현·문법 정리", 1)
    gram, rest = rest.split("## 컨설팅 스킬 노트", 1)
    skill, _, epilogue = rest.partition("## 완결")
    epilogue = epilogue or None
    lines = [l for l in head.strip().split("\n") if l.strip()]
    title = lines[0].lstrip("# ").strip()
    level, place, when = [x.strip() for x in lines[1].split("|")]
    issue = lines[2].replace("배경 현안:", "").strip()
    expr = lines[3].replace("핵심 표현:", "").strip()
    skillname = lines[4].replace("💼 스킬:", "").strip()

    h = doc.add_paragraph(style="Heading 1"); run(h, title, 18, italic=True, font=KO)
    p = doc.add_paragraph(); run(p, level, 10.5, bold=True, font=KO); run(p, f" · {place} · {when}", 10.5, font=KO)
    p = doc.add_paragraph(); shade(p._p.get_or_add_pPr(), "EEF2F8")
    run(p, "배경 현안:", 10, bold=True, font=KO); run(p, " " + issue, 10, font=KO)
    p = doc.add_paragraph(); shade(p._p.get_or_add_pPr(), "EEF2F8")
    run(p, "핵심 표현:", 10, bold=True, font=KO); run(p, " " + expr, 10)
    p = doc.add_paragraph(); shade(p._p.get_or_add_pPr(), "EEF2F8")
    run(p, "💼 스킬:", 10, bold=True, font=KO); run(p, " " + skillname, 10, font=KO)

    d = [l for l in dlg.strip().split("\n") if l.strip()]
    i = 0
    while i < len(d):
        if d[i].startswith("— "):
            p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(10)
            run(p, d[i], 11, bold=True, color="2F4A7A", font=KO); i += 1; continue
        spk, _, line = d[i].partition(": ")
        p = doc.add_paragraph(); run(p, spk + ":", 10.5, bold=True); run(p, " " + line, 10.5)
        p = doc.add_paragraph(); p.paragraph_format.left_indent = Cm(0.9)
        run(p, d[i + 1], 10, italic=True, color="555555", font=KO); i += 2

    h = doc.add_paragraph(style="Heading 2"); run(h, "📚 주요 단어", 13, italic=True, font=KO)
    rows = [("네덜란드어", "한글 발음", "뜻")] + [tuple(x.strip() for x in l.split("|")) for l in vocab.strip().split("\n") if l.strip()]
    table(doc, rows); doc.add_paragraph()

    h = doc.add_paragraph(style="Heading 2"); run(h, "📝 표현·문법 정리", 13, italic=True, font=KO)
    for n, l in enumerate([l for l in gram.strip().split("\n") if l.strip()], 1):
        p = doc.add_paragraph(); run(p, f"{n}. ", 10.5); rich(p, l)
    h = doc.add_paragraph(style="Heading 2"); run(h, "💼 컨설팅 스킬 노트", 13, italic=True, font=KO)
    for l in [l for l in skill.strip().split("\n") if l.strip()]:
        p = doc.add_paragraph(); shade(p._p.get_or_add_pPr(), "EEF2F8"); rich(p, l)
    if epilogue:
        lines = [l for l in epilogue.strip().split("\n") if l.strip()]
        doc.add_paragraph()
        h = doc.add_paragraph(style="Heading 2"); run(h, lines[0], 13, italic=True, font=KO)
        for l in lines[1:]:
            p = doc.add_paragraph(); rich(p, l)
    if not last:
        doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def main(out, title, sub, *eps):
    doc = Document("tools/template.docx")
    body = doc.element.body
    for el in list(body):
        if el.tag != qn("w:sectPr"):
            body.remove(el)
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_before = Pt(160)
    run(p, title, 26, italic=True, font=KO)
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run(p, sub, 13, font=KO); p.add_run().add_break(WD_BREAK.PAGE)
    for i, e in enumerate(eps):
        episode(doc, e, last=(i == len(eps) - 1))
    doc.save(out)


if __name__ == "__main__":
    main(*sys.argv[1:])
