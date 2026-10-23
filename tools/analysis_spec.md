# Sentence-analysis spec (for Korean learners of French)

Input: an episode file `french/partN/epNN.txt` with a `## 대화` section of exactly 150 turns. Each turn = 2 lines: `Speaker: French text` (may include stage directions in parentheses), then its Korean translation.
Output: `french/partN/analysis/epNN.md` with ONE entry per turn, in order, T001…T150, in EXACTLY this format (blank line between entries, nothing else in the file):

## T001 | Speaker
FR: <French line copied EXACTLY incl. "Speaker: " prefix — copy programmatically>
KO: <Korean line copied EXACTLY>
단어: <2–6 key words/expressions as `French = 한국어 뜻`, separated by ` · `; infinitive for verbs, m./f. for nouns where useful>
문법: <1–4 grammar points in Korean, separated by ` / `, quoting the French fragment explained (pronouns, word order, negation, questions, articles, agreement, relative pronouns, idioms, register)>
시제: <EVERY conjugated verb in the spoken text (and important ones in stage directions) as `form(infinitive) = 시제 명칭(French name), 인칭`, separated by ` · `. Names: 직설법 현재(présent), 복합과거(passé composé), 반과거(imparfait), 대과거(plus-que-parfait), 단순과거(passé simple), 단순미래(futur simple), 전미래(futur antérieur), 근접미래(futur proche), 근접과거(passé récent), 조건법 현재/과거, 접속법 현재/과거, 명령법, 제롱디프, 현재분사, 동사원형. No verb → `동사 없음(명사문·감탄)`. Short note when the tense choice matters.>

Rules: exactly 150 entries; FR/KO byte-identical to the source; each field on ONE line; no blank lines inside an entry. Be accurate; explanations clear for A2–B1 learners. Style example: french/part1/analysis/ep01.md (first ~40 lines).
Check: `python3 tools/check_analysis.py french/partN/epNN.txt french/partN/analysis/epNN.md` must print OK.
