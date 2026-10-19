#!/usr/bin/env python3
"""Build a sentence-analysis PDF for one part.

Usage: build_analysis_pdf.py PART_DIR OUT.pdf "Title" "Subtitle"
Reads PART_DIR/epNN.txt (episode headers) and PART_DIR/analysis/epNN.md,
renders HTML and prints it to PDF with headless Chromium.
"""
import html, os, re, subprocess, sys, tempfile

sys.path.insert(0, os.path.dirname(__file__))
from check_analysis import entries  # noqa: E402

CHROME = os.environ.get('CHROME', '/opt/pw-browsers/chromium-1194/chrome-linux/chrome')

CSS = """
@page { size: A4; margin: 16mm 14mm 16mm 14mm; }
body { font-family: 'Carlito', 'DejaVu Sans', 'NanumGothic', sans-serif; font-size: 9.6pt; color: #1d1d1f; line-height: 1.45; }
.cover { height: 250mm; display: flex; flex-direction: column; justify-content: center; text-align: center; }
.cover h1 { font-size: 34pt; margin: 0 0 6mm; letter-spacing: .02em; }
.cover h2 { font-size: 16pt; font-weight: normal; margin: 0 0 14mm; color: #444; }
.cover p { color: #666; font-size: 10.5pt; }
.legend { page-break-before: always; }
.legend h2, .ep h2 { font-size: 15pt; border-bottom: 2px solid #1f4e79; padding-bottom: 2mm; color: #1f4e79; margin: 0 0 3mm; }
.legend table { border-collapse: collapse; width: 100%; font-size: 9.2pt; }
.legend td, .legend th { border: 1px solid #ccd; padding: 1.6mm 2mm; vertical-align: top; }
.legend th { background: #eef3f9; text-align: left; }
.ep { page-break-before: always; }
.meta { color: #555; font-size: 9pt; margin-bottom: 1mm; }
.key { background: #fdf6e3; border-left: 3px solid #d4a017; padding: 1.5mm 3mm; margin: 2mm 0 4mm; font-size: 9.2pt; }
.t { border: 1px solid #dde3ea; border-radius: 2mm; padding: 2mm 3mm; margin: 0 0 2.4mm; page-break-inside: avoid; }
.n { color: #8a96a3; font-size: 8pt; margin-right: 1.5mm; }
.fr { font-size: 10.4pt; }
.fr b { color: #1f4e79; }
.sd { color: #7a7a7a; font-style: italic; }
.ko { color: #444; margin: .6mm 0 1.2mm; }
.row { display: grid; grid-template-columns: 11mm 1fr; gap: 1.5mm; font-size: 8.9pt; margin-top: .5mm; }
.lab { font-weight: bold; color: #fff; border-radius: 1mm; text-align: center; padding: .2mm 0; height: fit-content; }
.l1 { background: #2e7d32; } .l2 { background: #1565c0; } .l3 { background: #ad1457; }
"""

TENSES = [
    ('직설법 현재 (présent)', '지금의 사실·습관·일반 진리, 가까운 미래', 'Je travaille au Phare.'),
    ('복합과거 (passé composé)', '완료된 과거 사건. avoir/être + 과거분사', "J'ai vérifié. / Elle est partie."),
    ('반과거 (imparfait)', '과거의 배경·상태·습관 (진행 중이던 일)', 'Il pleuvait. Je travaillais.'),
    ('대과거 (plus-que-parfait)', '과거보다 더 이전의 일', "Il avait déjà signé."),
    ('단순미래 (futur simple)', '미래의 일·약속·예측', 'On publiera demain.'),
    ('근접미래 (futur proche)', 'aller + 동사원형: 곧 일어날 일', 'Je vais appeler.'),
    ('근접과거 (passé récent)', 'venir de + 동사원형: 방금 일어난 일', 'Je viens d\'arriver.'),
    ('조건법 (conditionnel)', '공손한 요청, 가정의 결과, 불확실한 정보(보도)', 'Je voudrais… / Il aurait vendu…'),
    ('접속법 (subjonctif)', 'il faut que, pour que, vouloir que 등 뒤에서', 'Il faut qu\'on vérifie.'),
    ('명령법 (impératif)', '명령·권유. 주어 없음', 'Écoute. / Allons-y.'),
    ('제롱디프 (gérondif)', 'en + 현재분사: 동시·방법·조건', 'en arrivant'),
]


def esc(s):
    return html.escape(s, quote=False)


def fr_html(line):
    sp, _, rest = line.partition(': ')
    body = esc(rest)
    body = re.sub(r'\(([^()]*)\)', r'<span class="sd">(\1)</span>', body)
    return f'<b>{esc(sp)}</b> {body}'


def episode_head(path):
    lines = open(path, encoding='utf-8').read().split('\n')
    title = lines[0].lstrip('# ').strip()
    meta = lines[1].strip()
    key = lines[2].replace('핵심 표현:', '').strip()
    return title, meta, key


def build(part_dir, out, title, subtitle):
    eps = sorted(f for f in os.listdir(part_dir) if re.fullmatch(r'ep\d\d\.txt', f))
    parts = [f'<div class="cover"><h1>{esc(title)}</h1><h2>{esc(subtitle)}</h2>'
             f'<p>대화 한 줄마다 원문 · 해석 · 주요 단어 · 문법 · 시제를 정리했습니다.</p></div>']
    rows = ''.join(f'<tr><td>{esc(a)}</td><td>{esc(b)}</td><td><i>{esc(c)}</i></td></tr>' for a, b, c in TENSES)
    parts.append('<div class="legend"><h2>읽는 법</h2>'
                 '<p><span class="lab l1">&nbsp;단어&nbsp;</span> 그 줄의 주요 단어와 뜻 &nbsp; '
                 '<span class="lab l2">&nbsp;문법&nbsp;</span> 문장 구조 설명 &nbsp; '
                 '<span class="lab l3">&nbsp;시제&nbsp;</span> 활용형(동사원형) = 시제, 인칭. '
                 '회색 기울임 글씨는 지문(무대 설명)입니다.</p>'
                 f'<h2 style="margin-top:6mm">시제 한눈에 보기</h2><table><tr><th>시제</th><th>쓰임</th><th>예</th></tr>{rows}</table></div>')
    for ep in eps:
        an = os.path.join(part_dir, 'analysis', ep.replace('.txt', '.md'))
        if not os.path.exists(an):
            sys.exit(f'missing {an}')
        t, meta, key = episode_head(os.path.join(part_dir, ep))
        parts.append(f'<div class="ep"><h2>{esc(t)}</h2><div class="meta">{esc(meta)}</div>'
                     f'<div class="key">핵심 표현: {esc(key)}</div>')
        for i, d in enumerate(entries(an), 1):
            parts.append(
                f'<div class="t"><div class="fr"><span class="n">{i}</span>{fr_html(d["FR"])}</div>'
                f'<div class="ko">{esc(d["KO"])}</div>'
                f'<div class="row"><span class="lab l1">단어</span><span>{esc(d["단어"])}</span></div>'
                f'<div class="row"><span class="lab l2">문법</span><span>{esc(d["문법"])}</span></div>'
                f'<div class="row"><span class="lab l3">시제</span><span>{esc(d["시제"])}</span></div></div>')
        parts.append('</div>')
    doc = f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(parts)}</body></html>'
    with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False, encoding='utf-8') as f:
        f.write(doc)
        src = f.name
    subprocess.run([CHROME, '--headless', '--no-sandbox', '--disable-gpu', '--no-pdf-header-footer',
                    f'--print-to-pdf={os.path.abspath(out)}', 'file://' + src],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    os.unlink(src)
    print('wrote', out)


if __name__ == '__main__':
    build(*sys.argv[1:5])
