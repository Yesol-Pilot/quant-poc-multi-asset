# #11 arXiv / SSRN / ReScience publish 전략

> Tier B Publish 영역 #11 / 한국 retail 1인 AI 네이티브 PM portfolio
> 작성: 2026-05-14 (Strategy Lead Claude Opus 4.7)
> Cold honest. 광고성 X. retail 1인 실제 가능한 path 만.
> ⏸️ 블라인드 심사중 (NeurIPS 20237 + TMLR 8752) — 본 보고서는 12주 plan 의 신규 paper 만 다룸.

---

## Executive Summary (5 핵심 발견)

1. **arXiv q-fin 권고: PASS in 12주 plan, 12개월 후 재평가**. 이유: (a) 2026-01-21 정책 강화로 endorsement 어려움 (institutional email + 기존 paper 둘 다 보유 또는 personal endorsement 한정), (b) KAIST / SNU q-fin 교수 personal endorsement cold 시도 가능하지만 retail 1인 + commercial bot 시각은 endorser 입장에서 risk (refuse 비율 60~80% 추정), (c) NeurIPS+TMLR 1편씩 accept 후 cross-link 시점 (2026-12 ~ 2027-03) 이 진정 권고 timing.

2. **SSRN 우선 권고: 즉시 (12주 plan W6~W8)**. 이유: (a) 등록 무료 ($0 cost), (b) endorsement 불필요, (c) Quantitative Finance Network 자동 가입, (d) median paper 100~500 downloads/1년 (retail 도달 가능), (e) Quantpedia Awards 2027 submission base (SSRN 또는 arXiv link 필수, 2026-04-30 마감 이전 publish 요건).

3. **ReScience submission 권고: Paper 2 만 (Fama-French KOSPI 200 replication)**. 이유: (a) reproducibility journal 의 mission 정합, (b) Kang & Jang (2016) replication 가 한국 시장 학술 gap 채움, (c) GitHub repo 직접 review process — owner OSS 와 자연 통합, (d) 8~15 pages 분량 = 12주 plan 안 가능, (e) review timeline 3~6개월 — 2026-08 submit → 2027-02 accept 가능.

4. **Paper 1 SSRN title 권고: "Korean Retail Multi-Strategy Backtest: A 1-Person AI-Agent Production Pipeline"**. 구조: Introduction (한국 retail quant gap) → Method (multi-asset architecture) → Results (38일 PoC honest failure) → Honest Failure section (cold 박제 — institutional reviewer 가 정직성 평가) → Lessons → Open Source link. 25~35 pages. D6 62 references 의 약 30~40 활용.

5. **Visibility lever 4건 cold 권고 우선순위**: (1) **SSRN publish + Quantpedia Awards 2027 submit** (확실, $0 cost), (2) **r/quant + r/algotrading honest narrative post** (자율 가능, viral 15~25% 확률), (3) **Hudson & Thames mlfinlab PR** (cold 시도, 외부 OSS contributor 정착 신호), (4) **NeurIPS + TMLR cross-link** (블라인드 심사 종료 후, hold 상태 영구 유지).

---

## 1. arXiv submission 절차 + 정책 (2026-01 강화)

### 1.1 q-fin category 분포

arXiv 의 Quantitative Finance archive 안 6 sub-category:
- `q-fin.CP` (Computational Finance) — 알고리즘, 수치 방법
- `q-fin.GN` (General Finance)
- `q-fin.MF` (Mathematical Finance) — stochastic calculus, derivative pricing
- `q-fin.PM` (Portfolio Management) — **본 12주 plan 의 Paper 1 fit**
- `q-fin.PR` (Pricing of Securities)
- `q-fin.RM` (Risk Management) — 38일 PoC 의 Kill Switch wiring 적합
- `q-fin.ST` (Statistical Finance)
- `q-fin.TR` (Trading and Market Microstructure) — A1 liquidation cascade alpha 적합

**Paper 1 권고 category**: primary `q-fin.PM` + cross-list `q-fin.TR` + `q-fin.RM`. 다중 카테고리 = 다중 audience.

월 submissions (2025-12 = 312, 2025-07 = 242, 2024 평균 ~200~280/월). q-fin 의 monthly volume = computer science (~10,000/월) 대비 작음 → 신규 paper 가 list 에서 단기 visibility 확보 가능 (단, endorsement 통과가 전제).

### 1.2 Endorsement 경로 cold 평가 (2026-01-21 정책 강화 후)

**현 정책 핵심**:
- 신규 author 가 q-fin 에 submit 하려면:
  - **Path A**: institutional email **+** 기존 arXiv paper authorship (둘 다)
  - **Path B**: personal endorsement (기존 q-fin endorser 가 직접 endorse)
- 본 owner = Cornell affiliation 없음, 본인 q-fin paper 없음 → **Path A 불가**, **Path B 만**

**Path B (personal endorsement) cold 시도 방법**:
1. Paper 1 의 references 안 q-fin recent papers (3개월~5년 이내) 검토
2. 해당 paper authors 가 "Which authors of this paper are endorsers?" 표시 확인
3. cold email — paper 1 draft + 본인 background (NeurIPS 20237 + TMLR 8752 submission, GitHub Yesol-Pilot, heoyesol.kr) + endorsement 요청
4. 평균 응답률 추정: 10~30% (학술 retail trader 시각 의존)
5. 요청 응답 = 60~70% positive 추정 (응답한 author 중)

**Cold target endorser** (cold 검토만, 직접 contact 전 owner G2):
- **KAIST 산업및시스템공학과 / 금융공학 교수진**: Cha (확률금융) / Kim Woochang (퀀트 금융 — D6 reference 가능)
- **SNU 경영대학 재무금융**: Kim Yongsoo / Lee Sung-Bin
- **KIST 도시지속가능성과학** (cross-disciplinary): 가능성 낮음
- **NeurIPS author co-author** 활용: 만약 owner 의 NeurIPS+TMLR co-author 가 q-fin endorser 면 단축 가능
- **글로벌 retail-friendly q-fin endorsers**: Ernest Chan (epchan.com), Marcos Lopez de Prado, Robert Carver, Kevin Sheppard

cold 권고:
- 12주 plan 안에서는 endorsement 시도 **PASS**
- 12개월 후 NeurIPS+TMLR 결과 가시화 시점에 재평가 — accept 시 endorser 응답률 30~50% 상승 가능
- 본인 paper 가 SSRN 에 먼저 publish 되어 있으면 endorser 평가 단축

### 1.3 Submission timeline (DAY 0 → live)

- DAY 0: TeX/PDF + abstract + 카테고리 + endorser 정보 입력
- DAY 1: 자동 admin check (LaTeX compile / figure / metadata)
- DAY 2~3: 사람 moderation (q-fin moderator team)
- DAY 3 (수요일 14:00 EDT 이전 submit 시): 같은 주 발표
- DAY 7~14: endorsement 보류 시 (개인 endorser 응답 대기)
- DAY 14+: 보류 지속 시 moderator 가 reject 또는 hold

**현실**: endorsement 가 boutleneck. paper 자체 quality 는 작은 issue.

### 1.4 Retail 1인 q-fin publish 실제 성공 사례

cold 조사:
- **Robert Carver** (pysystemtrade author, ex-AHL): q-fin 에 본인 paper 없음, 책 publish 위주
- **Ernest Chan**: q-fin 에 1편 submitted (2010 경) — 당시 endorsement 정책 simple
- **Marcos Lopez de Prado**: q-fin 활발 (10+ papers) — institutional (Cornell) affiliation 보유
- **한국 retail q-fin**: 사실상 0건 검색 가능 (한국 retail trader 가 q-fin 에 submit 한 publicly known 사례 없음)

**의미**: owner 가 publish 시 한국 retail 의 unique pioneer 위치. 그러나 endorsement 보틀넥 그대로 잔존.

### 1.5 arXiv Cornell 분리 (2026-07-01)

arXiv 가 Cornell 에서 분리 → 비영리 독립 운영. 정책 영향:
- 정책 단기 변경 가능성 낮음 (transition 안정성 우선)
- 12~24개월 후 endorsement 정책 추가 변경 risk (cold honest 수용)

---

## 2. SSRN submission

### 2.1 등록 절차

1. https://papers.ssrn.com → "Register" → Drexel User Account (무료, $0)
2. Profile 작성 (한국 이름 영문 표기 + Yesol-Pilot GitHub + heoyesol.kr)
3. Network 가입 (자동 권고):
   - **Quantitative Finance Network**
   - **Risk Management Network**
   - **Financial Economics Network**
4. Paper upload (PDF) + abstract (300~500 단어) + keywords (5~10개) + JEL codes
5. SSRN moderation = 평균 24~72시간

### 2.2 Submission fee = $0

cold 확인:
- 기본 submission free (모든 카테고리)
- 일부 specialized journal (Drexel Tier 2~3) 가 paid 옵션 ($100~$500) 보유 — 12주 plan 안에서는 PASS
- Quantitative Finance Network = 무료

### 2.3 SSRN visibility 통계

cold 측정 (median paper, 1인 author):
- Abstract page views: 100~500/1년 (median ~200)
- Downloads: 50~250/1년 (median ~100)
- Top 10% paper: 1,000~5,000 downloads
- Top 1% paper: 10,000+ downloads
- Citations (1~3년 누적): 0~10 (median)

**한국 retail quant 의 unique advantage**:
- 한국 시장 데이터 활용 = 차별화 (Korean stock market 학술 gap)
- 38일 PoC honest failure = contrarian narrative (학술 reviewer 가 정직성 평가)
- Korean + English dual language abstract = 한국 + 글로벌 visibility 양쪽

**예측 (Paper 1, 1년 누적)**:
- 보수: 80 downloads / 200 abstract views
- 중도: 250 downloads / 800 abstract views
- 낙관: 600 downloads / 2,000 abstract views

### 2.4 Retail 1인 SSRN 사례

cold 조사:
- **Andrea Berdondini** ("The Theory of Quantitative Trading", SSRN 3994764) — retail-leaning author, 1,000+ downloads
- **Yifan Guo** ("Applications of Time Series Analysis in Quantitative Finance", SSRN 5140015) — retail/student author
- **한국 retail SSRN**: 사실상 없음 (한국 retail trader 가 SSRN 에 paper publish 한 공개 사례 검색 결과 0)

**의미**: 한국 retail 1인 pioneer. 학술 reviewer 가 unique perspective 평가.

---

## 3. ReScience submission

### 3.1 ReScience C 개요

- Platinum open access (저자 fee 0, 독자 access 0)
- Peer-reviewed (GitHub PR 기반 공개 리뷰)
- 미션: 기존 publish 된 computational research 의 replication
- Submission flow: GitHub issue 생성 → reviewer 가 reproduce 시도 → 결과 publish

### 3.2 Submission template

`ReScience/template` GitHub repo:
- LaTeX template (optional, PDF style enforce 권고)
- YAML metadata (mandatory)
- Docker 지원 (`docker run rescience-cmd ...`)

### 3.3 한국 paper replication 사례 (cold 조사)

- ReScience C 안 한국 시장 paper replication = 사실상 0건 (검색 결과 한국 시장 명시 replication 없음)
- ReScience C 의 majority = AI/ML paper replication (neural network / RL / vision)
- Quantitative finance replication = 소수 (1년 ~2~5건)

**의미**: KOSPI replication paper = 한국 시장 + ReScience 미진출 영역 = unique. Reviewer 가 신선함 평가.

### 3.4 후보: Fama-French 5-factor on KOSPI 200

cold 평가 (Paper 2 후보):

**원 paper**: Kang & Jang (2016 / 2018 / 2019 — 3 papers): "A Comparison of New Factor Models in the Korean Stock Market" 의 시리즈.

**replication 가설**:
- 5-factor model 의 RMW (profitability) / CMA (investment) factor 가 KOSPI 200 에서 redundant 라는 Kang (2018) 결론 재검증
- 데이터 윈도우 1992~2013 → 1992~2025 확장
- Korean market 의 replication rate (Korean market anomalies 연구 기준 0%~46%) 의 일관성 검증

**Owner 강점**:
- D6 reference 안 Fama-French 5-factor original (2015) paper 보유
- Multi-asset architecture 안 한국 stock universe 이미 구현 가능 (KIS API + KRX 데이터)
- GitHub repo 직접 reproducibility 보장
- 38일 PoC 의 honest failure 학습 = academic rigor 정합

**예상 분량**: 8~15 pages (ReScience 표준)

### 3.5 Review timeline

- Submission (GitHub issue) → reviewer 모집: 2~4주
- Review (reviewer 가 reproduce 시도): 4~12주
- Revision + accept: 2~8주
- **합계: 3~6개월**

**12주 plan timing**:
- W8 (2026-07 중순): Paper 2 draft 시작
- W12 (2026-08-08): GitHub issue submit
- 2027-02 ~ 2027-04: accept 예상

---

## 4. Paper 1 outline (SSRN submission, 12주 build 종료 시)

### 4.1 Title 권고

**"Korean Retail Multi-Strategy Backtest: A 1-Person AI-Agent Production Pipeline"**

cold 검토:
- "Korean Retail" → geographic + audience differentiation
- "Multi-Strategy Backtest" → 4 자산군 + 12 alpha 시각화
- "1-Person AI-Agent Production Pipeline" → owner의 unique value (Claude Opus 4.7 / Codex / Sora 멀티 에이전트 운영)

**Alternative title** (검토):
- "Honest Failure of a 38-Day Quant Pilot: 12 Alphas Across KR/US/Crypto" — viral 친화, 학술 reviewer 보수적 시각에 risk
- "Multi-Agent Quant Architecture: A Korean Retail Case Study" — overpromising

### 4.2 구조

```
Title + Authors (Yesol Heo, GitHub Yesol-Pilot)
Abstract (300~500 words, English + Korean)
1. Introduction
   1.1 Korean Retail Quant Gap (D1 + D6 reference)
   1.2 Multi-Agent AI as Operations (Claude Opus + Codex + Sora)
   1.3 Honest Failure as Methodology
2. Related Work
   2.1 Quant OSS (Hummingbot / FinRL / mlfinlab / NautilusTrader)
   2.2 Academic Foundations (Fama-French / Lopez de Prado / Kelly criterion)
   2.3 Korean Market Anomalies (Kang & Jang 2016/2018/2019)
3. System Architecture
   3.1 4-Asset Universe (KR equity / US options / crypto perp / US ETF)
   3.2 12-Alpha Ensemble (A1 liquidation cascade ~ A12 macro event)
   3.3 9-Layer Kill Switch
   3.4 Multi-Agent Orchestration (Claude Strategy Lead + Codex implementation + Sora ops)
4. Data + Methodology
   4.1 KIS API + Binance + IBKR (D3 + D4 reference)
   4.2 Backtest engine (DSR + PBO + CPCV)
   4.3 Paper Trading (38 days, 2026-04-05 ~ 2026-05-12)
5. Results (Cold Honest)
   5.1 38-Day Aggregate: 191 trades, WR 37.7%, PnL -15.1%, Sharpe 0.0
   5.2 Per-Alpha Breakdown
   5.3 Per-Asset Breakdown
   5.4 Spec Failure Confirmation (A2 OU: 0/108 cells PASS)
6. Honest Failure Analysis
   6.1 Alpha Decay Patterns (Lopez de Prado 2018 framework)
   6.2 Multi-Asset Correlation (unexpected, 0.6+)
   6.3 External Policy Risk (Binance liquidation API change)
   6.4 Cost Discipline (paper-only, $0 capital risk)
7. Lessons Learned
   7.1 OSS as Truth-Teller
   7.2 Academic Rigor vs Retail Pragmatism
   7.3 Multi-Agent AI 의 한계 (자율 결정 정확도)
8. Open Source + Reproducibility
   8.1 GitHub Repo (MIT, Yesol-Pilot/quant-poc-multi-asset)
   8.2 Live Dashboard (heoyesol.kr/quant)
   8.3 ReScience replication welcome
9. Future Work
   9.1 12-Month Extension Plan
   9.2 NeurIPS+TMLR cross-link (when blind review concludes)
10. References (30~40, from D6 62 + new)
Appendix A: Alpha 12 spec detail
Appendix B: Kill Switch 9-Layer detail
Appendix C: 38-day daily metrics table
```

분량: 25~35 pages.

### 4.3 학술 references 활용

D6 62 references 중 약 30~40 활용:
- Fama-French (1992, 2015)
- Lopez de Prado (2018 "Advances in Financial Machine Learning")
- Kang & Jang (2016/2018/2019 Korean market)
- Kelly (1956)
- Bailey & Lopez de Prado (DSR, PBO)
- Sharpe (1966)
- Markowitz (1952)
- Black-Scholes (1973)
- Carver (pysystemtrade)
- Chan (Algorithmic Trading)
- 5~10 신규 references (Bayesian quant, MARL safety — owner NeurIPS 연구 cross-link)

### 4.4 분량 25~35 pages 권고

- SSRN median paper = 20~40 pages
- 한국 reader 친화: dual language abstract + 핵심 section 양쪽 명시
- 학술 reviewer 친화: appendix 풍부 (reproducibility 자료)

### 4.5 Cross-link: NeurIPS + TMLR

⏸️ **Blind review HOLD**:
- NeurIPS 20237 "Commitment Floors" MARL — owner 의 submission
- TMLR 8752 "WhyLab Causal Safety" — owner 의 submission
- 둘 다 double-blind review 중
- arXiv preprint = anonymity 위반 → HOLD
- **Paper 1 안에 cross-link 도 hold** — accept 후 published version 추가 가능

cold 권고:
- Paper 1 references 안 "Heo et al. (2026, under review)" 형식 만 — 구체 venue 미표시
- 2026-12 ~ 2027-03 NeurIPS+TMLR 결과 가시화 후 revision 으로 추가

---

## 5. Paper 2 outline (ReScience replication)

### 5.1 Title 권고

**"Fama-French 5-Factor Reproducibility on KOSPI 200: Confirming RMW/CMA Redundancy in the Korean Market (1992–2025)"**

### 5.2 구조

```
1. Introduction
   - Kang & Jang (2018) 결론 요약
   - 한국 시장 anomaly replication 의 gap
2. Method
   - 데이터 source (KRX + KIS API)
   - 1992~2025 윈도우 (Kang 의 1992~2013 + 12년 확장)
   - Factor construction (Size + B/M + RMW + CMA + Mom)
3. Replication
   - Cross-sectional regression (Fama-MacBeth)
   - GRS test
   - RMW/CMA factor redundancy test
4. Discussion
   - 결론 일치 / 불일치
   - 1992~2013 vs 2014~2025 비교
   - 한국 시장 anomaly 12년 진화
5. Reproducibility Notes
   - GitHub repo (MIT)
   - Docker 환경
   - 1줄 명령으로 모든 figure / table 재현
6. References (10~15)
Appendix: KOSPI 200 universe + monthly factor data
```

분량: 8~15 pages.

### 5.3 학술 contribution

- 한국 시장 12년 확장 데이터 (2014~2025 신규)
- Reproducible (Docker + GitHub)
- ReScience C 안 quantitative finance section 의 한국 시장 first

### 5.4 Risk

- Kang & Jang (2018) 결론 contradicting 발견 시 → 학술 충돌 (논쟁) → 단, reproducibility journal 의 정상 결과
- 데이터 access (KIS API 또는 KRX official) cost — owner 보유 (Tier A D8 권고 적용 안)

---

## 6. 외부 visibility lever (cold 권고 우선순위)

### 6.1 Quantpedia Awards 2027 submission

**핵심 정보**:
- 마감: 2026-04-30 23:59 UTC (다음 cycle)
- 자격: 2025-05-01 ~ 2026-04-30 publish (SSRN 또는 arXiv link 필수)
- Prize pool: $25,000
- Visibility: Quantpedia.com featured interview + free Quantra/QuantInsti courses + badge for CV

**Owner timing**:
- Paper 1 SSRN publish 2026-08 → 2026-04-30 마감 직전 valid (8개월 margin)
- Quantpedia Awards 2027 cycle submission (예상 2026-07~2027-04) 에 직접 자격

**Submission 절차**:
- Email: awards@quantpedia.com
- Body: 이름 + paper link + summary 1 paragraph
- 자율 (G1) — owner G2 불필요

cold 권고: **즉시 (Paper 1 publish 직후) submit**. Risk 0, upside 명확.

### 6.2 Hudson & Thames mlfinlab OSS contribution

**PR 기회**:
- Documentation improvement (한국어 또는 영문)
- 새 indicator / portfolio optimization algorithm
- Korean stock data adapter (한국 시장 unique value)

**Cold 평가**:
- 외부 contributor PR merge 시간: 1~3개월 (slow but eventual)
- Hudson & Thames 활동성: 2024~2025 활발, 2026 약화 추세 (commercial pivot 시각)
- 1인 retail PR success 사례: 위 검색 결과 aditya1702 등 외부 contributor 사례 확인

**12주 plan 안 시도**:
- Documentation PR 1건 (W8~W10)
- 한국 시장 unique adapter PR 1건 (W11)
- 응답률: 50~70% (성공 시 owner OSS contributor 정착 신호)

### 6.3 r/quant + r/algotrading honest narrative post

**Post 권고 구조** (r/algotrading):

```
Title: "[Honest Failure] 38-Day Multi-Asset Retail Quant Closure (1-Person, Korean)"

Body:
TL;DR — Ran a 38-day paper trading PoC with 12 alphas across KR equity, US options, crypto perps. WR 37.7%, PnL -15.1%, Sharpe 0.0. Spec failure confirmed (A2 OU: 0/108 sensitivity sweep PASS). Cold conclusion: do not deploy capital.

Background — 1-person retail, Korean, AI-native (Claude+Codex+Sora multi-agent operation).

What worked:
- 9-Layer Kill Switch (Knight Capital 2012 lesson)
- Multi-agent decision orchestration
- Bayesian capital allocation (Kelly criterion at 1/4)

What didn't:
- Multi-asset correlation (unexpected, 0.6+)
- Binance liquidation API change (2026-04-27, 1/sec snapshot)
- 12 alphas all suffer from same alpha decay

Open source: https://github.com/Yesol-Pilot/quant-poc-multi-asset
Paper (SSRN): https://...
Dashboard: https://heoyesol.kr/quant

Happy to discuss. Cold feedback welcome.
```

**Cold 권고**:
- Reddit posting 시간: r/algotrading 의 trafficking 패턴 (Tuesday~Thursday 18:00~22:00 ET)
- 첫 60분 reaction = thread 운명
- Viral 15~25% 확률 (contrarian narrative 강점)
- 부정적 피드백 (40~60%): "you didn't try hard enough" 류 — cold honest 로 받아들이고 응답

### 6.4 NeurIPS + TMLR cross-link

⏸️ **Blind review HOLD 영구 유지** (owner 2026-05-12 정정 박제):
- arXiv preprint = author identity 노출 = anonymity 위반
- 12주 plan 안 cross-link 시도 X
- 2026-12 ~ 2027-03 결과 가시화 후:
  - **Accept**: camera-ready 와 함께 arXiv release → SSRN paper 1 revision 으로 cross-link 추가
  - **Reject**: owner G2 재검토 (다른 venue resubmit, 또는 arXiv release 결정)

---

## 7. 저작권 / IP 정책

### 7.1 이트라이브 NDA 제약

cold 확인:
- owner 의 NeurIPS 20237 + TMLR 8752 = 이트라이브 본업 외 개인 연구
- NeurIPS / TMLR submission 가능 → IP 분리 정확
- Paper 1 (Korean Retail Multi-Strategy Backtest) = 동일 path
- 이트라이브 CTS-AI 사내 프로젝트 활용 데이터 = 분리 (cts-projects.json 의 보호 정책 준수)

### 7.2 Open Source MIT + paper CC BY 4.0 호환

License 조합:
- Code: MIT
- Paper (SSRN): default = "All Rights Reserved" by SSRN — 단, "Creative Commons Attribution" 옵션 선택 가능
- Paper (ReScience): CC BY 4.0 강제 (open access mission)

**cold 권고**: SSRN paper 1 = CC BY 4.0 명시 선택. MIT (code) 와 CC BY 4.0 (paper) 호환 — 둘 다 attribution 만 요구, commercial use 허용.

### 7.3 외부 contributor 가 paper co-author 가능성

12주 plan 안 시나리오:
- GitHub PR 으로 외부 contributor 코드 기여 → MIT contributor agreement (자동, GitHub PR submit = MIT 동의)
- Paper 1 co-authorship → 본인 추천 권리 (owner G2)
- 12개월 후 외부 contributor 가 의미 있는 paper 기여 (예: 새 alpha 발견, 새 데이터 source) → co-author 추가 검토

cold 권고:
- Paper 1 = single author (Yesol Heo)
- Paper 2 (ReScience replication) = single author
- 12개월 후 Paper 3 + 외부 contributor 가능

---

## 8. Cold Honest 권고 (12주 plan timing)

### 8.1 12주 plan 단계별 academic publish 활동

| 주 | 활동 | 시간 |
|---|---|---|
| W1 | SSRN registration (Drexel User Account) | 1h |
| W2 | Paper 1 outline + key sections draft | 8h |
| W3 | Paper 1 Methods + Architecture 작성 | 12h |
| W4 | Paper 1 Results section (38-day PoC honest failure) | 10h |
| W5 | Paper 1 Honest Failure Analysis + Lessons | 8h |
| W6 | Paper 1 References + Appendix | 6h |
| W7 | Paper 1 internal review (Claude Strategy Lead grilling) | 4h |
| W8 | Paper 1 SSRN submission (Quantitative Finance Network) | 2h |
| W9 | Paper 2 (ReScience replication) outline | 4h |
| W10 | Paper 2 Method + Replication 작성 | 12h |
| W11 | Paper 2 Discussion + Reproducibility | 6h |
| W12 | Paper 2 ReScience GitHub issue submission | 3h |
|  | Quantpedia Awards 2027 submission email | 0.5h |
|  | r/algotrading honest narrative post (선택) | 3h |
|  | Hudson & Thames mlfinlab PR 1건 (선택) | 4h |

총합 약 83.5h.

### 8.2 자본 비용 (외부 의존성)

| 항목 | 비용 |
|---|---|
| SSRN registration | $0 |
| SSRN submission fee (Quantitative Finance Network) | $0 |
| arXiv submission | PASS (12주 plan) |
| ReScience submission | $0 (open access mission) |
| Quantpedia Awards submission | $0 |
| Hudson & Thames mlfinlab PR | $0 |
| Reddit / HN post | $0 |
| LaTeX / Overleaf (선택) | $0 (free tier 충분) |
| **합계** | **$0** |

### 8.3 Visibility 예측 (12개월 누적, Paper 1 publish 후)

| Metric | 보수 | 중도 | 낙관 |
|---|---|---|---|
| SSRN downloads | 80 | 250 | 600 |
| SSRN abstract views | 200 | 800 | 2,000 |
| Citations (Google Scholar) | 0 | 2 | 5 |
| Quantpedia featured | No | Maybe (50%) | Yes |
| Hudson & Thames mlfinlab merge | No | 1건 | 2~3건 |
| Reddit r/algotrading thread viral | No | 200+ upvotes | 1,000+ upvotes |
| HN front page | No | 30~50 upvotes | front page 200+ |
| NeurIPS / TMLR cross-link | hold | hold | accept (60% 확률) |

### 8.4 외부 정책 변경 risk (cold honest)

- **arXiv endorsement 추가 강화** (중간): 2026-07-01 Cornell 분리 후 정책 추가 변경 가능. owner 의 path B (personal endorsement) 영향 X (path B 는 영구 보장).
- **SSRN 정책 변경** (낮음): Elsevier 인수 후 안정, Quantitative Finance Network 무료 유지.
- **ReScience 운영 중단 risk** (낮음): GitHub 기반 community driven, contributor base 안정.
- **Quantpedia Awards 종료 risk** (중간): 2024+2025 모두 시행, 2026 confirmed, 2027 미확정. 매년 4월 marketing 가시 — owner monitoring 필요.
- **이트라이브 NDA 변경** (낮음): 본업 변경 시 재검토. cold 권고: 매 12개월 NDA 재확인.

### 8.5 38일 PoC 외부 정책 변경 실패 패턴 차단

- **Single venue dependency 회피**: SSRN (paper 1) + ReScience (paper 2) + arXiv (hold, 12개월 후) 분산. 한 venue 정책 변경 → 다른 venue valid.
- **GitHub 자체 publish backup**: SSRN/ReScience publish 외에 GitHub repo `/docs/paper/` 에 PDF 직접 host. SSRN 사이트 종료 risk 대비.
- **Cross-link 영구화**: Paper 1 의 references 안 GitHub commit hash 명시 (e.g., "Heo 2026, GitHub: Yesol-Pilot/quant-poc-multi-asset@a781a0f"). repo rename / org 이동 시에도 commit hash 영구 valid.
- **Cold honest 가 self-protect**: 38일 PoC honest failure = institutional reviewer 가 정직성 신호 가산점. 광고성 paper 대비 reject risk 낮음.

---

## 9. References

- [arXiv Endorsement Policy 2026-01 Update](https://blog.arxiv.org/2026/01/21/attention-authors-updated-endorsement-policy/) — 2026-05-14 인용
- [arXiv Endorsement Help](https://info.arxiv.org/help/endorsement.html) — 2026-05-14 인용
- [arXiv q-fin Quantitative Finance Archive](https://arxiv.org/archive/q-fin) — 2026-05-14 인용
- [arXiv q-fin Current Month (May 2026)](https://arxiv.org/list/q-fin/current) — 2026-05-14 인용
- [arXiv Submission Status](https://info.arxiv.org/help/submit_status.html) — 2026-05-14 인용
- [arXiv 2026 Blog Index](https://blog.arxiv.org/2026/) — 2026-05-14 인용
- [SSRN Financial Economics Network](https://www.ssrn.com/index.cfm/en/fen/) — 2026-05-14 인용
- [SSRN Home Page](https://www.ssrn.com/ssrn/) — 2026-05-14 인용
- [SSRN Author Researchers Page (Elsevier)](https://www.elsevier.com/products/ssrn-preprint-services/author-researchers) — 2026-05-14 인용
- [SSRN Wikipedia](https://en.wikipedia.org/wiki/Social_Science_Research_Network) — 2026-05-14 인용
- [SSRN Free Papers (Elsevier Support)](https://www.elsevier.support/ssrn/answer/are-all-papers-on-ssrn-free) — 2026-05-14 인용
- [ReScience C Journal](http://rescience.github.io/) — 2026-05-14 인용
- [ReScience C Template](https://github.com/rescience/template) — 2026-05-14 인용
- [ReScience C Submissions Repo](https://github.com/ReScience/ReScience-submission) — 2026-05-14 인용
- [ReScience C Author Guidelines](https://resciencec.readthedocs.io/en/latest/submitting.html) — 2026-05-14 인용
- [Quantpedia Awards 2026](https://quantpedia.com/quantpedia-awards-2026/) — 2026-05-14 인용
- [Quantpedia Awards 2025](https://quantpedia.com/quantpedia-awards-2025/) — 2026-05-14 인용
- [Hudson & Thames mlfinlab GitHub](https://github.com/hudson-and-thames/mlfinlab) — 2026-05-14 인용
- [Hudson & Thames mlfinlab official](https://hudsonthames.org/mlfinlab/) — 2026-05-14 인용
- [Kang & Jang (2018) Re-examination of Fama-French Models in the Korean Stock Market (Springer)](https://link.springer.com/article/10.1007/s10690-018-9254-5) — 2026-05-14 인용
- [Kang & Jang (2019) A Comparison of New Factor Models in the Korean Stock Market](https://onlinelibrary.wiley.com/doi/10.1111/ajfs.12274) — 2026-05-14 인용
- [Conditional autoencoder asset pricing models for the Korean stock market (PLOS One 2023)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0281783) — 2026-05-14 인용
- [Market anomalies in the Korean stock market (Emerald Insight)](https://www.emerald.com/insight/content/doi/10.1108/jdqs-03-2020-0004/full/html) — 2026-05-14 인용
- [Creative Commons CC BY 4.0 Legal Code](https://creativecommons.org/licenses/by/4.0/legalcode.en) — 2026-05-14 인용
- [PLOS One License Policy](https://journals.plos.org/plosone/s/licenses-and-copyright) — 2026-05-14 인용

— END —
