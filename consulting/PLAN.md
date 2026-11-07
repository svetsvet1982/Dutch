# 네덜란드어 비즈니스 대화문 「De Zuidas-jaren」 — 전체 기획서

> 배경: 암스테르담(Zuidas 중심) · 언어: 표준 네덜란드어(Algemeen Nederlands)
> 분량: 4부 × 14화 = **56화**, 1화 = 120턴 → 총 **6,720턴**
> 형식: 기존 서점 시리즈(`../PLAN.md`)와 같은 포맷(대사 → 한글 해석, 단어표, 표현 정리)을 이어 쓰고, 화마다 **💼 컨설팅 스킬 노트**를 하나 더 붙임

---

## 1. 한눈에 보기

| 항목 | 내용 |
|---|---|
| 제목(가제) | **De Zuidas-jaren** (주이다스 시절) — 암스테르담 금융·업무지구 Zuidas에서 시작해 헬몬트의 공장, 자신들의 사무실, 헤이그 정치판까지 가는 10년 |
| 장르 | 직장·비즈니스 드라마. 문제해결 → 전략수립 → 설득이 매 화의 뼈대 |
| 구성 | 1부 민간기업 컨설팅 / 2부 제조기업 CEO·CFO / 3부 독립 경영감사 / 4부 정치 컨설턴트 |
| 난이도 | 1부 B1→B2 · 2부 B2 · 3부 B2→C1 · 4부 C1 (화 안에서 섞는 규칙은 4장) |
| 한 화 구성 | 제목·수준·장소·시간·핵심 표현 → 대화 120턴(턴마다 한글 해석) → 📚 주요 단어 15개 → 📝 표현·문법 정리 10~13항목 → 💼 컨설팅 스킬 노트 1개 |
| 네덜란드 현안 | 각 화에 실제 사회·경제 이슈를 **배경**으로 넣음(주택난, 전력망 혼잡, 질소 위기, 수출통제, 흐로닝언 가스, 수당 스캔들, 연금 개혁 등 — 5장) |
| 실존 인물·기업 | **기업·정당·정치인은 모두 가상**. 감독기관·제도(DNB, AFM, CPB, KvK, 노조 FNV, 법률 이름 등)는 실명으로 써서 학습 가치를 살림 |
| 산출물 | 부별 Word 파일 4개(`consulting/part1-advies.docx` … `part4-politiek.docx`), 기존 `tools/` 스크립트를 120턴 기준으로 바꿔 재사용 |

### 부별 한 줄 요약

| 부 | 제목 | 무대 | 주인공의 자리 | 핵심 질문 |
|---|---|---|---|---|
| **1부** | **Het Advies** (조언) | Zuidas, 컨설팅사 «Keizer & Co» | 시니어 컨설턴트·애널리스트 | "옳은 답을 찾았다. 그런데 고객이 믿게 하려면?" |
| **2부** | **De Fabriek** (공장) | 헬몬트(브레인포트 에인트호번), 정밀부품 제조사 «Verhoef Precisie» | CEO·CFO | "남에게 조언하던 대로 내가 직접 할 수 있을까?" |
| **3부** | **De Audit** (감사) | 암스테르담 하우트하번스, 자신들의 회사 «Hoekstra Brouwer & Ramdin» | 독립 경영감사인 | "누가 무엇을 알고 있었나? 진실을 말하면 누가 다치나?" |
| **4부** | **De Campagne** (선거전) | 헤이그, 가상 정당 «Brug» | 정치 전략가 | "숫자와 논리로 사람의 마음을 움직일 수 있을까?" |

---

## 2. 등장인물

### 주인공 3인

| | **Femke Hoekstra** (펨커 훅스트라) | **Thijs Brouwer** (테이스 브라우어르) | **Priya Ramdin** (프리야 람딘) |
|---|---|---|---|
| 1부 나이·직책 | 33세, 시니어 컨설턴트 → 매니저 | 36세, 컨설턴트(전직 은행 리스크 분석가), 1부 1화에 입사 | 26세, 신입 데이터 애널리스트 |
| 출신 | 프리슬란트 레이우아르던. 농가 출신, 엘프스테덴 투흐트 이야기를 좋아함 | 로테르담 항구 노동자 집안. "Geen woorden maar daden"(말보다 행동) | 덴하흐(헤이그) 수리남계 힌두스탄 가정. 법학 중퇴 후 데이터 사이언스 |
| 강점 | 구조화·스토리텔링·설득, 회의실 장악 | 숫자·재무·협상, 차갑게 보일 정도로 정직 | 데이터·코딩·꼼꼼함, 정의감 |
| 약점 | 일 중독, 남에게 맡기지 못함 | 무뚝뚝함, 정치적 감각 부족 | 경험 부족, 상사 앞에서 말을 삼킴 → 부마다 성장 |
| 말투 | 직설적이지만 따뜻함. 회의에서는 `u`, 동료에게 `je` | 짧고 단호. 로테르담식 표현(`Gewoon doen.`) | 처음엔 공손한 `u`, 3부부터 거침없음 |
| 2부 | **CEO** | **CFO** | 데이터·IT 책임자(COO 대행) |
| 3부 | 공동창업 파트너(전략·지배구조 감사) | 공동창업 파트너(재무·포렌식) | **파트너로 승격**, 알고리즘 감사 담당 |
| 4부 | 정당 «Brug» 선거 전략가 | 선거 자금·공약 비용 계산(CPB 대응) | HBR 대표(독립성 유지), 딥페이크 독립 검증 |

> **언어 장치**: 세 사람은 지역·계층·세대가 달라 표준 네덜란드어 안에서도 말투 차이가 생김. 고객사 인물이 바뀔 때마다 새 어휘(금융·제조·의료·정치)가 들어와 화마다 학습 주제가 자연스럽게 달라짐.

### 주요 조연

| 인물 | 설명 | 등장 |
|---|---|---|
| **Maarten Keizer** (마르턴 케이저르) | Keizer & Co 창업 파트너, 58세. 노련하고 매력적이지만 "고객이 듣고 싶은 말"을 팔려 함. 1부의 멘토이자 갈등 축, 3부에서 감사 대상 회사의 자문역으로 재등장 | 1·3·4부 |
| **Ingrid van der Laan** | Keizer & Co 파트너, 50세. Femke의 진짜 멘토. "Wat is de vraag achter de vraag?"가 말버릇 | 1부, 4부 14화 |
| **Gerrit Verhoef** | Verhoef Precisie 창업자의 동생이자 COO, 61세. 현장 출신, 컨설턴트를 불신 → 2부 후반 최고의 동지 | 1부 13화~2부 |
| **Marloes Verhoef** | 창업자의 딸, 감독이사회(RvC) 위원, 39세. Femke를 CEO로 데려온 인물 | 1부 13~14화, 2부 |
| **Sevda Aksoy** | Verhoef의 노동자평의회(OR) 의장, 44세. 2부의 협상 상대, 3부에서 클라이언트를 소개 | 2·3부 |
| **Jeroen Bos** | 경제지 «Het Financieele Dagblad»풍 가상 신문 «De Beurskoerier» 기자. 매 부에 한 번씩 진실을 캐러 옴 | 전 부 |
| **Anouk Verbruggen** | 아메르스포르트 시장 출신, 신생 중도 정당 «Brug»의 대표(lijsttrekker), 47세 | 3부 14화, 4부 |
| **Kees Dijkhuizen** | «Brug»의 노련한 당 사무총장, 66세. 옛 정치의 화신, Femke와 사사건건 충돌 | 4부 |
| **Lotte & Jonas** | 전작 서점 시리즈 주인공. 프린센흐라흐트 서점 «De Tweede Pagina»가 Femke의 단골 서점으로 카메오 등장(1부 5화, 4부 14화) | 카메오 |

### 주요 장소

- **Zuidas**: Keizer & Co 사무실(가상 타워 12층), Gustav Mahlerplein, 암스테르담 남역(Station Zuid), VU 대학 근처 카페
- **헬몬트/에인트호번**: Verhoef Precisie 공장(가상), Brainport 산업단지, 에인트호번 스트레이프 지구
- **암스테르담 하우트하번스**: 3부 사무실(옛 목재 창고)
- **헤이그**: 국회(비넨호프는 장기 보수 공사로 임시 의사당 사용), Nieuwspoort 기자 클럽, Plein, 당사(가상)
- 그 밖: 담락 거리의 호텔, 알스메이르 화훼 경매장, 베스틀란트 온실, 로테르담 마스플락터 컨테이너 터미널, 헤이렌베인 자전거 공장, 흐로닝언 지진 피해 마을, 헬더르선 발레이 축산농가, 알메러 신도시, 스히폴 공항

---

## 3. 시간 흐름 (약 10년, 연도는 느슨하게)

| 부 | 시간 | 주인공 상황 |
|---|---|---|
| 1부 | 1년차 9월 → 2년차 6월 | Femke 매니저 승진 시험, Thijs 입사, Priya 신입 |
| 2부 | 2년차 9월 → 5년차 봄 (화 사이 시간 점프) | 헬몬트 이주, 공장 회생 |
| 3부 | 6년차 → 8년차 | 독립 창업, 감사 사건 12건 |
| 4부 | 9년차 2월 → 10년차 봄 | 조기 총선(6월)과 연정 협상 |

> 실제 연도를 박지 않아서 현안(예: 30% 루링 축소, 연금 이행 기한, 2026 지자체 예산 절벽)을 "지금 일어나는 일"로 자연스럽게 쓸 수 있게 함. 수치·제도는 집필 시점 기준으로 다시 확인.

---

## 4. 난이도와 언어 설계

### 부별 기본 곡선

| 부 | 주 수준 | 호칭 | 언어 초점 |
|---|---|---|---|
| 1부 | **B1 → B2** | 동료끼리 `je`, 고객사 경영진은 처음 `u` → 신뢰가 쌓이면 `je` | 회의·인터뷰·발표, 의견과 근거, 질문 기법 |
| 2부 | **B2** | 공장 현장은 `je`, 은행·주주·관청은 `u` | 협상·지시·위기 대응, 노사 협의, 재무 용어 |
| 3부 | **B2 → C1** | 감사 인터뷰는 철저히 `u`, 팀 내부는 `je` | 신중한 표현(hedging), 사실과 의견 구분, 보고서 문체, 법률 어휘 |
| 4부 | **C1** | 정치인끼리는 `je`, 공식 석상·언론은 `u` | 연설·토론·프레이밍, 관용구·속담, 행간 읽기, 외교적 거절 |

### 화 안에서 섞는 규칙 (120턴 기준)

- **주 수준 약 85턴 / 한 단계 아래 약 20턴 / 한 단계 위 약 15턴**
- 한 화는 보통 **3~4개 장면**(예: 팀 내부 준비 30턴 → 고객 미팅 50턴 → 복도/퇴근길 정리 40턴). 장면 전환은 `— Scène 2: … —` 줄로 표시
- 신입 Priya와 현장 인물(Gerrit, 노동자, 유권자)의 대사가 쉬운 문장을 담당하고, 이사회·관료·정치인의 대사가 어려운 문장을 담당
- 턴 길이: B1 1~2문장, B2 2~3문장, C1 3~4문장까지(발표·연설 장면은 한 턴 5문장까지 허용, 화당 최대 6턴)

### 부별 표현·문법 커리큘럼

| 부 | 핵심 표현·문법 |
|---|---|
| **1부** | 회의 시작·마무리(`Laten we beginnen met…`, `Om samen te vatten…`) / 의견·동의·반대(`Ik ben het (niet) met je eens`, `Dat klopt, maar…`) / 종속절 어순(dat, omdat, zodat, hoewel) / `zou`로 정중한 제안 / 수동태(`Er wordt gekeken naar…`) / 숫자·퍼센트·추세(`stijgen`, `dalen`, `met 12 procent`) / 질문 기법(열린·닫힌·후속 질문) / 네덜란드식 직설(`Eerlijk gezegd…`) 과 완화(`Misschien kunnen we…`) |
| **2부** | 지시·위임(`Ik wil dat jij…`, `Zorg ervoor dat…`) / 조건·양보(`mits`, `tenzij`, `ook al`) / 재무 용어(omzet, marge, kasstroom, convenant, EBITDA를 네덜란드어로 설명) / 협상(`Wat als we…?`, `Daar staat tegenover dat…`) / 위기 소통(`Wij betreuren…`) / `er` + 전치사 심화 / 분리동사 복합시제 / 현장 구어(`Dat gaat 'm niet worden`) |
| **3부** | 신중한 표현(`Het lijkt erop dat…`, `Voor zover wij hebben kunnen vaststellen…`) / 간접화법·시제 일치 / 대과거와 사건 재구성 / 관계대명사 심화(`hetgeen`, `waarbij`, `waarvan`) / 보고서 문체(명사화: `het niet naleven van…`) / 법률·감독 어휘 / 인터뷰 질문 설계 / 불리한 결론 전달하기 |
| **4부** | 연설 수사(3단 반복, 대조) / 프레이밍과 재프레이밍 / 관용구·속담(`De kool en de geit sparen`, `Wie A zegt, moet ook B zeggen`, `Water bij de wijn doen`) / 외교적 거절과 모호화 / 토론 반박(`Dat is een karikatuur van ons standpunt`) / 미디어 인터뷰 회피 기술 / 격식 서한·성명서 / 의회·연정 용어 |

---

## 5. 작품에 넣을 네덜란드 현안 (배경 자료)

| 분야 | 현안 | 쓰이는 화 |
|---|---|---|
| 주택 | 주택난(woningnood), 임대료 규제(Wet betaalbare huur), 주택조합의 곰팡이·유지보수 문제, 노동이민자 숙소 | 1-5·7, 3-2·3, 4-4 |
| 에너지·환경 | 전력망 혼잡(netcongestie), 온실 에너지 비용, 질소 위기(stikstofcrisis), PFAS 오염, 탈탄소 | 1-7, 2-5, 4-5 |
| 산업·안보 | 반도체 장비 대중 수출통제, 칩 공급망 위기, 외국인 투자 심사(Wet Vifo), 브레인포트 투자(Project Beethoven), 국방비 확대(NATO 목표)와 방위산업, 미국 관세 | 1-13, 2-3·4·9·10 |
| 노동 | 노동력 부족(krapte), 기술인력·MBO, 해외 인재 30% 루링 축소, 노동자평의회(OR)와 노조, 단체협약(cao) | 2-6·11 |
| 금융 | 은행 자금세탁방지(Wwft) 위반·벌금, 과잉 '디뱅킹', 은행 재무약정(convenant), WHOA 법정 외 구조조정 | 1-3·4·12, 2-7 |
| 유통 | 도심 다크스토어 규제(flitsbezorging), 상가 공동화, 해외 초저가 웹숍 경쟁 | 1-1·2·11·12 |
| 공공·복지 | 지자체 예산 절벽(ravijnjaar), 수당 스캔들(toeslagenaffaire)과 피해 회복, 복지 부정수급 알고리즘의 차별 논란, 청소년 돌봄 위기 | 3-6·12, 4-11 |
| 의료 | 지방 병원 응급실·분만실 폐쇄 논란, 의료보험사(zorgverzekeraar)의 힘, 간호 인력 부족 | 3-4·5 |
| 연금 | 새 연금제도 이행(Wtp, invaren) | 3-11 |
| 지배구조 | 이원 이사회(RvB/RvC), 기업지배구조 코드, 회계감사 품질 논란, 내부고발자 보호(Huis voor Klokkenluiders), 사이버 공격과 NIS2 | 1-4, 2-8, 3-7·8 |
| 정치 | 잦은 내각 붕괴·조기 총선, 신당 돌풍, CPB 공약 비용 계산, 여론조사(Peilingwijzer), Stemwijzer, 정찰자·정보관(verkenner/informateur), 연정 협정, 흐로닝언 가스 피해 보상, 이민·난민 수용, 딥페이크·허위정보, 비넨호프 보수 공사 | 4부 전체 |
| 관광 | 과잉관광, 관광세 인상, 단기임대(에어비앤비) 규제 | 1-5 |
| 항만·치안 | 로테르담 항을 통한 마약 밀수, 항만 내부자 부패, 자동화와 부두 노동자 파업 | 1-8·9 |
| 제조 | 자전거 업계 재고 위기, 아시아산 덤핑, 전기자전거 경쟁 | 1-10 |
| 기타 | 스히폴 운항 축소, 화훼 산업의 케냐 경쟁, 축구 클럽 재정(KNVB 라이선스), 교육 재단 예산 | 1-6, 3-9·10, 4-12 |

> 원칙: 현안은 **인물의 결정을 어렵게 만드는 조건**으로만 쓰고, 특정 정당·실존 정치인을 편들지 않음. 4부의 정당과 정치인은 모두 가상이며, 대립하는 견해를 각각 설득력 있게 대사로 보여 줌.

---

## 6. 서사 구조 (4부)

| 부 | 성장 단계 | 핵심 사건 | 마무리 장면 |
|---|---|---|---|
| 1부 | 분석가 → 설득하는 사람 | 고객사 8곳(배달 스타트업·은행·호텔·화훼·항만·자전거·백화점·제조사), Maarten과의 윤리 갈등, 브레인포트 피치 | Verhoef가 Femke에게 CEO, Thijs에게 CFO를 제안 |
| 2부 | 조언자 → 결정하는 사람 | 현금 위기·수출통제·랜섬웨어·외국 인수 제안·노사 대립, CEO와 CFO의 충돌 | 회생 완료, 회계 부정 사건을 계기로 독립 감사 회사 창업 결심 |
| 3부 | 결정하는 사람 → 진실을 말하는 사람 | 주택조합·병원·지자체·핀테크 내부고발·연금·알고리즘 감사, 자기 회사가 공격당함 | 알고리즘 감사 보고서가 화제가 되어 정당 대표가 Femke를 영입 |
| 4부 | 진실을 말하는 사람 → 사람을 움직이는 사람 | 공약 계산, 토론, 스캔들, 딥페이크, 개표, 연정 협상 | 장관 제안을 거절하고 암스테르담으로 돌아와 새 신입을 맞음(1부 1화의 거울) |

### 복선과 회수

- **"Wat is de vraag achter de vraag?"** (질문 뒤의 질문은 무엇인가) — Ingrid의 말버릇. 1부 1화 → 4부 14화에서 Femke가 신입에게 똑같이 말함
- **Femke의 노트**: 1부 1화에 산 몰스킨에 "고객에게 하지 말아야 할 말"을 적음 → 2부 12화 Thijs와 싸울 때 펼쳐 봄 → 4부 14화 신입에게 선물
- **Maarten Keizer**: 1부 13화 "Verhoef 일은 작게 시작해 크게 팔아라" → 3부 7·8화 핀테크 부정의 자문역 → 4부 7화 스캔들 제보자가 아님이 밝혀지며 화해
- **기자 Jeroen Bos**: 1부 3화 은행 취재 → 2부 8화 랜섬웨어 → 3부 13화 공격 기사 → 4부 7화 진실 확인 전화
- **Priya의 성장**: 1부 1화 회의에서 한마디도 못 함 → 1부 3화 첫 발견 → 2부 8화 위기 대응 지휘 → 3부 12화 단독 보고 → 4부 14화 회사 대표

---

## 7. 화별 기획 (56화)

표기: 수준 / 장소·시점 / 줄거리 / 네덜란드 현안 / 핵심 표현 / 💼 스킬

### 1부 · Het Advies (조언) — B1 → B2

> 무대: Zuidas의 컨설팅사 «Keizer & Co». **고객사 8곳**을 1~2화씩 다룸. 1~12화에서 7곳을 컨설팅하고, 13~14화의 8번째 고객사 Verhoef가 2부로 넘어가는 다리가 됨.

#### 1부 소재 8가지

| # | 고객사 | 업종·지역 | 화 | 핵심 과제 | 배경 현안 |
|---|---|---|---|---|---|
| 1 | **Fietsmand** | 장보기 배달 스타트업·암스테르담 노르트 | 1~2 | 적자 허브 정리, 생존 전략 | 다크스토어 규제, 배달원 고용 지위, 투자 한파 |
| 2 | **Noordbank** | 중견 은행·Zuidas | 3~4 | 자금세탁방지 개선, 감독이사회 보고 | Wwft 위반·벌금, 디뱅킹, EU AI법, 지배구조 코드 |
| 3 | **Grand Hotel Amstelzicht** | 호텔 그룹·암스테르담 중심가 | 5 | 성장 계획 vs 도시의 관광 억제 정책 | 과잉관광, 유럽 최고 수준의 관광세, 단기임대 규제 |
| 4 | **Van Leeuwen Bloemen** | 화훼 무역 가족기업·알스메이르/베스틀란트 | 6~7 | 가업 승계, 온실 에너지 | 케냐·에티오피아 경쟁, 스히폴 축소, 전력망 혼잡, 노동이민자 숙소 |
| 5 | **Maasvlakte Terminals** | 컨테이너 터미널·로테르담 항 | 8~9 | 자동화와 고용, 항만 보안 | 항만을 통한 마약 밀수와 내부자 부패, 부두 노동자 파업 |
| 6 | **Rijwielfabriek Friso** | 자전거 제조사·프리슬란트 헤이렌베인 | 10 | 재고 과잉, 공장 존폐 | 자전거 업계 재고 위기, 아시아산 덤핑, 전기자전거 경쟁 |
| 7 | **Van Dam Warenhuizen** | 백화점 체인·아메르스포르트 | 11~12 | 점포 폐쇄와 법정 외 회생 | 상가 공동화, 초저가 웹숍, OR 자문권, WHOA |
| 8 | **Verhoef Precisie** | 반도체 장비 부품 제조사·헬몬트 | 13~14 | 창업자 사망 후 전략 진단 → CEO·CFO 제안 | 대중 수출통제, 브레인포트 투자 |

#### 화별 기획

| 화 | 제목 | 수준 | 장소·시점 | 줄거리 | 현안 | 핵심 표현 | 💼 스킬 |
|---|---|---|---|---|---|---|---|
| 1 | Eerste dag op de Zuidas (주이다스 첫날) | B1 | Keizer & Co 사무실→Fietsmand 본사·9월 | 은행 출신 Thijs와 신입 Priya 입사. Femke가 첫 프로젝트 리드. 오후엔 바로 Fietsmand 킥오프, 창업자 인터뷰. Priya는 회의에서 한마디도 못 함 | 다크스토어 규제, 배달원 고용 지위 | Welkom bij het team · Wat is de vraag achter de vraag? · Mag ik even doorvragen? | 문제 정의(SCQ)·이슈 트리 |
| 2 | De stuurgroep (운영위원회) | B1~B2 | Fietsmand 회의실·4주 후 | "14개 허브 중 6개를 닫아야 한다." 창업자의 반발, Femke가 피라미드 원칙으로 설득 | 스타트업 투자 한파 | Ik begin met de conclusie · Dat is een harde boodschap · Wat als we niets doen? | 피라미드 원칙(결론 먼저) |
| 3 | Witwassen en wantrouwen (돈세탁과 불신) | B2 | Noordbank 본사→프로젝트룸·10월 | 감독당국(DNB)의 경고장. 현장 직원은 "또 컨설턴트냐". Priya가 의심거래 경보의 95%가 오탐이고 소상공인·이민자 고객이 과하게 계좌를 해지당했다는 걸 발견, 처음 발표. 기자 Jeroen Bos가 취재 전화 | Wwft 위반, 디뱅킹, EU AI법 | Er ligt een brief van de toezichthouder · Uit de analyse blijkt dat… · Wie is eigenaar van dit probleem? | 데이터로 이야기하기(so what?) |
| 4 | De raad van commissarissen (감독이사회) | B2 | Noordbank 이사회실·11월 | 이원 이사회 구조. CEO는 축소 보고를 원하고, Femke는 감독이사회에 있는 그대로 말함 | 기업지배구조 코드 | Met alle respect… · Ik zou u willen adviseren om… · Dat is niet onze rol | 어려운 메시지 전달 |
| 5 | Te veel toeristen? (관광객이 너무 많다?) | B1~B2 | 담락 거리의 호텔 로비→시청 앞→서점 «De Tweede Pagina»(카메오)·12월 | 호텔 그룹은 객실 300개 증설을 원하지만 시는 신규 호텔을 막고 관광세를 올림. Femke가 "더 많이"가 아니라 "더 오래, 더 좋게"로 전략을 바꾸자고 설득. 퇴근길에 단골 서점에 들름 | 과잉관광, 관광세 인상, 단기임대 규제 | De stad wil minder, niet meer · Wat voor gast willen we? · Kwaliteit boven kwantiteit | 외부 환경 분석(PESTEL) |
| 6 | Bloemen en bloedbanden (꽃과 핏줄) | B1~B2 | 알스메이르 가족 화훼 무역회사·1월 | 은퇴하는 아버지, 회사를 두고 다투는 세 남매. 경매장 새벽 풍경 | 케냐·에티오피아 경쟁, 스히폴 축소 | Het is een familiebedrijf, hè · Daar wil ik niet over praten · Iedereen heeft gelijk en niemand heeft gelijk | 이해관계 vs 입장 |
| 7 | De familieraad (가족 회의) | B2 | 베스틀란트 온실→아버지의 집·2월 | 온실 에너지비 폭등과 전력망 연결 대기 3년, 폴란드 노동자 숙소 문제를 숫자로 보여 준 뒤 가족 헌장(familiestatuut)을 만듦. Femke의 실수와 사과 | 전력망 혼잡, 노동이민자 숙소, 가업 승계 세제 | We zitten klem · Laten we elkaar laten uitpraten · Ik heb me vergist | 퍼실리테이션 |
| 8 | Containers en cocaïne (컨테이너와 코카인) | B2 | 로테르담 마스플락터 터미널·3월 | Thijs의 고향 무대. 터미널 운영사가 자동화 전략을 의뢰했는데, 현장 인터뷰 중 직원이 마약 조직에 매수되는 문제가 드러남. Thijs의 옛 동네 친구가 부두 노동자 | 항만 마약 밀수와 내부자 부패 | Hier praat niemand graag over · Dit valt buiten onze opdracht, maar… · Veiligheid gaat voor alles | 범위 관리(scope) |
| 9 | Staking op de kade (부두의 파업) | B2 | 노조 사무실→터미널 식당·3월 말 | 자동화 계획이 새어 나가 부두 노동자 파업. Thijs가 노조와 경영진 사이에서 재교육·고용 보장안을 협상. 처음으로 Thijs가 앞에 섬 | 부두 노동자 파업, 자동화와 일자리 | Geen woorden maar daden · Wat hebben jullie nodig? · Niemand valt tussen wal en schip | 노사 협상 |
| 10 | Stilstaande fietsen (멈춰 선 자전거) | B2 | 헤이렌베인 자전거 공장·4월 | 창고에 팔리지 않은 자전거 4만 대. Femke의 고향 프리슬란트. 공장을 닫을 것인가, 고급 전기자전거와 수리·구독 서비스로 갈 것인가. 아버지 세대 노동자들과의 대화 | 자전거 업계 재고 위기, 아시아산 덤핑 | Dit is meer dan een fabriek · Waar verdienen we nog geld aan? · We moeten durven kiezen | 사업 포트폴리오(BCG 매트릭스) |
| 11 | Winkelstraat in nood (위기의 상점가) | B2 | Van Dam 본사(아메르스포르트)→OR 회의실·5월 | 47개 점포, 3년 연속 적자. 18곳 폐쇄안에 OR의 자문권, 노조 FNV와 만남. Thijs의 무뚝뚝함이 일을 망칠 뻔함 | 상가 공동화, 초저가 웹숍, OR 자문권 | Wat maakt ons nog uniek? · Wij nemen uw advies serieus · Zonder draagvlak lukt het niet | 고객 세분화·지지 기반 만들기 |
| 12 | Het WHOA-akkoord (법정 외 회생 합의) | B2 | 법원 앞 카페·5월 말 | 임대인·채권자와 협상, 법원 인가. Maarten이 "추가 프로젝트를 팔아라"고 압박, Femke 거절 | WHOA 구조조정 제도 | Iedereen moet iets inleveren · Dit is ons laatste bod · Daar teken ik niet voor | 협상(BATNA) |
| 13 | Een pitch in Brainport (브레인포트 피치) | B2 | 헬몬트 «Verhoef Precisie» 공장·6월 | 창업자가 갑자기 별세한 반도체 장비 부품 회사. 딸 Marloes와 COO Gerrit 앞에서 피치. Gerrit: "양복쟁이들이 기계를 알아?" | 반도체 수출통제, 브레인포트 투자 | Wij kennen uw sector · Wat houdt u 's nachts wakker? · Geef ons zes weken | 피치·제안서 구조 |
| 14 | Een onmogelijk aanbod (거절할 수 없는 제안) | B2 | Zuidas 옥상 테라스→암스테르담 남역·6월 말 | 6주 진단 후 감독이사회가 Femke에게 CEO, Thijs에게 CFO를 제안. Maarten은 반대, Ingrid는 "가라". Priya도 따라가겠다고 함 | (정리 화) | Ik moet erover nadenken · Dit is een kans van mijn leven · Wie gaat er mee? | 커리어 결정 매트릭스 + 1부 총정리 |

### 2부 · De Fabriek (공장) — B2

> 무대: 헬몬트의 정밀부품 제조사 «Verhoef Precisie»(직원 340명, 매출의 60%가 한 대형 반도체 장비 고객). Femke=CEO, Thijs=CFO, Priya=데이터·IT. 조언하던 사람이 결정하는 사람이 되는 부.

| 화 | 제목 | 수준 | 장소·시점 | 줄거리 | 현안 | 핵심 표현 | 💼 스킬 |
|---|---|---|---|---|---|---|---|
| 1 | De eerste honderd dagen (첫 100일) | B2 | 공장 현장·9월 | 첫 출근. 작업복을 입고 현장을 돌며 직원 인사. Gerrit의 차가운 태도 | 브레인포트 지역 정체성 | Ik ben hier om te luisteren · Hoe gaat het hier echt? · Dat zien we dan wel | 100일 계획 |
| 2 | Cijfers onder de motorkap (보닛 아래의 숫자) | B2 | CFO실·9월 | Thijs가 재고 과다와 현금 부족을 발견. 은행 재무약정 위반까지 두 분기 | 금리·운전자본 | We hebben een kasprobleem · Waar zit het geld? · Dit moet vandaag op tafel | 현금흐름 13주 예측 |
| 3 | Eén klant van zestig procent (매출 60%짜리 고객) | B2 | 대형 고객사 구매팀(펠트호번)·10월 | 큰 고객이 가격 인하 8%를 요구. 의존도를 줄일 것인가, 더 묶일 것인가 | 반도체 공급망, 미국 관세 | Wij zijn een betrouwbare partner · Daar staat tegenover dat… · Dat kunnen wij niet waarmaken | 고객 포트폴리오 전략 |
| 4 | De exportvergunning (수출 허가) | B2 | 회의실·11월 | 중국 고객 대량 주문이 수출통제에 걸릴 수 있음. 영업이사는 "합법 범위"를 주장, Femke는 정부 확인을 택함 | 반도체 대중 수출통제, 이중용도 품목 | Is dit juridisch in orde? · We willen geen risico lopen · Integriteit is niet onderhandelbaar | 리스크 매트릭스 |
| 5 | Geen stroom voor groei (성장할 전기가 없다) | B2 | 새 공장동 공사현장·12월 | 새 공장동이 완공돼도 전력망 연결이 5년 뒤. 이웃 기업과 에너지 허브·배터리 공동 투자 협상 | 전력망 혼잡 | Het net zit vol · Samen staan we sterker · Wie betaalt wat? | 창의적 대안 찾기 |
| 6 | Handen tekort (일손이 없다) | B2 | 직업학교(MBO)·인도 출신 엔지니어 면접·1월 | 기술자 40명 부족. 학교와 협약, 해외 인재 채용, 그런데 집이 없음 | 노동력 부족, 30% 루링 축소, 지역 주택난 | We zoeken vakmensen · Wat bieden jullie? · Zonder huis geen medewerker | 인력 계획 |
| 7 | De bank aan tafel (은행과 마주 앉다) | B2 | 은행 회의실(에인트호번)·2월 | 재무약정 면제 협상. Thijs의 냉정함과 Femke의 비전이 처음 손발이 맞음 | 중소 제조업 자금난 | Wij vragen om een waiver · Wat is uw zekerheid? · Dit plan is realistisch | 은행 협상 |
| 8 | Gegijzeld (인질로 잡힌 공장) | B2 | 위기 대응실·3월 밤 | 랜섬웨어로 생산 정지. Priya가 대응을 지휘. 기자 Jeroen Bos의 전화 | 사이버 공격, NIS2 지침 | Wij betalen geen losgeld · Wat weten we zeker? · Wij communiceren open | 위기 커뮤니케이션 |
| 9 | Een bod uit het buitenland (외국에서 온 인수 제안) | B2 | 감독이사회·4월 | 중국계 지분이 섞인 해외 펀드가 높은 가격을 제시. 투자 심사법(Wet Vifo) 검토 | 외국인 투자 안보 심사 | Het bod is aantrekkelijk, maar… · Wat betekent dit voor de banen? · Wij laten het toetsen | 이해관계자 영향 분석 |
| 10 | Defensie klopt aan (방위산업이 문을 두드리다) | B2 | 국방물자청 방문·5월 | 국방비 증액으로 방산 부품 주문 제안. 일부 직원이 반대 서명 | NATO 국방비 목표, 방위산업 확대 | Dit is een ethische vraag · Iedereen mag zijn mening geven · Wij maken een bewuste keuze | 가치 기반 의사결정 |
| 11 | De ondernemingsraad zegt nee (노동자평의회의 거부) | B2 | OR 회의실·9월(1년 후) | 교대제 개편안에 OR 의장 Sevda가 부정적 자문, 파업 경고. Femke가 현장 교대조와 밤샘 근무를 함께 함 | 단체협약, 교대근무 건강 문제 | Wij hebben u niet goed betrokken · Wat als we het samen ontwerpen? · Afspraak is afspraak | 변화관리(ADKAR) |
| 12 | CEO tegen CFO (CEO 대 CFO) | B2 | Femke의 집→공장 주차장·이듬해 2월 | 사모펀드 투자안을 두고 Thijs(재무 안정)와 Femke(독립·성장) 정면충돌. Femke가 1부의 노트를 펼침 | 사모펀드의 제조업 인수 붐 | Je luistert niet naar me · Ik vertrouw jouw cijfers, niet je conclusie · We moeten dit oplossen, niet winnen | 갈등 해결·의사결정 규칙 |
| 13 | De aandeelhoudersvergadering (주주총회) | B2 | 헬몬트 시민회관·4월 | Verhoef 가족 주주들의 표결. Marloes의 결정적 한마디. 회생 성공 발표 | 가족기업 지배구조 | Ik geef het woord aan… · Het voorstel is aangenomen · Dit is het werk van iedereen | 이사회 보고서 작성 |
| 14 | Afscheid van Helmond (헬몬트와의 작별) | B2 | 공장 구내식당 송별회·5월 | 공급업체의 회계 부정이 밝혀지고 그 회사 감사인이 놓쳤다는 사실에 셋은 충격. "누군가는 진짜로 들여다봐야 해." 독립 감사 회사 창업 결심. Gerrit의 송별사 | 회계감사 품질 논란 | Bedankt voor alles · Jullie waren eerst pottenkijkers, nu familie · Wat gaan jullie nu doen? | 2부 총정리 |

### 3부 · De Audit (감사) — B2 → C1

> 무대: 암스테르담 하우트하번스의 옛 목재 창고, «Hoekstra Brouwer & Ramdin» (줄여서 HBR). 감독이사회·장관·시의회의 의뢰로 조직을 들여다보는 독립 경영감사(bestuurlijke audit). 한 사건을 1~2화로 다루며, 매 화 **인터뷰 → 증거 → 결론 전달**의 리듬.

| 화 | 제목 | 수준 | 장소·시점 | 줄거리 | 현안 | 핵심 표현 | 💼 스킬 |
|---|---|---|---|---|---|---|---|
| 1 | Een eigen naam op de deur (문패를 걸다) | B2 | 새 사무실·KvK 등록·6월 | 창업. 첫 고객을 못 구해 3개월. 노동자평의회 의장이던 Sevda가 주택조합을 소개 | 프리랜서·창업 행정 | Wie zijn wij en waar staan wij voor? · Onafhankelijkheid is ons product · We beginnen klein | 서비스 정의·가격 책정 |
| 2 | Schimmel in de boeken (장부 속의 곰팡이) | B2~C1 | 가상 주택조합 «Woonstede Zaanstreek»·9월 | 세입자 집의 곰팡이 민원 2,000건이 몇 년째 '처리 완료'로 표시. 이사회는 몰랐다고 함 | 주택조합 유지보수 부실, 주택난 | Uit de stukken blijkt… · Wanneer wist u dit? · Dat is mij niet bekend | 감사 인터뷰 설계 |
| 3 | Huurders aan het woord (세입자가 말하다) | B2~C1 | 세입자 집·주민 모임·10월 | 아이 천식으로 고생한 가족의 증언. 보고서 초안을 본 이사장이 문구를 바꿔 달라고 압박 | 주택조합 감독(Autoriteit woningcorporaties) | Wij passen de feiten niet aan · De toon kunnen we bespreken · Het rapport wordt openbaar | 사실과 해석 분리 |
| 4 | Spoed zonder spoed (응급 없는 응급실) | C1 | 지방 병원(가상 «Ziekenhuis Oostflank»)·11월 | 야간 응급실·분만실 폐쇄 결정의 근거 감사. 의사·간호사·주민의 분노 | 지방 병원 기능 축소, 간호 인력 부족 | Het gaat hier om mensenlevens · Op basis waarvan is dit besloten? · Er is geen eenvoudig antwoord | 의사결정 과정 감사 |
| 5 | De zorgverzekeraar (의료보험사) | C1 | 보험사 본사(자이스트)·12월 | 결정 뒤에 보험사 계약 압박이 있었음을 확인. 병원장은 희생양인가 | 보험사의 구매력, 의료비 상승 | Wie heeft hier de regie? · Dat is een interessante vraag, maar… · Formeel klopt dat | 권한·책임 매핑(RACI) |
| 6 | Het ravijnjaar (예산 절벽의 해) | B2~C1 | 가상 중소도시 «Wester-Amstel» 시청·1월 | 지자체 예산 절벽. 시가 소유한 폐기물 회사의 적자 감사. 시의원들 앞 공개 보고 | 지자체 재정 절벽(ravijnjaar) | De gemeente kan dit niet blijven betalen · Wij doen geen politieke uitspraken · Er zijn drie scenario's | 시나리오 분석 |
| 7 | Een anonieme mail (익명 메일) | C1 | HBR 사무실·카페·3월 | 결제 핀테크 «Payvaart» 직원의 내부고발: 매출 부풀리기. 자문역에 Maarten Keizer의 이름이 | 내부고발자 보호 제도 | Wij beschermen onze bron · Dit moet zorgvuldig · Is dit een vermoeden of een feit? | 포렌식 감사 절차 |
| 8 | Wie wist wat? (누가 무엇을 알았나) | C1 | Payvaart 감독이사회·Maarten과 독대·4월 | 회계감사인도 경고를 묵살. Maarten은 "몰랐다"고 하지만 메일이 남아 있음. 옛 스승에게 결론을 말하는 장면 | 금융감독(AFM), 감사 품질 | U had het kunnen weten · Ik zeg dit niet graag · Dit verandert alles | 불리한 결론 전달 |
| 9 | Het onderwijsgeld (교육 예산) | B2~C1 | 가상 초등학교 재단·5월 | 학습 회복 지원금이 컨설팅·리무진에 쓰임. 교사 부족 속 분노 | 교사 부족, 교육 재단 지배구조 | Het geld is niet bij de kinderen aangekomen · Wie heeft dit goedgekeurd? · Dat is pijnlijk | 지출 흐름 추적 |
| 10 | Rood-wit in het rood (적자의 적백군) | B2~C1 | 가상 프로축구 클럽 경기장·9월 | 클럽 재정 감사, 라이선스 강등 위기. 서포터와 시의 지원금 논쟁 | 축구 클럽 재정, 지자체 지원 | De club is van de stad · Emotie en cijfers gaan hier niet samen · Wij zijn geen supporters | 독립성 유지 |
| 11 | Invaren (새 연금제도로 갈아타기) | C1 | 가상 업종 연금기금·10월 | 새 연금제도 이행 결정의 지배구조 감사. 고령 가입자들의 불안 | 연금 개혁(Wtp) | Wat betekent dit voor mijn pensioen? · Er is geen garantie · Leg het uit alsof ik twaalf ben | 복잡한 것을 쉽게 설명하기 |
| 12 | Het algoritme (알고리즘) | C1 | 가상 대도시 사회복지국·12월 | Priya 단독 감사. 부정수급 탐지 알고리즘이 한부모·이민 배경 여성을 차별적으로 지목. 수당 스캔들의 그림자 | 복지 알고리즘 차별 논란, 수당 스캔들 | Het systeem discrimineert · Dat was nooit de bedoeling · Bedoeling is niet hetzelfde als effect | 알고리즘 감사 프레임 |
| 13 | Onder vuur (포화 속으로) | C1 | HBR 사무실·신문사·1월 | 기자 Jeroen Bos의 기사: "HBR의 감사도 편향됐나?" Priya의 데이터 실수 하나가 빌미. 셋이 함께 공개 정정 | 신뢰와 언론 | Wij hebben een fout gemaakt · De conclusie blijft overeind · Transparantie is onze enige verdediging | 실수 인정과 신뢰 회복 |
| 14 | Een telefoontje uit Den Haag (헤이그에서 온 전화) | C1 | 하우트하번스 부두·2월 | 알고리즘 보고서가 국회 질의로까지 이어짐. 신생 정당 «Brug» 대표 Anouk Verbruggen이 직접 찾아와 Femke를 선거 전략가로 영입하려 함. Thijs·Priya의 반응 | 내각 붕괴·조기 총선 | Politiek is niet mijn wereld · Juist daarom vraag ik u · Wat zou je doen als je niet bang was? | 3부 총정리 |

### 4부 · De Campagne (선거전) — C1

> 무대: 헤이그. 내각 붕괴로 조기 총선. 신생 중도 정당 «Brug»(가상, "다리를 놓는 정당")의 선거 전략가 Femke. Thijs는 공약 비용 계산, 당의 데이터 책임자 Sara Bakkali(신규)가 여론·데이터 담당. Priya는 HBR 대표로 남아 독립성을 지키며 8화에서 외부 검증자로 등장. 선거(1~9화) → 연정 협상(10~13화) → 귀환(14화).

| 화 | 제목 | 수준 | 장소·시점 | 줄거리 | 현안 | 핵심 표현 | 💼 스킬 |
|---|---|---|---|---|---|---|---|
| 1 | Den Haag roept (헤이그가 부른다) | C1 | 당사·기자 클럽 Nieuwspoort·2월 말 | 첫 출근. 사무총장 Kees: "정치는 감사가 아니오." 선거까지 110일 | 신당 돌풍, 비넨호프 보수 공사 | De kiezer is geen klant · Wat is ons verhaal? · In de politiek telt perceptie | 포지셔닝 |
| 2 | Het verkiezingsprogramma (선거 공약) | C1 | 당 강령위원회·3월 | 공약을 줄이고 다듬기. Thijs가 CPB 공약 비용 계산 대비 숫자를 맞춤 | CPB 공약 계산, 재정 규율 | Is dit doorgerekend? · Beloof niets wat je niet kunt waarmaken · Minder is meer | 우선순위 정하기 |
| 3 | De peilingen (여론조사) | C1 | 데이터룸·3월 | Sara의 분석: 지지율 4석, 젊은층·지방에서 약함. 전략적 투표의 함정 | 여론조사, 전략적 투표 | Peilingen zijn geen uitslagen · Waar zit onze groei? · We praten tegen de verkeerde mensen | 유권자 세분화 |
| 4 | Woningnood aan de deur (현관 앞의 주택난) | B2~C1 | 알메러·위트레흐트 가가호호 방문·4월 | Anouk와 함께 유권자 집을 돌며 청년·노부부의 목소리 듣기. 연설문 다시 쓰기 | 주택난, 청년 세대 박탈감 | Wat merkt u er zelf van? · Ik ga u niets beloven · Uw verhaal neem ik mee | 공감 인터뷰 |
| 5 | Stikstof en de boer (질소와 농부) | C1 | 헬더르선 발레이 축산농가·트랙터 시위·4월 | 농가의 분노, 자연보호 단체와의 대화. Anouk가 양쪽에서 비난받음 | 질소 위기, 농민 시위 | U begrijpt het niet · Wij willen een toekomst voor boer én natuur · Daar ga ik niet omheen draaien | 갈등 프레이밍 |
| 6 | Het debat (토론) | C1 | 리허설 스튜디오→방송국·5월 | 대표 토론회 준비. Femke가 상대 당 역할을 맡아 Anouk를 몰아붙임. 실제 토론에서 한 문장이 화제 | 이민·난민 수용 논쟁 | Dat is een karikatuur van ons standpunt · Laat me even uitpraten · De vraag is niet of, maar hoe | 토론 리허설·메시지 하우스 |
| 7 | Het lek (유출) | C1 | 당사 위기 회의·심야·5월 | 후보 명단 3번의 과거 사업 실패와 미납 세금이 유출. 누가 흘렸나? Maarten을 의심했다가 오해로 밝혀지고 화해 | 정치인 검증(screening) | Wie A zegt, moet ook B zeggen · Wij zijn niet perfect, wel eerlijk · Dit blijft niet bij één dag | 스캔들 대응 |
| 8 | Deepfake (딥페이크) | C1 | 데이터룸·방송국·6월 초 | 선거 열흘 전 Anouk의 가짜 영상이 퍼짐. 방송사가 HBR(Priya)에 독립 검증을 의뢰, Sara의 대응, 플랫폼·선관위 대응 | 허위정보, AI와 선거 | Dit is aantoonbaar nep · Wij gaan niet terugslaan met modder · De waarheid heeft tijd nodig | 허위정보 대응 |
| 9 | De verkiezingsavond (개표의 밤) | C1 | 선거 파티장·6월 수요일 밤 | 출구조사 9석 → 개표 후 11석. 환호와 눈물. 다음 날 아침 "이제 진짜 일이 시작된다" | 개표·의석 배분 | De exitpoll is binnen! · Dit hadden we niet durven dromen · Nu begint het pas | 성과 해석 |
| 10 | De verkenner (정찰자) | C1 | 국회 임시 의사당 방·6월 말 | 정찰자(verkenner)와의 면담. 어떤 연정이 가능한가, 무엇을 양보할 수 없는가 | 연정 구성 절차 | Wij sluiten niets uit · Onze rode lijnen zijn helder · Dat is geen breekpunt | 협상 전략 설계 |
| 11 | Onderhandelen in de achterkamer (밀실 협상) | C1 | 협상장 별관·7~8월 | 흐로닝언 지진 피해 보상, 수당 스캔들 피해자 회복, 국방비. 밤샘 협상, "포도주에 물을 타다" | 흐로닝언 가스 피해, 수당 스캔들 회복 | Wij moeten water bij de wijn doen · Wat krijgen wij daarvoor terug? · De kool en de geit sparen | 양보 교환(trade-off) |
| 12 | Het coalitieakkoord (연정 협정) | C1 | 협정문 작성실·9월 | 문구 한 단어를 두고 새벽까지 싸움("onderzoeken" vs "invoeren"). Kees와 Femke가 처음으로 서로를 인정 | 연금·이민·기후·스히폴 | Elk woord telt · Dit kunnen wij uitleggen aan onze kiezers · Een akkoord is nooit van één partij | 문서로 설득하기 |
| 13 | De bordesfoto (계단 사진) | C1 | 궁전 계단 앞·10월 | 새 내각 사진 촬영. Anouk가 Femke에게 차관직을 제안, Femke는 정중히 거절. 외교적 거절의 정석 | 내각 출범 | Ik voel me zeer vereerd, maar… · Mijn plek is ergens anders · U weet mij te vinden | 자기 역할 정의 |
| 14 | Terug aan de gracht (다시 운하로) | B2~C1 | 암스테르담 서점 «De Tweede Pagina»(카메오)→HBR 사무실·봄 | Priya가 HBR 대표가 되고, Thijs는 Verhoef 감독이사회로. Femke는 Ingrid와 재회한 뒤 HBR 신입에게 노트를 건네며 "질문 뒤의 질문은 뭐죠?" — 1부 1화의 거울 | (정리 화) | Wat is de vraag achter de vraag? · Ik heb veel geleerd, vooral van mijn fouten · Welkom bij het team | 시리즈 총정리 |

---

## 8. 한 화의 포맷 (서점 시리즈 양식 + 컨설팅 스킬 노트)

1. **제목 줄**: `N부 M화. Nederlandse titel (한글 제목)`
2. **수준 줄**: `수준: 중상급 (B2) | 장소: … | 시간: …`
3. **현안 줄**: `배경 현안: …` (한 줄, 한국어)
4. **핵심 표현 줄**: `핵심 표현: … · … · …`
5. **대화 120턴** — 턴 번호 없음, 장면 전환은 `— Scène 2: Bij de klant —`
   ```
   Femke: Goedemorgen allemaal. Laten we beginnen met de vraag waarom we hier zitten.
   좋은 아침입니다, 여러분. 우리가 왜 여기 앉아 있는지, 그 질문부터 시작하죠.
   Thijs: (kijkt op zijn laptop) De cijfers zijn slechter dan gedacht.
   (노트북을 보며) 숫자가 생각보다 나쁩니다.
   ```
6. **📚 주요 단어** 표 15개 (네덜란드어 / 한글 발음 / 뜻). 명사는 관사 포함, 동사는 원형 + 과거분사
7. **📝 표현·문법 정리** 10~13항목, 예문 + 한글 풀이 + 사용 장면(회의/이메일/발표)
8. **💼 컨설팅 스킬 노트** 1개: 그 화에서 쓰인 기법(예: MECE, 피라미드 원칙)을 네덜란드어 핵심 문장 3개와 함께 정리
9. 부 마지막 화 끝에 **🎉 N부 완결** 요약 + 다음 부 예고

### 120턴 기본 장면 설계 (예시: 1부 2화)

| 장면 | 턴 | 내용 |
|---|---|---|
| Scène 1 · 프로젝트룸 | 1~30 | 팀 내부 준비: 결론 정리, Priya의 데이터 확인, 예상 반론 연습 |
| Scène 2 · 운영위원회 | 31~85 | 고객 앞 발표: 결론 → 근거 3개 → 창업자 반발 → 질문과 재설득 |
| Scène 3 · 엘리베이터·남역 플랫폼 | 86~120 | 복기: 무엇이 통했고 무엇이 실패했나, 다음 단계, 인물의 감정선 |

---

## 9. 제작 방식과 품질 관리

1. **기획 확정 → 샘플 1화(1부 1화) 먼저 작성 → 서식·난이도·분량 확인** → 승인 후 본 작성
2. 화 단위로 대사 120턴 + 해석 + 단어표 + 표현 정리 + 스킬 노트를 한 번에 작성 (`consulting/part1/ep01.txt` …)
3. 자동 점검: 기존 `tools/check_ep.py`에 턴 수 옵션(120)과 💼 섹션 점검을 추가
   - 대사가 정확히 120턴인가 / 각 턴마다 한글 해석이 있는가 / 턴 번호가 없는가
   - 핵심 표현이 본문에 실제로 나오는가 / 단어 15개, 표현 10~13항목, 스킬 노트 1개
4. 부 단위로 docx 생성(`tools/build_docx.py` 재사용)
5. 사실 확인: 현안에 나오는 제도·수치(세율, 법 이름, 기관 권한)는 집필 직전에 최신 정보로 확인하고, 불확실한 수치는 대사에서 "약", "수천 건"처럼 처리
6. 원어민 검수 권장: 3~4부의 법률·정치 어휘, 관용구, 회의 장면의 자연스러운 직설 화법

---

## 10. 확인이 필요한 결정 사항 (기본값은 제가 정해 둠)

| # | 항목 | 기본값 | 대안 |
|---|---|---|---|
| 1 | 주인공 구성 | Femke(CEO)·Thijs(CFO)·Priya(데이터) 3인 | 2인 체제로 줄이기 |
| 2 | 난이도 | B1 → C1 | 전 부 B2 고정 / 한국어 학습자용으로 A2부터 |
| 3 | 2부 제조사 | 반도체 장비 부품(브레인포트) | 식품(치즈·유제품), 조선(로테르담), 자전거 |
| 4 | 4부 무대 | 조기 총선 + 연정 협상 | 지방선거(시의회), 유럽의회 선거 |
| 5 | 실존 기관 이름 | 감독기관·법률은 실명, 기업·정당·인물은 가상 | 모두 가상 |
| 6 | 전작과의 연결 | 서점 «De Tweede Pagina» 카메오 2회 | 연결 없음 |
| 7 | 💼 스킬 노트 | 화마다 1개 | 생략 / 부 끝에 몰아서 |
| 8 | 시간 흐름 | 약 10년, 연도 미표기 | 실제 연도(2026~) 명시 |

---

## 11. 집필 현황

| 부 | 상태 | 파일 |
|---|---|---|
| 1부 Het Advies (14화) | **완료** (각 화 120턴, 단어 15개, 표현 13항목, 스킬 노트) | `consulting/part1/ep01.txt` … `ep14.txt` → `consulting/part1/part1-advies.docx` |
| 2부 De Fabriek (14화) | **완료** | `consulting/part2/ep01.txt` … `ep14.txt` → `consulting/part2/part2-fabriek.docx` |
| 3부 De Audit (14화) | **완료** | `consulting/part3/ep01.txt` … `ep14.txt` → `consulting/part3/part3-audit.docx` |
| 4부 De Campagne (14화) | **완료** (시리즈 완결, 56화 6,720턴) | `consulting/part4/ep01.txt` … `ep14.txt` → `consulting/part4/part4-politiek.docx` |

- 도구: `consulting/tools/check_ep.py`(120턴·해석·장면 표시·단어 15·표현 10~13·스킬 노트·핵심 표현 점검), `consulting/tools/build_docx.py`(저장소 루트에서 실행, `tools/template.docx` 사용)
- 1부에서 생긴 설정(2부 이후 이어 쓸 것): Thijs의 부모 헹크(전 래싱공, 허리 부상)·헤르다(샤를루아), 아내는 교사(에인트호번으로 이사) / Femke의 어머니(레이우아르던), 할아버지(pake)는 농부 / Priya의 삼촌은 헤이그 식료품점 주인(계좌 해지 피해) / Keizer & Co 파트너 Maarten(이해충돌 갈등, "boos en trots"), Ingrid(멘토, 젊은 시절 해운사 제안을 거절한 후회) / Verhoef: 창업자 얀(67세, 4월 골프장 심장마비), 동생 헤릿(COO, "Ik ben een draaier, geen directeur"), 딸 마를루스(법률가, 감독이사), 감독이사회 의장 프란스 콜런, 최대 고객 구매 담당 라르스 더 빗(두 번째 공급업체 검토 중, 20~30%) / 진단 결과: 기계 가동 중단 31%, 재고 2년간 +60%, CFO 공석, 고객 주문 20% 감소 시 2분기 안에 은행 약정 위반, 채용 공고 38건 / 세 사람은 9월 1일 아침 7시 첫 출근, Priya는 데이터·IT 담당 / 기자 예룬 보스(«De Beurskoerier»)는 1부 3화에 첫 등장
- 2부에서 생긴 설정(3부 이후 이어 쓸 것): Verhoef 후임 체제 — CEO 마를루스, COO 아르준 메타(인도 출신, 아내와 딸), CFO 헤스터르 스미츠(전 은행 특별관리부), 헤릿은 주 2일 지도 선배 / OR 의장 세브다 악소이, 위원 헹크 / 야간 조 바스(뭐든 출력), 요스(58세, 손자), 에디(전 트럭 기사), 견습생 노아·야스미나, 엔지니어 리커(보스니아계, 국방 위원회 위원), IT 뤼트, 인사 마리커, 영업 롭, 구매팀 산너(피싱 메일 클릭 후 보안 교육 담당) / 얀의 부인 리트, 고모 리스, 사촌 바르트 / 테이스의 아내 메럴(교사, 하를럼으로 이사 희망) / 고객 라르스 더 빗·모니크 헤르만스(펠트호번), MedVision 한스페터(베스트), 헹얼로 방산 기업 / 펠란트 캐피털 파트너 산더르 콕(1부 Fietsmand 투자자) / 협력업체 프레시지코팅스 자위트의 회계 부정·파산(감사인이 4년간 적정 의견) → HBR 창업의 계기 / 마르턴: "Bij mij een audit? Dat zou ik nog wel eens willen zien." → 3부 7~8화 복선 / Femke의 새 수첩 표지: "Wat is de vraag achter de vraag?"(직원들이 선물) / HBR 사무실: 하우트하번스의 비 새는 옛 창고(창문이 예쁨) / 회사 이름 순서 농담(Hoekstra Brouwer & Ramdin)
- 3부에서 생긴 설정(4부에서 이어 쓸 것): HBR 사건 목록 — 주택조합 Woonstede Zaanstreek(대표 로버르트 스바르트 사임, 세입자 협회장 무라트·딸 엘리프, 파티마 엘 암라니) · 동부 병원 Oostflank(병원장 한네커 베스터르펠트, 응급의 요리스, 조산사 엘런, 보험사 조르흐사멘의 바르트 오버르베이크, 지역 협의체) · 베스터르암스털 시(재정 부시장 카린 데커르, 폐기물 회사 합병) · 핀테크 Payvaart(CEO 스벤 루룰프스 직무 정지, CFO 나디아 함디, 제보자 제시, 앤트워프 변호사 페르베커, 마르턴은 자문 계약 종료 후 젊은 컨설턴트 교육) · 교육 재단 킨트크라흐트(노르 선생님, 단) · 축구 클럽 SC 레인스타트(톤, 리뉘스, 유망주 야신) · 연금기금(헹크 판 오스, 리사) · 베스테르뷔르흐 생계 지원 알고리즘(사미라와 딸, 개발자 셈, 옴부즈맨) / 3부 13화: 부록 4의 필터 오류(4.2배→3.1배) 공개 정정, 기자 예룬 보스의 후속 기사, 벽의 네 번째 문장 "Vier ogen zien meer dan twee. Vooral om twee uur 's nachts." / Priya의 어머니(헤이그, 과거 생계 지원 수급, 두 번 조사받음, 사르나미어를 쓰는 할머니) / Femke의 할아버지 말: "우리 같은 사람이 아무도 안 가면 그들은 우리에 대해서만 말한다" / 4부 시작 조건: 내각 붕괴(망명법), 석 달 반 뒤 6월 총선, Brug 여론조사 4석, Anouk는 전 아메르스포르트 시장, Femke·Thijs는 HBR 휴직(문패에서 이름 제거), Priya가 «HBR Onderzoek» 대표, HBR은 선거 기간 해당 정당 책임 기관 조사 금지 / Femke의 세 조건: 계산된 공약만, 상대에 대한 거짓 없음, 선거 후 복귀(직책 없음)
- 4부에서 생긴 설정: 최종 의석 VN 33 · PvZ 23 · Samen Sterk 20 · Christen Verbond 13 · Brug 11(출구조사 9) · 농민당 7 / 리나 하두(명부 11번, 마지막 잔여 의석, 최연소 의원) / 정찰자 헤르다 뮐더르, 정보수집자 한스 더 볼프(전 흐로닝언 시장) / 연정 VN+SS+CV+Brug(77석) / 협정: 국가 30억 + 연금기금 보증 125억(늦어도 2027년 7월 1일 시행), 흐로닝언 집당 창구 하나, 알고리즘 사전 검증·"최종 결정은 항상 사람" / 아나우크 주택부 장관, 윌럼얀 브라우어르스 차관(펨커는 거절) / 케이스 은퇴(마르턴과 아흐테르훅 자전거), 빈 병 "Voor 1994"는 HBR 벽 선반에 / 사라는 CPB로, 테이스는 Verhoef 감독이사, 위레는 HBR 파트너, 신입 사너 베스트라(흐로닝언 로퍼르쉼, 피터르의 사촌) / 벽의 다섯 번째 문장: "Wie niets durft te vragen, heeft de beste vraag nog in zijn zak."
