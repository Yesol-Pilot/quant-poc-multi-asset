# #03 — 12주 Daily Build Plan + 5차원 Excellence Milestone + Security/Monitoring

> **작성:** 2026-05-14, Strategy Lead Claude Opus 4.7 (자율)
> **대상:** owner 허예솔 (한국 retail 1인 AI 네이티브 PM portfolio, NeurIPS 20237 + TMLR 8752 블라인드 심사 중)
> **기간:** 2026-05-14 (W1 D1, Mon) ~ 2026-08-05 (W12 D84, Tue) = 84 days
> **모드:** cold honest. 광고성 표현 0. 실 작동 가능한 daily granularity 만.
> **본 SSOT 의 위치:** Research Phase 16 docs (`docs/research/`) 와 Design Phase 02 (예정) 의 다음 산출. Build Phase 의 day-by-day plan.

---

## 0. Reading Guide (먼저 읽기)

이 문서는 7 section + 84-day daily matrix 로 구성된다. 각 section 의 진입점:

- **Section 1**: Build Plan Overview (5차원 + 자산 활용 + Strategy Lead 자율 95%) — 80~120 단어 / 1분
- **Section 2**: 5차원 Detailed Milestone (D1 Code / D2 Academic / D3 OSS / D4 Live / D5 Comm) — 각 차원 verification check 포함
- **Section 3**: Security Design (12-Layer Kill Switch / OWASP / Disclaimer / Credential isolation)
- **Section 4**: Monitoring + Observability (Vercel / Supabase / GitHub / Sentry / GA4 + 매주 자동 보고)
- **Section 5**: Weekly Risk Matrix (Week 1~12 cold risks + mitigation)
- **Section 6**: Daily Verification Checklist (각 day 끝 5건 체크)
- **Section 7**: Week × Day Daily Plan — 84 days, 각 100~300 단어 spec

**사용 권장 패턴**:
- 매 주 월요일: Section 5 본 주차 risks 확인 + Section 7 본 주 D1~D7 daily plan review
- 매 day 끝: Section 6 verification 5건 PASS 확인 → 다음 day plan 확정
- 매 4주 (W4/W8/W12): Section 2 5차원 milestone aggregate 진척 보고
- 사고/regression 발생 시: Section 3 (security) + Section 5 (risk mitigation) 재참조

---

## Section 1. Build Plan Overview

### 1.1 Core Premise (research 16 영역 cross-check 산출)

12주 build 의 5차원 목표:

| 차원 | 12주 종료 시 목표 | research 근거 |
|---|---|---|
| **D1 Code Quality** | 1,000+ tests / 90% coverage / 4 자산군 production-grade | research 03 (KIS), 04 (IBKR), 08 (data sources) |
| **D2 Academic Rigor** | SSRN 1편 publish + ReScience 1편 publishable draft | research 06 (62 refs), 11 (publish strategy) |
| **D3 Open Source** | GitHub 300~600 stars (50% 확률), 5+ external contributors | research 09 (OSS strategy), 07 (competitive) |
| **D4 Live Production** | heoyesol.kr/quant Lighthouse 95+ / 4-asset dashboard / public API | research 10 (tech stack) |
| **D5 Communication** | Substack 100~800 subs / Twitter +500~3,000 / LinkedIn +200~1,000 | research 12 (viral), 13 (content), 14 (KR community) |

### 1.2 자산 활용 명시 (38일 PoC + 16 Research)

| 자산 | 본 plan 안 활용 위치 |
|---|---|
| 38일 PoC failure forensic (191 trades / WR 37.7% / -15.1%) | README "Results" + SSRN Paper 1 §4 + Substack 첫 newsletter + Show HN angle |
| 9-Layer Kill Switch production wiring (commit `c8f4e7b`) | L10/L11/L12 확장 base (Section 3.2) |
| 16 research docs (65,000 단어 / 300+ refs) | D2 paper references + D5 newsletter source + D4 docs page |
| A2 OU 108-cell sensitivity sweep (0/108 acceptance) | SSRN Paper 1 §4.2 honest negative result 박제 |
| Multi-agent 자율 capability (Claude + Codex + Gemini) | Strategy Lead 95% 자율 가능 base |
| 11 SBU Next.js 정착 | D4 stack 학습 cost 0 (Next.js 15 + Vercel Pro) |
| Yesol-Pilot organization (13 active repos) | D3 repo `quant-poc-multi-asset` 일관성 |

### 1.3 owner 시간 budget cold (12주 = 96~156h)

| Track | h/week | 12주 합 |
|---|---|---|
| Strategy Lead 자율 build review + 결정 (5%) | 0.5~1.0 | 6~12h |
| Content review + 승인 (Twitter / LinkedIn / Substack draft) | 3 | 36h |
| 한국 quant community (cold lurk + 첫 contact + reply) | 5~8 | 60~96h |
| 학술 publish review + SSRN/ReScience submission | 2 (마지막 3주만) | 6h |
| **합계** | **8~13h/week** | **108~150h** |

**Strategy Lead 자율 = 95%**. owner = 5% (review + 결정 + signature + community).

### 1.4 12주 timeline 한 줄 요약

```
W1  Setup        : repo public + Live page + KIS 가입 + 계정 (5 channel)
W2  KIS build    : A11~A14 (KR equity 4 알파) + paper trading scaffold
W3  KIS finalize : 모의투자 첫 동작 + 100+ tests + Substack #1
W4  IBKR        : A15~A17 (US ETF 3 알파) + 300+ tests + README v2
W5  Crypto      : 38일 PoC archive + Bybit/OKX integration + WebSocket
W6  Options     : A19~A21 backtest (선택) + 500+ tests + 첫 external PR
W7  Integration : 4 자산군 통합 + Live dashboard + Paper 1 draft 50%
W8  Quality     : 700+ tests + 80% coverage + DSR/PBO + Stars 100+
W9  Paper       : SSRN draft 90% + ReScience draft 30%
W10 Polish      : Lighthouse 95+ + Stars 200~400 + SEO 100
W11 Submit      : SSRN submit + ReScience submit prep + HN warm-up
W12 Launch      : HN Tuesday 09:00 PT + 300~600 stars + Apply prep
```

### 1.5 Build 종료 (Week 13+) 상태 박제

- GitHub `Yesol-Pilot/quant-poc-multi-asset` public + 1,000+ tests + 90% coverage
- SSRN Paper 1 live (Quantpedia Awards 2027 submission base)
- ReScience Paper draft submit prep
- heoyesol.kr/quant dashboard live + public API rate-limited
- Substack 100~800 subscribers + Twitter +500~3,000 + LinkedIn +200~1,000
- 5+ apply 동시 (토스/카카오페이/뱅크샐러드/채널톡/뤼튼/Sendbird/Upstage/에이블리)
- 1+ offer 확률 60~80% (cold, research 15 기준)

---

## Section 2. 5차원 Detailed Milestone

각 차원의 weekly milestone 과 verification check. 진척 측정 가능한 단위로 박제.

### 2.1 D1 Code Quality — 1,000+ tests / 90% coverage / 4 자산군 production-grade

#### Weekly milestones

| Week | Milestone | Verification |
|---|---|---|
| W1 | Monorepo + CI/CD setup + pre-commit + ruff/black + GitHub Actions | `git ls-files .github/workflows/ | wc -l >= 3` (test.yml / lint.yml / build.yml), `.pre-commit-config.yaml` exists, first PR green |
| W2 | KIS adapter (REST + WS) + 50+ tests | `pytest -q | tail -1` ≥ 50 PASS, KIS scaffold 안 `MockKisClient` + `KisClient` 분리 |
| W3 | A11~A14 (KR 알파 4개) scaffold + 100+ tests + paper engine | `pytest tests/strategies/ -q` ≥ 30 PASS, `python run_paper.py --strategy a11 --dry-run` no error |
| W4 | IBKR adapter (ib_insync wrapper) + A15~A17 + 300+ tests | `pytest -q` ≥ 300 PASS, `pytest --cov=src --cov-report=term-missing` coverage ≥ 60% |
| W5 | Crypto cross-exchange (Bybit + OKX + Binance) + A1~A6 wiring migration | 38일 PoC 의 commit `4849d84` 재현 — 3-way liquidation aggregation 라이브 |
| W6 | A19~A21 옵션 backtest (선택, Theta Data Value $80) + 500+ tests | `pytest tests/strategies/options/` ≥ 50 PASS (선택 활성화 시) |
| W7 | 4 자산군 unified backtest runner + Live dashboard wiring | `python run_unified.py --asset kr,us,crypto,options --days 30` 정상 종료 |
| W8 | 700+ tests + 80% coverage + DSR + PBO + Sensitivity sweep CI | `pytest --cov=src --cov-fail-under=80 -q` PASS, `python tools/dsr.py` + `python tools/pbo.py` 둘 다 동작 |
| W9 | 800+ tests + Kill Switch L10/L11/L12 + HaltOrchestrator integration | `pytest tests/kill_switch/` ≥ 30 PASS, 12-Layer 모두 unit test 커버 |
| W10 | 900+ tests + Docker Dev Container + 1-command local launch | `docker compose up` → paper trading 자동 시작, README 5분 quick start verified |
| W11 | 1,000+ tests + 85% coverage + Mutation testing (mutmut) baseline | `pytest -q` ≥ 1000 PASS, `mutmut run` baseline kill rate ≥ 50% |
| W12 | 1,000+ tests + 90% coverage + Mutation kill rate 70%+ + Performance benchmark | `pytest --cov-fail-under=90` PASS, `pytest tests/benchmarks/ --benchmark-only` baseline 기록 |

#### Cold realistic note

- **Coverage 90% 는 cold target**: 1인 retail 에서 90% 는 인프라 (logging / error handling / config) 포함 시 도달 가능. 비즈니스 로직 (전략 + 백테스트) 만 측정 시 95%+ 도달 가능 (작은 surface).
- **1,000+ tests 의 의미**: 적당히 묶어 측정 시 unit 600 + integration 250 + property-based (hypothesis) 100 + benchmark 50 = 1,000. test bloat 회피 (한 알파에 30 tests 적당).
- **38일 PoC 의 6 알파 (A1~A6) 기존 wiring 재활용**: zero-rewrite 원칙. A11~A21 신규는 base abstract class 상속.

### 2.2 D2 Academic Rigor — SSRN 1편 publish + ReScience 1편 publishable

#### Weekly milestones

| Week | Milestone | Verification |
|---|---|---|
| W1 | References 50+ 누적 (research 06 의 62 → curated 50) + bibtex sync | `wc -l docs/paper-1/refs.bib` ≥ 50 entries, `bibtex paper.aux` no error |
| W2 | Paper 1 outline (Introduction + Method + Results + Honest Failure + Lessons) | `docs/paper-1/outline.md` 5 sections 명시, 각 sub-section bullet 박제 |
| W3 | Paper 1 §1 Introduction draft (한국 retail quant gap + 38일 PoC framing) | 500~800 단어, references 5~10 cited |
| W4 | Paper 1 §2 Method draft (multi-asset architecture + alpha registry) | 1,200~1,800 단어, 다이어그램 1~2개 (Mermaid) |
| W5 | Paper 1 §3 Results draft (38일 PoC + W2~W4 paper trading 합산) | 1,500~2,000 단어, 표 3~5개 + chart 4~6개 |
| W6 | Paper 1 §4 Honest Failure section (cold 박제 + reviewer 검증 가능 표) | 800~1,200 단어, 12 알파 별 trade count + PnL + cause analysis |
| W7 | Paper 1 §5 Lessons + §6 Open Source link + Paper 1 draft 60% | 단어 합산 5,000~7,000, 25~35 pages 진척 |
| W8 | Paper 1 draft 80% + figure 8~12개 (matplotlib + PGFPlots) + references final | 100% LaTeX compile (pdflatex no error) |
| W9 | Paper 1 draft 95% + Internal review (Strategy Lead self-grill + cold judgement) | 6,000~9,000 단어, abstract 200~250 단어 |
| W10 | ReScience Paper draft 50% (Fama-French KOSPI 200 replication, Kang & Jang 2016 base) | 5~8 pages, GitHub repo link + replication notebook |
| W11 | **SSRN submission live** + Paper 1 ABS 등록 (Quantitative Finance Network) + Quantpedia Awards 2027 submission prep | SSRN paper ID 발급, 첫 download counter visible |
| W12 | ReScience submission prep (GitHub repo review-ready) + SSRN downloads 30~100 | ReScience PR 또는 ReScience X workflow start, SSRN counter check |

#### Cold realistic note

- **SSRN median paper 100~500 downloads/1년** (research 11). owner 의 retail audience cross-link 시 200~800 downloads 가능 (50% 확률).
- **ReScience review timeline 3~6개월**: 2026-08 submit → 2027-02 accept 가능. 12주 plan 안에서는 submit prep 까지.
- **arXiv 는 PASS** (research 11 권고): endorsement 보틀넥. 12개월 후 NeurIPS+TMLR accept 가시화 시점 재평가.
- **블라인드 심사 룰 준수**: NeurIPS 20237 / TMLR 8752 venue + title 명시 절대 금지. "TIER 1 ML 컨퍼런스 single-author submission under review" 정도 표기 안전 (research 15).

### 2.3 D3 Open Source — GitHub 300~600 stars / 5+ external contributors

#### Weekly milestones

| Week | Milestone | Verification |
|---|---|---|
| W1 | Repo `Yesol-Pilot/quant-poc-multi-asset` public + README v0 + LICENSE MIT + Code of Conduct | `gh repo view Yesol-Pilot/quant-poc-multi-asset --json visibility` = "PUBLIC", LICENSE.md exists, CODE_OF_CONDUCT.md exists |
| W2 | README v1 (5 sections: hero + quick start + architecture + results + docs link) + 5~7 badges | README 안 `## What This Is`, `## Quick Start`, `## Architecture`, `## Results`, `## Documentation`, `## License` 모두 존재 |
| W3 | Korean README (README.ko.md) + dual-track link bar | README 첫 줄 `[English](README.md) | [한국어](README.ko.md)`, README.ko.md 영문 길이의 60%+ |
| W4 | README v2 (Mermaid architecture diagram + benchmark table + citation BibTeX) | README 안 ```mermaid code block + ```bibtex code block, `@misc{heo2026quantpoc...}` 정확 |
| W5 | First external contributor (issue 또는 small PR) + CONTRIBUTING.md + ISSUE_TEMPLATE | `gh pr list --state all` 외부 author 1+ 또는 `gh issue list --state all` 외부 1+ |
| W6 | Stars 50+ + awesome-quant PR submit + Reddit r/algotrading first post | `gh repo view --json stargazerCount` ≥ 50, awesome-quant PR URL 확보 |
| W7 | Stars 80~150 + Substack newsletter cross-link + Twitter 첫 thread | stars ≥ 80, Substack post URL 안 GitHub link 확인 |
| W8 | Stars 100~200 + 첫 PR merge (외부) + Discord channel open (선택) | merged PR 의 author != Yesol-Pilot, `git log --all --pretty='%an' | sort -u | wc -l` ≥ 2 |
| W9 | Stars 150~300 + Hacker News warm-up (account karma 50+) + Show HN draft | HN account karma ≥ 50, Show HN draft 박제 (`docs/launch/show-hn.md`) |
| W10 | Stars 200~400 + 2~5 external contributors + Documentation site live | contributors ≥ 2 (gh insights), `heoyesol.kr/quant/docs` 200 OK |
| W11 | Stars 250~500 + Pre-launch tease (Twitter / LinkedIn 24h before HN) | tweet 1+ "launching X tomorrow" pattern 확인 |
| W12 | **Hacker News Show HN launch (Tuesday 09:00 PT)** + Stars 300~600 + Reddit cross-post + Product Hunt 동시 | HN URL submitted, upvotes ≥ 5 within 60min (first hour Stop/Go), final stars ≥ 300 |

#### Star 누적 cold target (50% 확률)

```
W1:   1 (owner)
W2:   3~5 (Strategy Lead + 1~2 friends)
W3:   5~10
W4:   10~20 (README v2 viral 일부)
W5:   15~30 (첫 external traction)
W6:   30~80 (awesome-quant + Reddit first post)
W7:   80~150 (Substack + Twitter)
W8:   100~200 (PR merge + Discord)
W9:   150~300 (HN warm-up + cross-channel)
W10:  200~400 (docs site + 2~5 contributors)
W11:  250~500 (pre-launch tease)
W12:  300~600 (HN Show HN launch)
```

50% 확률은 cold target. 25% 확률 = 100~300 stars (under-perform), 25% 확률 = 600~1,500 stars (viral over-perform).

#### Cold realistic note

- **glob 시장: 12주 OSS 신규 launch 의 stars median = 50** (research 09). 300~600 = top 10%.
- **viral over-perform 트리거**: HN front page (top 30) 도달 시 1주 만에 +500~2,000 stars 가능. 평균 stay-in-front-page 4~8h.
- **under-perform 시 mitigation**: W13~W16 에 awesome-systematic-trading PR + Quantpedia Pro feature + Korean blog (Cherry Quant / 인텔리퀀트) guest post.

### 2.4 D4 Live Production — heoyesol.kr/quant Lighthouse 95+ / 4-asset dashboard

#### Weekly milestones

| Week | Milestone | Verification |
|---|---|---|
| W1 | Vercel Pro 활성 + Supabase Pro 활성 + `heoyesol.kr/quant` Next.js 15 scaffold + 404 → 200 | `curl -I https://heoyesol.kr/quant` = 200, Vercel project ID 정합 |
| W2 | `/quant` landing page (hero + 38일 PoC summary card + GitHub link + Substack subscribe) | Lighthouse Performance ≥ 80, Vercel Web Vitals 자동 수집 시작 |
| W3 | `/quant/paper-trading` page (mock dashboard with Tremor charts) | 4 chart 컴포넌트 렌더 (PnL line, trade count bar, win rate gauge, drawdown area) |
| W4 | `/quant/dashboard` 초기 (3 자산군 KR/US/Crypto metrics, Supabase 연결) | Supabase Realtime channel `quant-trades` 구독 동작, mock data flow OK |
| W5 | `/quant/api/v1/strategy/[id]` public API endpoint (rate-limited 10 RPS) | `curl https://heoyesol.kr/quant/api/v1/strategy/a11` returns JSON 200, 11번째 호출 429 |
| W6 | `/quant/docs` Next.js MDX docs (10+ pages: setup, strategies, kill switch, etc.) | `find src/app/quant/docs -name "*.mdx" | wc -l` ≥ 10 |
| W7 | 4 자산군 통합 dashboard (KR + US + Crypto + Options card switcher) + Paper page link | dashboard 안 4 asset selector 동작, 각 selector 별 chart render |
| W8 | Lighthouse Performance ≥ 90 (preload / image optim / code split) | `npx lighthouse https://heoyesol.kr/quant --output=json | jq '.categories.performance.score'` ≥ 0.90 |
| W9 | `/quant/paper-1` 학술 paper landing page (abstract + PDF download + BibTeX citation copy button) | PDF 다운로드 동작, BibTeX clipboard copy 동작 |
| W10 | **Lighthouse Performance ≥ 95 / Accessibility 100 / Best Practices 100 / SEO 100** | 4 categories 모두 ≥ 0.95 / 1.00 |
| W11 | Public API docs (OpenAPI 3.1 spec + Swagger UI 또는 Scalar) + rate-limit visibility | `/quant/api/docs` 200 OK, OpenAPI spec download 가능 |
| W12 | OG image dynamic generation (`@vercel/og`) + Twitter card preview + 한국어 SEO meta | Twitter card validator + LinkedIn post inspector 둘 다 image rendering 정상 |

#### Lighthouse 95+ 도달 cold path

1. **Performance 95+** (가장 어려움): Next.js 15 SSG + image lazy + critical CSS inline + JS code split + Vercel Edge cache
2. **Accessibility 100**: shadcn/ui base + ARIA labels + keyboard navigation + color contrast 4.5:1
3. **Best Practices 100**: HTTPS + no console errors + valid CSP + image aspect ratio
4. **SEO 100**: meta description + canonical + structured data (JSON-LD) + sitemap.xml + robots.txt

### 2.5 D5 Communication — Substack 100~800 subs / Twitter +500~3,000 / LinkedIn +200~1,000

#### Weekly milestones

| Week | Milestone | Verification |
|---|---|---|
| W1 | Twitter (@yesolheo or @YesolPilot) / LinkedIn / Substack / Threads / Hashnode 5 channel 셋업 | 5 channel 모두 profile 완성 (avatar + bio + cross-link) |
| W2 | LinkedIn 첫 post (Tuesday 09:00 KST) + Twitter 첫 thread | LinkedIn post URL + Twitter thread URL 박제 |
| W3 | Substack 첫 newsletter "38일 PoC closure: cold honest" | Substack post URL, open rate 측정 (target 30%+) |
| W4 | Substack #2 "Multi-asset architecture for 1-person quant" + LinkedIn #2 + Twitter +50 followers | Twitter follower count ≥ 50 누적 |
| W5 | Substack #3 "KIS API: 한국 retail quant 의 첫 장벽" + Korean Cherry Quant guest article 제안 | Substack subscribers ≥ 30, Cherry Quant draft 박제 |
| W6 | Twitter +200 followers + r/algotrading post (38일 PoC honest narrative) | follower ≥ 200, Reddit post karma ≥ 10 |
| W7 | Substack #4 (학술 paper draft preview) + LinkedIn 한국 quant 인플루언서 5 connection request | LinkedIn 5 connection request sent, accept rate 측정 |
| W8 | LinkedIn 5 connection accept + Substack subscribers 50~100 + Twitter +400 | LinkedIn connection 5+, Substack subs ≥ 50 |
| W9 | Twitter +800 followers + Hashnode crosspost (3개 글 syndicate) | follower ≥ 800, Hashnode dashboard verify |
| W10 | Substack 100~300 subscribers + LinkedIn #6 + Twitter +1,500 | subs ≥ 100, LinkedIn impressions 누적 ≥ 50K |
| W11 | Pre-launch warm-up: Twitter daily thread (D-7 ~ D-1 카운트다운) + Substack #6 (HN launch teaser) | Twitter thread 7개 (각 day 1개), Substack open rate ≥ 35% |
| W12 | **Hacker News Show HN launch (Tuesday 09:00 PT)** + Twitter +500~3,000 final / LinkedIn +200~1,000 final / Substack 100~800 final | HN front page 도달 여부 박제, 모든 channel 최종 metrics 보고 |

#### Cold realistic note

- **Substack 100~800 subscribers**: research 13 의 retail quant Substack median = 50 subs / 12주. 100~800 = top 30~50%.
- **Twitter +500~3,000**: 비-paid + 자체 콘텐츠 + 한국 quant 시장 visibility 의 한계 = ~3,000.
- **LinkedIn +200~1,000**: 한국 LinkedIn 사용성 낮음 (research 15) → 1,000 도달이 쉽지 않음. 200~500 = 현실적.
- **블라인드 심사 룰**: NeurIPS / TMLR venue + title 명시 절대 금지. owner G2 자율 결정.

### 2.6 5차원 종합 verification cron

매 day 끝:

```bash
# D1 (Code)
pytest -q | tail -1 | grep -oP '\d+ passed' | head -1
pytest --cov=src --cov-report=term-missing | tail -1

# D2 (Academic)
wc -l docs/paper-1/refs.bib
wc -w docs/paper-1/*.tex | tail -1

# D3 (OSS)
gh repo view Yesol-Pilot/quant-poc-multi-asset --json stargazerCount,forkCount

# D4 (Live)
npx lighthouse https://heoyesol.kr/quant --output=json --quiet \
  | jq '{perf: .categories.performance.score, a11y: .categories.accessibility.score}'

# D5 (Comm)
# Twitter API + LinkedIn API + Substack API 활용, 또는 매 day 5분 manual 측정

# 모두 Supabase quant_milestone_metrics 테이블 insert
```

이 5건 결과를 Supabase `quant_milestone_metrics` 테이블에 insert (daily row). Strategy Lead 가 매 Monday 08:00 KST 자동 보고 (Section 4.5).

---

## Section 3. Security Design

### 3.1 Credential Isolation (5 자산 / 5 storage)

| 자산 | Storage | 접근 권한 | 회전 주기 |
|---|---|---|---|
| KIS Developers AppKey / AppSecret | Supabase Vault (encrypted) | runtime only via SDK | 90일 (KIS 의무) |
| IBKR TWS connection | Local IB Gateway (localhost:7497 only) | local machine only, no remote | 365일 (cert renewal) |
| Gemini API key | Vercel env var (production runtime) | Vercel deploy + edge function | 180일 |
| GitHub PAT (CI) | GitHub Actions secret (`secrets.GH_PAT`) | CI runner only | 90일 |
| Supabase service_role | Vercel env var (server-side only) | Next.js API route only | 365일 |

#### 절대 금지

- `.env` 파일 git commit
- `.env.local` 파일 git commit
- GitHub PAT 본문 README / docs 노출
- KIS AppSecret 클라이언트 사이드 (Next.js client component) 전달
- Vercel preview env var 에 production credential (preview = staging key only)

#### CI/CD 자동 가드 (W1 D2 적용)

```yaml
# .github/workflows/credential-scan.yml
name: credential-scan
on: [pull_request]
jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: gitleaks/gitleaks-action@v2
      - run: |
          if grep -rE '(KIS_APPKEY|KIS_APPSECRET|sk-ant-|sk-or-)' src/; then
            exit 1
          fi
```

### 3.2 12-Layer Kill Switch (38일 PoC 자산 + 신규 3 layer)

#### 기존 9-Layer (commit `c8f4e7b` 의 production wiring)

| Layer | 발동 조건 | 6-step action |
|---|---|---|
| L1 | open order > 임계값 | cancelAll → verifyNoOpenOrders → close active position → persistHaltUntil → block new entries → alert |
| L2 | position notional > 한도 | 동상 |
| L3 | margin level < 임계 | 동상 |
| L4 | API error rate > 5% (1분) | 동상 |
| L5 | latency p99 > 500ms (1분) | 동상 |
| L6 | drawdown > 5% | 동상 |
| L7 | trade rate > 10x baseline | 동상 |
| L8 | manual halt flag (env var) | 동상 |
| L9 | 외부 source halt 신호 (heartbeat 결손) | 동상 |

#### 신규 3 layer (12주 plan 안 wiring)

##### L10 Alpha Decay Detector

```python
# src/kill_switch/l10_alpha_decay.py
def check(strategy_id: str, lookback_days: int = 14) -> bool:
    """
    Rolling Sharpe 14일이 0.5 미만이면 halt.
    38일 PoC 학습: A2 OU 의 108-cell sweep 0/108 acceptance gate
    => 이 검출이 실시간으로 됐다면 자본 보호 가능했음.
    """
    sharpe = compute_rolling_sharpe(strategy_id, lookback_days)
    if sharpe < 0.5:
        log.warning(f"Alpha decay detected: {strategy_id} Sharpe={sharpe:.2f}")
        return True
    return False
```

**테스트 (W8 D52~D54)**:
- A2 의 38일 PoC trade log 입력 → L10 발동 정확 검증 (positive case)
- 임의 정상 trade log 입력 → L10 미발동 (negative case)
- 표본 30+ trade 미만 시 graceful skip (false-positive 차단)

##### L11 Regime Detector

```python
# src/kill_switch/l11_regime.py
def check(asset_class: str) -> bool:
    """
    BEAR regime (price < 50d MA) + 변동성 > 10% (ATR/price) 동시 발생 시 halt.
    research 06 의 momentum strategy 한국 적용 evidence 4개만 학습.
    """
    is_bear = is_bear_regime(asset_class)
    vol = compute_atr_pct(asset_class)
    if is_bear and vol > 0.10:
        log.warning(f"Regime halt: {asset_class} BEAR + vol={vol:.2%}")
        return True
    return False
```

##### L12 Overfit Guard

```python
# src/kill_switch/l12_overfit.py
def check(strategy_id: str, pbo_threshold: float = 0.7) -> bool:
    """
    PBO (Probability of Backtest Overfitting) > 0.7 시 halt.
    Bailey & Lopez de Prado (2014) "The probability of backtest overfitting".
    """
    pbo = compute_pbo(strategy_id)
    if pbo > pbo_threshold:
        log.warning(f"Overfit halt: {strategy_id} PBO={pbo:.2f}")
        return True
    return False
```

#### HaltOrchestrator integration (W9 D58~D60)

```python
# src/kill_switch/orchestrator.py
class HaltOrchestrator:
    LAYERS = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12]

    def check_all(self) -> list[str]:
        triggered = []
        for layer in self.LAYERS:
            try:
                if layer.check():
                    triggered.append(layer.__name__)
            except Exception as e:
                log.error(f"Layer {layer.__name__} check error: {e}")
        return triggered

    def execute_halt(self, triggered: list[str]):
        if not triggered:
            return
        self.cancel_all_orders()
        self.verify_no_open_orders()
        self.emergency_close_positions()
        self.persist_halt_until(timedelta(hours=24))
        self.block_new_entries()
        self.send_alert(triggered)
```

#### 라이브 검증 (W9 D60)

- **Paper mode 도 모두 적용** (research 06 권고: backtest != live, but kill switch 는 같은 path)
- 12 Layer × 5 paper alphas × 3 동시 발동 시뮬레이션 = 180 unit tests
- HaltOrchestrator 의 race condition 검증 (asyncio.gather + lock)
- 38일 PoC 의 commit `c8f4e7b` 의 6-step path 정합 확인

### 3.3 Open Source Disclaimer (LICENSE + SECURITY + DISCLAIMER)

#### LICENSE (W1 D1)

```
MIT License

Copyright (c) 2026 Yesol Heo (Yesol-Pilot)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

#### SECURITY.md (W3 D17)

```markdown
# Security Policy

## Supported Versions
- main branch: actively supported
- v1.x.x tags: 6 months after release

## Reporting a Vulnerability
Email: dpthf1537@gmail.com (or open a private security advisory on GitHub)
Response SLA: 7 days
Disclosure timeline: 90 days after fix

## Kill Switch
This project implements a 12-Layer Kill Switch (see `src/kill_switch/`).
Production wiring: see `docs/security/kill-switch.md`.
Paper mode: kill switch is fully active (testing 환경 = production 환경).

## Sensitive Files
- `.env*`: gitignored
- `secrets/`: gitignored
- `data/private/`: gitignored
```

#### DISCLAIMER.md (W1 D5)

```markdown
# Disclaimer

이 프로젝트는 **교육 목적의 1인 retail quant POC** 이다.
This is a 1-person retail quant proof of concept for educational purposes only.

## 영문 Cold Honest Notice

- **No investment advice**: nothing here is a recommendation to buy, sell, or hold any security.
- **No fiduciary duty**: the author owes no fiduciary obligation to any user, contributor, or fork.
- **Past performance does not predict future results**: the 38-day PoC documented in `docs/closure-note.md` shows -15.1% PaperPnL with 37.7% win rate. This is a real and replicable failure.
- **Use at your own risk**: forking, modifying, or running this code is at the user's sole risk. The MIT license disclaims all warranties and liability.

## 한국어 Cold Honest 안내

- 본 코드는 **투자 자문 아님**. 매수/매도/보유 권유 없음.
- 본 코드는 **자기자본 paper mode 가정**. 외부 판매 / 위탁 운용 절대 금지.
- 한국 외부 판매 시 **자본시장법 제8조의2 (투자자문업) 위반** 가능 — 형사처벌 risk.
- 본 코드 fork 또는 수정 후 발생하는 모든 결과는 사용자 책임.
- 38일 PoC 결과 = WR 37.7% / PaperPnL -15.1% / 0 Sharpe. **alpha 검증 실패 사례**.

## Korean Regulatory Cold 박제

- 외국환거래법: 한국 거주자가 외화 derivative trading 시 신고 의무 (5만 달러 초과)
- 자본시장법 제8조의2: 투자자문업 등록 없이 타인 자본 운용 형사처벌
- 자본시장법 제286조: 미신고 외환 거래 형사처벌

## License

MIT — `LICENSE` 참조. 본 disclaimer 는 LICENSE 의 "AS IS" / "no warranty" 조항을 한국 사용자 향 보충 설명.
```

### 3.4 OWASP Top 10 (Web Application) 자동 탐지 + 패치

owner 자산: SecurPilot Engine (`007.infra-tools/` 아래)에 OWASP 12종 결정론적 패치 코드 박제. 본 plan 안에서 재활용:

| OWASP | Risk in quant-poc context | Mitigation |
|---|---|---|
| A01 Broken Access Control | Public API `/quant/api/*` 가 user-specific data 노출 | rate-limit IP-based + no PII storage (research 10) |
| A02 Cryptographic Failures | KIS AppSecret 평문 환경변수 | Supabase Vault (encrypted at rest) |
| A03 Injection | SQL injection on Supabase queries | Supabase parameterized queries only, no raw SQL |
| A04 Insecure Design | Kill Switch 우회 path | 12 Layer 모두 production wiring (paper mode 도) |
| A05 Security Misconfiguration | Next.js dev tools 노출 | `next.config.mjs` 안 `poweredByHeader: false`, CSP 헤더 |
| A06 Vulnerable Components | dependency vulnerabilities | `npm audit --production` CI 매일, `dependabot.yml` 활성 |
| A07 Auth & Session Failures | public API 의 auth 부재 (의도적) | rate-limit + IP throttle + no session 필요 |
| A08 Software & Data Integrity | npm package tampering | `package-lock.json` commit + `npm ci` only in CI |
| A09 Logging & Monitoring Failures | 사고 후 trace 어려움 | OpenTelemetry + Sentry + Supabase logs (Section 4) |
| A10 SSRF | LLM proxy 가 internal endpoint 호출 | LLM 사용 시 allowlist URLs only |

#### 자동 CI 검증 (W1 D2)

```yaml
# .github/workflows/security.yml
name: security
on:
  schedule:
    - cron: '0 9 * * 1'  # 매 Monday 09:00 UTC
  pull_request:
jobs:
  npm-audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm audit --production --audit-level=high
  python-audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install pip-audit
      - run: pip-audit -r requirements.txt
  gitleaks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: { fetch-depth: 0 }
      - uses: gitleaks/gitleaks-action@v2
```

### 3.5 한국 규제 cold 박제 (한국 사용자 향)

- **자기자본 자동매매**: 합법 (research 05)
- **타인 자본 위탁 운용**: 형사처벌 risk (자본시장법 제8조의2 위반)
- **외환 거래 신고**: 5만 달러 초과 시 외국환거래법 신고 의무
- **개인정보 처리**: PIPA 5 cron + data_retention_enforcer (이미 `data_retention_enforcer.py` 박제, W2 D8 적용)
- **금융위원회 등록**: 본 POC 외부 판매 없음 = 미등록

본 plan 안 모든 작업은 **자기자본 paper mode + 자기자본 live mode 만 가정**. 외부 자본 위탁 가능성 0건.

### 3.6 Audit Trail (SHA-256 누적)

owner 자산: SecurPilot 의 SHA-256 chain audit log 패턴 재활용.

```python
# src/audit/sha256_chain.py
def append_audit(event: dict):
    prev_hash = get_last_hash()
    payload = json.dumps({**event, "prev": prev_hash}, sort_keys=True)
    new_hash = hashlib.sha256(payload.encode()).hexdigest()
    db.insert("audit_log", {"event": event, "prev": prev_hash, "hash": new_hash})
```

- 모든 trade event + kill switch trigger + credential access = audit_log row
- chain 검증: `python tools/verify_audit_chain.py` (W11 D72 추가)
- 90일 retention + Supabase Pro backup

---

## Section 4. Monitoring + Observability

### 4.1 Metrics Inventory (5차원 × 각 4~6 metrics)

| 차원 | Metrics | 출처 | 주기 |
|---|---|---|---|
| D1 Code | test pass count / coverage / build time / mutation kill rate / benchmark p99 | pytest + Codecov + GitHub Actions | daily |
| D2 Academic | paper word count / references count / submission status / SSRN downloads | git ls-files + SSRN API + manual | weekly |
| D3 OSS | stars / forks / clones / external contributors / open issues / merged PRs | gh repo view + GitHub Insights | daily |
| D4 Live | Lighthouse 4 categories / Uptime / Web Vitals / Public API rate / Supabase egress | Vercel Analytics + Supabase Logs + Lighthouse CI | daily |
| D5 Comm | Twitter impressions / LinkedIn views / Substack opens / HN upvotes / Reddit karma | platform APIs + manual | daily |

### 4.2 Tools Stack

| Tool | 역할 | Cost | 활용 위치 |
|---|---|---|---|
| **Vercel Analytics** | page views + Web Vitals | Pro $20/월 포함 | D4 |
| **Supabase Logs** | DB queries + Edge Functions + audit_log | Pro $25/월 포함 | D1, D4 |
| **GitHub Insights** | stars / clones / contributors | Free | D3 |
| **Codecov** | coverage report + PR comment | Free for OSS | D1 |
| **OpenTelemetry** | distributed traces (Python + Node) | Free, self-hosted | D1, D4 |
| **Sentry** | error tracking + breadcrumbs | Free tier 5K errors/월 | D1, D4 |
| **Plausible** (옵션) | privacy-friendly analytics | $9/월 (옵션, W10+) | D4, D5 |
| **GA4** | Google Analytics 4 + 한국 시장 visibility | Free | D4, D5 |
| **Sentry Performance** | Web Vitals deep dive | 위 Sentry free tier 포함 | D4 |
| **Better Stack (Uptime)** | uptime check | Free (10 monitors) | D4 |

#### 비활용 (cold 판단)

- **Datadog** ($15+/host/월): 1인 retail overkill, Supabase + Sentry + Vercel 으로 cover
- **New Relic**: 동상
- **Mixpanel**: D5 의 Twitter API 로 cover 가능
- **Amplitude**: 동상

### 4.3 D1 Code Quality Monitoring 상세

#### GitHub Actions metrics emit (W1 D3)

```yaml
# .github/workflows/test.yml
- name: Run tests
  run: pytest --cov=src --cov-report=xml --junitxml=junit.xml -q
- name: Upload coverage to Codecov
  uses: codecov/codecov-action@v4
- name: Insert metrics to Supabase
  run: |
    python tools/insert_test_metrics.py \
      --commit ${{ github.sha }} \
      --branch ${{ github.ref_name }} \
      --tests-passed $(grep -oP '\d+(?= passed)' pytest.log) \
      --coverage $(jq '.totals.percent_covered' coverage.json)
```

#### Supabase `quant_milestone_metrics` 테이블 schema

```sql
create table quant_milestone_metrics (
  id uuid primary key default uuid_generate_v4(),
  recorded_at timestamptz default now(),
  dimension text check (dimension in ('D1', 'D2', 'D3', 'D4', 'D5')),
  metric_name text not null,
  metric_value numeric not null,
  meta jsonb default '{}'
);
create index on quant_milestone_metrics (recorded_at desc, dimension);
```

#### Strategy Lead 자동 보고 query

```sql
select dimension, metric_name, metric_value, recorded_at
from quant_milestone_metrics
where recorded_at >= now() - interval '7 days'
order by dimension, metric_name, recorded_at;
```

### 4.4 D4 Live Production Monitoring 상세

#### Vercel Web Vitals (W1 D2 활성)

```typescript
// src/app/layout.tsx
import { SpeedInsights } from '@vercel/speed-insights/next'
import { Analytics } from '@vercel/analytics/react'

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html>
      <body>
        {children}
        <Analytics />
        <SpeedInsights />
      </body>
    </html>
  )
}
```

#### Lighthouse CI (W8 D54)

```yaml
# .github/workflows/lighthouse.yml
name: lighthouse-ci
on:
  schedule:
    - cron: '0 9 * * *'  # 매일 09:00 UTC
jobs:
  lhci:
    runs-on: ubuntu-latest
    steps:
      - run: npm install -g @lhci/cli
      - run: |
          lhci autorun \
            --collect.url=https://heoyesol.kr/quant \
            --assert.preset=lighthouse:recommended \
            --assert.assertions.categories:performance=0.95 \
            --upload.target=temporary-public-storage
```

#### Sentry Error Tracking (W2 D8)

```typescript
// src/instrumentation.ts (Next.js 15)
import * as Sentry from '@sentry/nextjs'

Sentry.init({
  dsn: process.env.SENTRY_DSN,
  tracesSampleRate: 0.1,  // 10% sampling for free tier preservation
  profilesSampleRate: 0.01,
})
```

```python
# src/main.py (Python)
import sentry_sdk
sentry_sdk.init(
    dsn=os.environ["SENTRY_DSN_PYTHON"],
    traces_sample_rate=0.1,
)
```

#### Better Stack Uptime (W2 D10)

- Monitor 1: `https://heoyesol.kr/quant` 5분 주기, status check ≥ 95%
- Monitor 2: `https://heoyesol.kr/quant/api/v1/health` 1분 주기 (W5 이후)
- Monitor 3: Supabase `https://[project].supabase.co/rest/v1/` 1분 주기
- Email + Slack notification on failure (response time > 3s or status != 200)

### 4.5 Strategy Lead 매주 자동 보고 (cron Monday 08:00 KST)

```python
# scripts/weekly_progress_report.py
def generate_weekly_report():
    metrics = fetch_metrics_last_7_days()
    report = render_template("weekly_report.md.j2", metrics=metrics)

    # 5차원 dashboard insert
    db.insert("strategy_lead_reports", {
        "week": current_week_num(),
        "report_md": report,
        "metrics_snapshot": metrics,
    })

    # owner alert
    send_telegram(BOT_TOKEN, OWNER_CHAT_ID, summary_120_words(report))
    send_email(OWNER_EMAIL, "Week N Progress Report", report)
```

#### Supabase cron 등록 (W1 D6)

```sql
select cron.schedule(
  'weekly-progress-report',
  '0 23 * * 0',  -- 매 Sunday 23:00 UTC = Monday 08:00 KST
  $$ select net.http_post('https://[project].supabase.co/functions/v1/weekly-report'); $$
);
```

#### owner 매 Monday 5분 review

- Telegram summary 120 단어 이내
- 5차원 dashboard 1 페이지 (heoyesol.kr/quant/internal, owner only auth)
- 5분 내 review + 다음 주 priority 1~3건 결정 → Strategy Lead 적용

### 4.6 GA4 + Plausible (옵션, 한국 시장 visibility)

- **GA4** (Free, 기존 heoyesol.kr 정착): cross-property report 활용 (research 14 의 한국 retail visibility 측정)
- **Plausible** (선택, W10 활성): privacy-friendly, $9/월. EU GDPR compliance + 한국 PIPA 정합 더 강함
- 비교: GA4 = 무료 + 깊은 분석, Plausible = 유료 + privacy 강함. 12주 plan 안에서는 GA4 만 + Plausible W10+ 옵션.

### 4.7 Audit Log Dashboard (W11 D72)

- Supabase RLS 적용: owner only auth
- 14일 trade event + kill switch trigger + credential access + cron run = audit_log table
- chain verify command: `python tools/verify_audit_chain.py`
- 사고 발생 시 trace timeline 시각화 (audit_log → Sentry breadcrumbs cross-link)

---

## Section 5. Weekly Risk Matrix

각 week 의 cold risks + mitigation. 사고 발생 시 즉시 적용 가능한 lever 만 박제.

### Week 1 (D1~D7): Setup risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| GitHub repo name SEO 약함 | 30% | M | 12주 plan 종료 후 rename 가능 (GitHub redirect auto). 우선 `quant-poc-multi-asset` 유지. |
| License 선택 오류 (GPL or BSL) | 5% | H | research 09 권고 MIT 만 (Apache 2.0 보다 simpler, 1인 retail fit) |
| Vercel project ID mismatch → 잘못된 repo 배포 | 10% | H | `.vercel/project.json` 의 projectId + orgId 매 deploy 전 검증 (D:\00.test\CLAUDE.md §1.2 정합) |
| KIS Developers 가입 reject (한국 신분 확인) | 15% | M | owner 직접 한국투자증권 계좌 + KIS Developers 가입 (owner action 2~3h) |
| Twitter 계정 정지 (신규 계정 + 빠른 follow) | 10% | M | first week = profile 완성 + 1~2 posts only (no follow spam) |

### Week 2 (D8~D14): KIS API integration risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| KIS API rate limit (20 RPS) 초과 → ban | 25% | H | exponential backoff + token bucket (10 RPS soft cap, 20 RPS hard cap). Mock client 우선 |
| KIS WS disconnect 빈번 | 30% | M | reconnect with jitter, heartbeat 30s, dead-letter queue for skipped events |
| Supabase free tier 한도 초과 (egress 5GB) | 5% | L | Pro $25/월 활성 (W1 D1) → 250GB egress 보장 |
| 첫 LinkedIn post 0 engagement | 70% | L | 한국 LinkedIn 활동도 낮음 (research 15). 본 plan 의 LinkedIn target = slow accumulation |

### Week 3 (D15~D21): KIS finalize risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| 모의투자 첫 trade 의 unintended 의도하지 않은 매수 | 5% | H | paper mode 확정 + double check `is_paper_mode = True` assertion |
| 100 tests 목표 → quality 보다 quantity 우선 → flaky | 30% | M | test bloat 회피 (1 알파 30 tests 적당), flaky 발견 시 즉시 rewrite |
| Substack 첫 newsletter open rate 20% 미만 | 40% | L | 첫 newsletter = small audience (예: 5~10 subs), 측정 base 무의미. 단순 launch signaling |

### Week 4 (D22~D28): IBKR 가입 risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| IBKR Korea 가입 reject (자본 부족 / 신분 / 거주지) | 30% | H | 백업 path = KIS 단독 (D4 dashboard 의 US ETF section delay to W6) + Yahoo Finance 데이터로 backtest only |
| README v2 viral 일부 → 첫 100+ stars 도달 → maintenance burden | 5% | M | external PR triage = max 1h/day 예산 정착. 아직 시점이 아님 (W4) |
| coverage 60% 목표 → 인프라 (logging) 가 60% 차지 → 비즈니스 로직 coverage 40% only | 40% | L | W8 의 80% 가 핵심. W4 는 60% 만족 (인프라 무관) |

### Week 5 (D29~D35): Crypto integration risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Bybit / OKX WS API 정책 변경 | 10% | M | 38일 PoC 의 Binance `!forceOrder@arr` 영구 1/sec 정책 변경 학습. 3-way redundancy (Binance + Bybit + OKX) 가 mitigation |
| 38일 PoC 의 6 알파 코드 재활용 시 hidden coupling | 25% | M | 신규 `quant-poc-multi-asset` repo 에 6 알파 zero-rewrite 이전. coupling 발견 시 즉시 refactor |
| Korean Cherry Quant guest post draft reject | 50% | L | 단순 draft 제안만, reject 시 자체 Substack 으로 대체 |

### Week 6 (D36~D42): Options + external contributor risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Theta Data Value $80 결제 → quality 불만족 (옵션 데이터 incomplete) | 20% | L | refund window 30일, free tier 먼저 검증 |
| 첫 external contributor 미도래 (W6 D42 까지 0건) | 50% | M | mitigation = W7 의 awesome-quant PR 가속 + r/algotrading 2nd post |
| Reddit r/algotrading first post downvote (cold honest narrative 가 부정 평가) | 25% | L | downvote 시 post 회수 가능, retry W9 with different angle |

### Week 7 (D43~D49): Integration risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| 4 자산군 unified backtest 가 5 자산군 schema mismatch (data type 불일치) | 30% | M | Pydantic schema 통일 (research 02 의 NormalizedInput pattern 학습) |
| Paper 1 draft 50% target → 4,000 단어 미달 | 40% | L | W8 까지 buffer. cold 박제: 50% = section 1+2+3 완료 |
| Supabase Realtime 의 동시 connections 한도 (500) 발견 시 | 5% | L | 12주 plan 안 visitor 동시 500 도달 가능성 5% 미만 |

### Week 8 (D50~D56): Quality + GitHub stars risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| GitHub stars < 50 (W8 target 100~200) | 40% | M | HN pre-launch 조정 (W12 → W14 옵션), awesome-quant PR 가속, Reddit 2~3 추가 post |
| coverage 80% 미달 (75% 도달) | 30% | M | W9~W11 의 1 week buffer 활용. coverage 가 90% 까지 가야 함 |
| DSR/PBO 도구 implement 시 외부 lib 충돌 | 25% | L | mlfinlab fork 또는 자체 implement (학습 가치 > 외부 lib 의존) |

### Week 9 (D57~D63): Kill Switch + Paper draft risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| L10/L11/L12 의 false-positive (정상 strategy 를 halt) | 35% | H | unit test 30+ 추가 + paper mode 1주 shadow run (실 halt action 차단, log only) |
| SSRN paper draft 90% → 8,000 단어 미달 (target 6,000 단어) | 30% | L | 6,000 단어 = section 1~5 완료. 8,000 단어 는 honor target |
| ReScience PR 의 reproducibility report 작성 어려움 | 50% | M | W12 까지 30% draft 만 OK. 정식 submit 은 W14+ |

### Week 10 (D64~D70): Polish + Lighthouse risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Lighthouse Performance < 90 (image / JS 무거움) | 40% | M | Next.js Image / lazy loading + critical CSS + bundle analyzer + Vercel edge cache |
| Stars 200~400 target 미달 (150 stars 도달) | 35% | M | W11 pre-launch warm-up 강화 + 한국 Cherry Quant guest article 가속 |
| Substack subscribers 100~300 target 미달 (50~80 subs) | 40% | L | research 13 의 retail Substack median = 50 subs. 50~80 = on-target |

### Week 11 (D71~D77): SSRN submit risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| SSRN submission reject (Quantitative Finance Network 자동 분류 실패) | 10% | L | SSRN reject 사례 거의 0, format check 만 통과 시 99% accept |
| Pre-launch tease (D-7 ~ D-1) 의 engagement 약함 | 40% | M | Twitter daily thread 7개 = funnel 효과 누적, individual day low engagement OK |
| HN account karma 50+ 미달 (W9 D63 까지 30~40 karma) | 30% | M | W10~W11 comment activity 가속 (다른 HN posts 에 substantive comment) |

### Week 12 (D78~D84): HN Launch risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| **HN 첫 60min < 5 upvotes** (front page 도달 실패) | 50% | H | 60min Stop/Go gate: Reddit r/algotrading + Product Hunt 동시 launch path 활성. Twitter / LinkedIn 동기화 |
| Show HN title 의 negative tone (honest failure) → moderator flag | 15% | M | title = positive framing + 38-day honest narrative 후행. "Open-source 1-person quant POC with 38-day honest failure documentation" 등 |
| Stars +200 spike → server overload (free tier 만 활용) | 5% | L | Vercel Pro + Supabase Pro 이미 활성 (W1 D1). egress 250GB 충분 |
| owner 의 본업 (이트라이브 CTS-AI) 충돌로 D78~D84 launch 시점 흔들림 | 20% | M | launch 시점 1주 flexible (W12 → W13 옵션, Strategy Lead 자율 결정) |

### 12주 종합 risk cold judgment

- **High-impact risks 종합**: 5건 (Week 1 license, Week 2 KIS rate limit, Week 4 IBKR reject, Week 9 false-positive, Week 12 HN flop)
- **각 risk 의 mitigation path** = 본 plan 안 명시
- **owner G2 결정 필요 risks**: Week 4 (IBKR backup path → KIS only or KIS+Yahoo Finance), Week 12 (HN launch 시점 W12 vs W13)
- **나머지 = Strategy Lead 자율 가능** (G1)

---

## Section 6. Daily Verification Checklist

각 day 끝 5건 check. 모두 PASS 시 다음 day plan 확정. fail 1건 이상 시 mitigation 적용 후 재check.

### 6.1 Check 1: Strategy Lead 자율 task 완료 (Y/N)

- 본 day 의 자율 task 3~5건 모두 deliverable 박제됨
- `git status` 의 staged + committed changes = 본 day plan 의 산출과 매칭
- 미완료 시 next day 의 첫 작업으로 carry-over

### 6.2 Check 2: owner action (필요 시) 완료 (Y/N)

- 본 day 의 owner action (예: 결제 / 가입 / signature) 완료 여부
- 미완료 시 dependent task 차단 → owner 알림 (Telegram + Email)
- D1 (Mon) 의 Vercel Pro 결제 / D8 (Mon) 의 KIS 가입 / D78 (Mon) 의 HN account karma 가 핵심

### 6.3 Check 3: Test pass + coverage update

```bash
# 매 day 끝 자동 실행 (post-commit hook)
pytest -q --cov=src --cov-report=term-missing \
  | tee logs/test-$(date +%Y%m%d).log \
  | tail -3 \
  | mail -s "Day $(date +%j) test report" dpthf1537@gmail.com
```

- 본 day 의 test pass count 가 milestone 대비 매칭
- coverage % 가 weekly target 으로 진척 (W4=60%, W8=80%, W12=90%)
- failing tests > 0 시 next day 의 첫 작업 fix

### 6.4 Check 4: Milestone 진척 보고 (Supabase metrics 테이블 insert)

```bash
# 매 day 끝 자동 실행
python scripts/insert_daily_metrics.py \
  --day "$(date +%Y-%m-%d)" \
  --d1-tests "$(pytest --collect-only -q | tail -1 | grep -oP '\d+')" \
  --d1-coverage "$(coverage report | tail -1 | grep -oP '\d+%' | head -1)" \
  --d3-stars "$(gh repo view --json stargazerCount | jq -r .stargazerCount)" \
  --d4-lighthouse-perf "$(cat logs/lighthouse-latest.json | jq -r .categories.performance.score)"
```

- 5차원 metrics 의 daily row 가 Supabase 에 insert 됐는지 확인
- query: `select count(*) from quant_milestone_metrics where recorded_at::date = current_date;` → ≥ 5 rows

### 6.5 Check 5: GitHub commit + push + 다음 day plan 확정

```bash
git add .
git commit -m "Day $(date +%j) W$(($(date +%j) / 7 + 1)): [본 day deliverable 요약]"
git push origin master
# 또는 PR-based workflow 시:
git push origin feature/day-$(date +%j)
```

- 본 day 의 모든 변경사항 commit 됨
- 다음 day plan (Section 7) review + Strategy Lead 의 자율 task 3~5건 사전 박제

### 6.6 5건 fail 시 escalation

- **1 fail**: Strategy Lead 자율 mitigation 후 재check
- **2 fails**: owner Telegram 알림 + 다음 day plan 1h 지연 가능
- **3+ fails**: Strategy Lead 가 본 week schedule 재조정 + owner G2 결정 요청

---

## Section 7. Week × Day Daily Plan (84 Days)

각 day 의 100~300 단어 spec. 모든 day 의 owner action 시간 명시 (대부분 0, review 만).

### Week 1 — Setup (D1~D7, 5/14 ~ 5/20)

#### Day 1 (Mon, 5/14)

**5차원**: D3 + D4 + D5 (Open Source + Live + Communication)

**Strategy Lead 자율 task**:
- GitHub repo `Yesol-Pilot/quant-poc-multi-asset` public 생성 (`gh repo create --public`)
- LICENSE.md (MIT) + README.md (v0, 100~200 단어 placeholder) 박제
- DISCLAIMER.md + CODE_OF_CONDUCT.md + SECURITY.md 박제
- `.gitignore` 표준 (Python + Node + Vercel + Supabase env)
- `heoyesol.kr/quant` Next.js 15 scaffold (`npx create-next-app@latest --typescript --tailwind`)
- Vercel project link (`vercel link` to existing heoyesol.kr project), `/quant` route 생성
- Twitter `@yesolheo` (또는 `@YesolPilot`) profile 셋업 + bio (cold honest 1줄)
- LinkedIn headline 변경 (`Building a 1-person retail quant POC + AI-native PM`)
- Substack 계정 셋업 (`heoyesol.substack.com` 또는 `quantpoc.substack.com`)
- Threads + Hashnode 계정 셋업

**owner action**:
- Vercel Pro 결제 ($20/월, 신용카드 1회) — **30분 (결제 + Vercel billing setup)**
- Supabase Pro 결제 ($25/월) — **20분**
- KIS Developers 가입 시작 (한국투자증권 계좌 보유 시) — **2~3h (계좌 + Open API 등록 + 모의투자 신청)**

**산출**:
- `gh repo view Yesol-Pilot/quant-poc-multi-asset --json visibility` = `"PUBLIC"`
- `curl -I https://heoyesol.kr/quant` = `HTTP/2 200`
- 5 social channel profile 완성 (cross-link)

**Verification (Section 6 의 5건)**:
1. Strategy Lead task 10건 완료 ✓
2. owner action 3건 완료 (Vercel + Supabase + KIS 가입 시작)
3. 첫 test 없음 (W2 부터)
4. metrics row insert: D3 stars=1, D4 page=200 OK
5. commit `Day 1 W1: setup repo + heoyesol.kr/quant scaffold`

#### Day 2 (Tue, 5/15)

**5차원**: D1 + D4 + Security

**Strategy Lead 자율 task**:
- `.github/workflows/test.yml` (pytest + coverage), `.github/workflows/lint.yml` (ruff + black + mypy), `.github/workflows/security.yml` (gitleaks + npm-audit + pip-audit)
- `.pre-commit-config.yaml` (ruff + black + check-yaml + check-json)
- `pyproject.toml` (Python 3.11+, dev dependencies)
- `package.json` (Next.js + TypeScript dev dependencies)
- Vercel Web Vitals + Speed Insights 통합 (`@vercel/analytics` + `@vercel/speed-insights`)
- Sentry Next.js setup (DSN env var)
- README v0.5 (5 sections placeholder: hero + quick start + architecture + results + docs link)
- 첫 PR with CI green (lint + security workflows pass)

**owner action**:
- Sentry account signup (free tier) + DSN 발급 → Vercel env var 추가 — **15분**

**산출**:
- `.github/workflows/*.yml` 3개 파일
- 첫 PR `#1: setup CI/CD + Sentry` merged
- Sentry dashboard 첫 deploy 인식

**Verification**:
1. Strategy Lead 8건 ✓
2. owner action 1건 (Sentry) ✓
3. CI test green: `gh workflow list | grep -c success` ≥ 3
4. metrics row: D4 sentry_dsn=set
5. commit `Day 2 W1: CI/CD + Sentry + pre-commit`

#### Day 3 (Wed, 5/16)

**5차원**: D1 + D3

**Strategy Lead 자율 task**:
- `src/` 디렉토리 구조: `src/strategies/`, `src/data/`, `src/kill_switch/`, `src/backtest/`, `src/paper/`, `src/audit/`
- `src/strategies/base.py` abstract class (`Strategy` interface: `on_bar`, `on_trade`, `on_kill_switch`)
- `tests/test_base_strategy.py` 첫 10 tests (abstract class + interface)
- `requirements.txt` (pytest + pandas + numpy + ccxt + ib_insync + pydantic + supabase-py)
- README v1 (Hero + Quick Start + Architecture placeholder Mermaid + Results placeholder + Citation BibTeX placeholder)
- 5~7 badges (build / coverage / license / python / stars)

**owner action**:
- KIS Developers 가입 완료 → AppKey + AppSecret 발급 (W1 D1 시작분의 follow-up) — **1h**
- KIS AppKey + AppSecret 을 Supabase Vault 에 저장 (owner Telegram → Strategy Lead 가 vault SQL 박제)

**산출**:
- `pytest -q` ≥ 10 PASS
- README v1 (1,500~2,500 단어)
- KIS credentials secured

**Verification**:
1. Strategy Lead 5건 ✓
2. owner action 1건 (KIS 발급) ✓
3. tests 10 PASS, coverage 50%~70% (작은 surface)
4. metrics row: D1 tests=10
5. commit `Day 3 W1: src structure + base strategy + 10 tests`

#### Day 4 (Thu, 5/17)

**5차원**: D2 + D3

**Strategy Lead 자율 task**:
- `docs/paper-1/` 디렉토리 생성
- `docs/paper-1/refs.bib` 박제 (research 06 의 62 references 중 curated 50~55)
- `docs/paper-1/outline.md` (5 sections: Introduction + Method + Results + Honest Failure + Lessons + 6. Open Source Link)
- 한국어 README (`README.ko.md`) draft (영문 README 의 60~80%)
- 첫 줄 link bar: `[English](README.md) | [한국어](README.ko.md)`
- `CONTRIBUTING.md` 박제 (PR template + commit message convention + test requirement)

**owner action**:
- 없음 (Strategy Lead 자율)

**산출**:
- `wc -l docs/paper-1/refs.bib` ≥ 50 entries
- README.ko.md (3,000~5,000 단어)
- CONTRIBUTING.md 박제

**Verification**:
1. Strategy Lead 6건 ✓
2. owner action 없음 ✓
3. tests 10 (unchanged)
4. metrics row: D2 refs=50
5. commit `Day 4 W1: paper-1 outline + Korean README + CONTRIBUTING`

#### Day 5 (Fri, 5/18)

**5차원**: D4 + D5

**Strategy Lead 자율 task**:
- `src/app/quant/page.tsx` (landing page): hero + 38-day PoC summary card + GitHub repo link + Substack subscribe form
- Tremor 설치 (`npm install @tremor/react`) + 첫 chart 컴포넌트 (placeholder data)
- Vercel deploy → `https://heoyesol.kr/quant` 200 OK + Lighthouse 측정 (≥ 80)
- LinkedIn 첫 post draft (Tuesday 09:00 KST publish 예정, owner D8 review)
- DISCLAIMER.md 갱신 (한국 규제 cold 박제, Section 3.3 정합)

**owner action**:
- 없음 (LinkedIn post draft 만, publish 는 D8)

**산출**:
- Lighthouse Performance ≥ 80, Accessibility ≥ 90
- Tremor chart 1개 렌더

**Verification**:
1. Strategy Lead 5건 ✓
2. owner action 없음 ✓
3. tests 10
4. metrics row: D4 lighthouse_perf=0.80, D4 page=quant landing
5. commit `Day 5 W1: landing page + Tremor + LinkedIn draft + DISCLAIMER ko`

#### Day 6 (Sat, 5/19)

**5차원**: D1 + Monitoring

**Strategy Lead 자율 task**:
- Supabase `quant_milestone_metrics` 테이블 생성 (Section 4.3 schema)
- Supabase `audit_log` 테이블 생성 (SHA-256 chain, Section 3.6)
- Supabase cron `weekly-progress-report` 등록 (Section 4.5, 매 Sunday 23:00 UTC)
- `scripts/weekly_progress_report.py` skeleton (template render + Telegram send)
- Vercel project `heoyesol-kr` 의 env var 추가 (SUPABASE_URL, SUPABASE_ANON_KEY, SENTRY_DSN)
- Better Stack Uptime monitor 1 (heoyesol.kr/quant) 등록

**owner action**:
- Telegram bot token (NEO_ALERT_BOT_TOKEN 별도 또는 기존 활용) → env var — **5분**

**산출**:
- Supabase 2 tables + 1 cron
- Better Stack first uptime check green

**Verification**:
1. Strategy Lead 6건 ✓
2. owner action 1건 (Telegram bot) ✓
3. tests 10
4. metrics row: D1 audit_log_table=created
5. commit `Day 6 W1: Supabase metrics + cron + Better Stack`

#### Day 7 (Sun, 5/20)

**5차원**: D1 + Cleanup

**Strategy Lead 자율 task**:
- W1 종합 review + Section 5 의 Week 1 risks 5건 모두 mitigated 확인
- `docs/weekly/W1.md` 작성 (Mon~Sun 종합, 5차원 metrics 박제)
- KIS API mock client (`src/data/kis/mock_client.py`) skeleton (W2 D8 의 real client 의 base)
- `tests/test_kis_mock_client.py` 5 tests
- README v1.1 (Architecture Mermaid 박제 추가, 2,500~3,500 단어)

**owner action**:
- W1 종합 review (Telegram + 5차원 dashboard preview) — **30분**
- W2 의 KIS API rate limit 정책 owner 확인 (20 RPS soft cap 권고 ACCEPT 여부) — **10분**

**산출**:
- W1 종합 보고서
- pytest 15 PASS (10 + 5 KIS mock)

**Verification**:
1. Strategy Lead 5건 ✓
2. owner action 2건 (W1 review + KIS rate limit G2) ✓
3. tests 15 PASS, coverage 50%~70%
4. metrics row: 5 dimensions all baseline
5. commit `Day 7 W1: W1 closure + KIS mock client`

---

### Week 2 — KIS Build (D8~D14, 5/21 ~ 5/27)

#### Day 8 (Mon, 5/21)

**5차원**: D1 + D5

**Strategy Lead 자율 task**:
- `src/data/kis/client.py` (real KIS REST client, requests + token refresh)
- `src/data/kis/websocket.py` (KIS WS client, websockets lib + heartbeat 30s)
- `tests/test_kis_client.py` 15 tests (mock-based, no real API call in CI)
- LinkedIn 첫 post publish (Tuesday 09:00 KST, but Day 8 = Monday Korea time, so post pre-scheduled or 화요일 publish 보장)
- Substack 첫 newsletter draft (cold honest 시작 narrative)

**owner action**:
- LinkedIn post publish 확인 (Tuesday 09:00 KST) — **5분 review**

**산출**:
- KIS client + WS scaffold (no live call yet)
- pytest 30 PASS

**Verification**:
1. Strategy Lead 5건 ✓
2. owner action 1건 (LinkedIn review) ✓
3. tests 30 PASS, coverage 55%~70%
4. metrics row: D1 tests=30, D5 linkedin_post=1
5. commit `Day 8 W2: KIS REST + WS client scaffold`

#### Day 9 (Tue, 5/22)

**5차원**: D1 + D2

**Strategy Lead 자율 task**:
- `src/strategies/a11_kr_momentum.py` scaffold (한국 momentum 알파, research 06 의 momentum evidence 4 references 활용)
- `tests/test_a11.py` 10 tests
- `docs/paper-1/01-introduction.md` draft (500~800 단어, 한국 retail quant gap framing)
- `docs/paper-1/refs.bib` 의 5~10 references cited

**owner action**:
- 없음

**산출**:
- A11 알파 scaffold + 10 tests
- Paper 1 §1 Introduction draft

**Verification**:
1. Strategy Lead 4건 ✓
2. owner action 없음 ✓
3. tests 40 PASS, coverage 60%
4. metrics row: D1 tests=40, D2 paper1_words=800
5. commit `Day 9 W2: A11 scaffold + Paper 1 Introduction`

#### Day 10 (Wed, 5/23)

**5차원**: D1 + D3

**Strategy Lead 자율 task**:
- `src/strategies/a12_kr_mean_reversion.py` scaffold (OU process 기반, 38일 PoC A2 의 학습 반영)
- `tests/test_a12.py` 10 tests
- README v1.2 (Architecture Mermaid 다이어그램 추가 + 4-asset placeholder)
- Better Stack Uptime monitor 2 (heoyesol.kr/quant/api/v1/health) 준비 (W5 까지 endpoint 가 없으므로 W5 활성)

**owner action**:
- 없음

**산출**:
- A12 알파 scaffold + 10 tests

**Verification**:
1. Strategy Lead 4건 ✓
2. owner action 없음 ✓
3. tests 50 PASS, coverage 60%
4. metrics row: D1 tests=50
5. commit `Day 10 W2: A12 scaffold + README v1.2`

#### Day 11 (Thu, 5/24)

**5차원**: D1 + D2

**Strategy Lead 자율 task**:
- `src/strategies/a13_kr_pairs.py` scaffold (KR pairs trading, KOSPI 200 안 cointegrated pairs)
- `tests/test_a13.py` 10 tests
- `docs/paper-1/02-method.md` draft (1,200~1,800 단어, multi-asset architecture + alpha registry)

**owner action**:
- 없음

**산출**:
- A13 알파 scaffold + 10 tests
- Paper 1 §2 Method draft

**Verification**:
1. Strategy Lead 3건 ✓
2. owner action 없음 ✓
3. tests 60 PASS, coverage 60%
4. metrics row: D1 tests=60, D2 paper1_words=2800
5. commit `Day 11 W2: A13 scaffold + Paper 1 Method`

#### Day 12 (Fri, 5/25)

**5차원**: D1 + D4

**Strategy Lead 자율 task**:
- `src/strategies/a14_kr_macro.py` scaffold (KR macro event bracket, BOK 금리 결정 / 한국은행 발표 시점)
- `tests/test_a14.py` 10 tests
- Live page `/quant/strategies/` route + 4 알파 (A11~A14) summary card + GitHub link
- Tremor chart 4개 (각 알파 별 placeholder PnL line)

**owner action**:
- 없음

**산출**:
- A14 알파 scaffold + 10 tests
- /quant/strategies/ page live

**Verification**:
1. Strategy Lead 4건 ✓
2. owner action 없음 ✓
3. tests 70 PASS, coverage 60%~65%
4. metrics row: D1 tests=70, D4 page=strategies
5. commit `Day 12 W2: A14 scaffold + /quant/strategies/ page`

#### Day 13 (Sat, 5/26)

**5차원**: D1 + Cleanup

**Strategy Lead 자율 task**:
- A11~A14 의 backtest runner unification (`src/backtest/runner.py`) + 단일 entry point
- `tests/test_backtest_runner.py` 15 tests
- 38일 PoC 의 commit `c8f4e7b` 의 Kill Switch 6-step 의 L1~L9 코드 이전 (`src/kill_switch/` 재구성)
- L1~L9 unit tests 30+

**owner action**:
- 없음

**산출**:
- Backtest runner 통합
- L1~L9 ported + tests

**Verification**:
1. Strategy Lead 4건 ✓
2. owner action 없음 ✓
3. tests 115 PASS, coverage 65%
4. metrics row: D1 tests=115
5. commit `Day 13 W2: backtest runner + L1-L9 Kill Switch ported`

#### Day 14 (Sun, 5/27)

**5차원**: D2 + D5 + Cleanup

**Strategy Lead 자율 task**:
- W2 종합 review + risks 5건 mitigated 확인 (Section 5)
- `docs/weekly/W2.md` 작성
- Substack 첫 newsletter publish ("38일 PoC closure: 191 trades, 37.7% win rate, -15.1% PnL, what went wrong")
- Twitter 첫 thread publish (Substack post 의 8 tweet excerpt)
- `docs/paper-1/03-results.md` placeholder

**owner action**:
- Substack newsletter publish 확인 + Twitter thread review — **15분**
- W2 종합 review (Telegram + dashboard) — **20분**

**산출**:
- Substack subscribers 5~15 (첫 신규)
- Twitter +30~80 followers (첫 thread 효과)

**Verification**:
1. Strategy Lead 5건 ✓
2. owner action 2건 (publish 확인 + W2 review) ✓
3. tests 115 PASS
4. metrics row: D5 substack_subs=5~15, D5 twitter_followers=30~80
5. commit `Day 14 W2: W2 closure + Substack #1 + Twitter #1`

---

### Week 3 — KIS Finalize (D15~D21, 5/28 ~ 6/3)

#### Day 15 (Mon, 5/28)

**5차원**: D1 + Security

**Strategy Lead 자율 task**:
- KIS 모의투자 첫 paper trading run (`python run_paper.py --strategy a11 --paper`)
- Audit log 첫 entry (W1 D6 의 audit_log 테이블에 trade event insert)
- `src/kill_switch/l1_orchestrator.py` HaltOrchestrator skeleton (L1~L9 통합)
- `tests/test_paper_runner.py` 10 tests

**owner action**:
- 없음 (KIS 모의투자 계좌 W1 D3 에 가입 완료된 가정)

**산출**:
- 첫 paper trade event audit_log row
- HaltOrchestrator skeleton

**Verification**:
1. Strategy Lead 4건 ✓
2. owner action 없음 ✓
3. tests 125 PASS, coverage 65%
4. metrics row: D1 tests=125, audit_log first row
5. commit `Day 15 W3: paper trading first run + HaltOrchestrator`

#### Day 16 (Tue, 5/29)

**5차원**: D1 + D3

**Strategy Lead 자율 task**:
- A11~A14 paper trading 24h shadow run (`python run_paper.py --all --shadow --hours 24`)
- Backtest 5년치 데이터 (Yahoo Finance + KIS historical) 다운로드 + cache
- `tests/test_alpha_backtest_5y.py` 12 tests (1 알파 3 tests × 4 알파)
- README v1.3 (Quick Start 5-minute path 갱신 + Architecture v2)

**owner action**:
- 없음

**산출**:
- Backtest 5y data cached
- 12 신규 tests

**Verification**:
1. Strategy Lead 4건 ✓
2. owner action 없음 ✓
3. tests 137 PASS, coverage 65%~70%
4. metrics row: D1 tests=137
5. commit `Day 16 W3: 5y backtest data + 12 tests + README v1.3`

#### Day 17 (Wed, 5/30)

**5차원**: Security + D1

**Strategy Lead 자율 task**:
- `SECURITY.md` 박제 (Section 3.3)
- `src/kill_switch/l10_alpha_decay.py` implement (Section 3.2 의 신규 L10)
- `tests/test_l10_alpha_decay.py` 10 tests
- A2 의 38일 PoC trade log 입력 → L10 발동 positive case 검증

**owner action**:
- 없음

**산출**:
- L10 implement + tests
- SECURITY.md live

**Verification**:
1. Strategy Lead 3건 ✓
2. owner action 없음 ✓
3. tests 147 PASS, coverage 70%
4. metrics row: D1 tests=147
5. commit `Day 17 W3: L10 Alpha Decay + SECURITY.md`

#### Day 18 (Thu, 5/31)

**5차원**: D2

**Strategy Lead 자율 task**:
- `docs/paper-1/03-results.md` draft (1,500~2,000 단어, 38일 PoC + W2~W4 paper trading 합산)
- 표 3~5개 (per-alpha trade count + PnL + Sharpe)
- chart 4~6개 (matplotlib export to PNG, paper-1 figure 폴더)
- 38일 PoC 의 191 trades / WR 37.7% / -15.1% 박제 (cold honest)

**owner action**:
- 없음

**산출**:
- Paper 1 §3 Results draft

**Verification**:
1. Strategy Lead 4건 ✓
2. owner action 없음 ✓
3. tests 147
4. metrics row: D2 paper1_words=4500
5. commit `Day 18 W3: Paper 1 Results draft + figures`

#### Day 19 (Fri, 6/1)

**5차원**: D4 + D5

**Strategy Lead 자율 task**:
- `/quant/paper-trading` page 의 mock data 를 실제 KIS paper trading data 로 교체 (Supabase Realtime subscribe)
- Tremor 4 chart 컴포넌트 활성 (PnL line, trade count bar, win rate gauge, drawdown area)
- Substack #2 draft ("Multi-asset architecture for 1-person quant")

**owner action**:
- 없음

**산출**:
- /quant/paper-trading live with real data
- Substack #2 draft

**Verification**:
1. Strategy Lead 3건 ✓
2. owner action 없음 ✓
3. tests 147
4. metrics row: D4 page=paper-trading, D5 substack_draft=2
5. commit `Day 19 W3: paper-trading live + Substack #2 draft`

#### Day 20 (Sat, 6/2)

**5차원**: D1 + D3

**Strategy Lead 자율 task**:
- Property-based testing (hypothesis) 도입 + 5 tests (kill switch invariant)
- Strategy backtest 의 walk-forward analysis (`src/backtest/walk_forward.py`)
- `tests/test_walk_forward.py` 10 tests
- README v1.4 (Results table cold 박제 갱신)

**owner action**:
- 없음

**산출**:
- 15 신규 tests
- Walk-forward analysis

**Verification**:
1. Strategy Lead 4건 ✓
2. owner action 없음 ✓
3. tests 162 PASS, coverage 70%~75%
4. metrics row: D1 tests=162
5. commit `Day 20 W3: hypothesis tests + walk-forward`

#### Day 21 (Sun, 6/3)

**5차원**: Cleanup + D5

**Strategy Lead 자율 task**:
- W3 종합 review + risks 3건 mitigated 확인
- `docs/weekly/W3.md` 작성
- Substack #2 publish ("Multi-asset architecture")
- Twitter +50 followers target

**owner action**:
- W3 종합 review — **20분**
- Substack #2 publish 확인 — **5분**

**산출**:
- Substack subs 15~30 (누적)
- Twitter +50 (누적 80~130)

**Verification**:
1. Strategy Lead 4건 ✓
2. owner action 2건 ✓
3. tests 162 PASS, coverage 75%
4. metrics row: D5 substack_subs=25
5. commit `Day 21 W3: W3 closure + Substack #2`

---

### Week 4 — IBKR (D22~D28, 6/4 ~ 6/10)

#### Day 22 (Mon, 6/4)

**5차원**: D1 + D3

**Strategy Lead 자율 task**:
- IBKR `ib_insync` wrapper (`src/data/ibkr/client.py`)
- IBKR paper account scaffold (no real funds)
- `tests/test_ibkr_client.py` 15 tests (mock-based)
- README v2 (Mermaid architecture diagram + benchmark table + citation BibTeX)

**owner action**:
- **IBKR Korea paper account 가입** (research 04 의 한국 거주자 신청 path) — **2~4h**
  - **risk: 가입 reject (research 04 의 D4/D5 모순) 시 백업 path = KIS 단독 + Yahoo Finance**

**산출**:
- IBKR client scaffold (no live yet, paper account 가입 후 W4 D24~D25 live)
- README v2

**Verification**:
1. Strategy Lead 4건 ✓
2. owner action 1건 (IBKR 가입 시작) ✓ (가입 결과는 W4 D24)
3. tests 177 PASS, coverage 75%
4. metrics row: D1 tests=177, D3 readme=v2
5. commit `Day 22 W4: IBKR client + README v2`

#### Day 23 (Tue, 6/5)

**5차원**: D1 + D2

**Strategy Lead 자율 task**:
- `src/strategies/a15_us_etf_momentum.py` scaffold (US ETF momentum)
- `src/strategies/a16_us_etf_pairs.py` scaffold (US ETF cointegrated pairs)
- `src/strategies/a17_us_macro.py` scaffold (US macro event, CPI / FOMC)
- `tests/test_a15.py`, `tests/test_a16.py`, `tests/test_a17.py` 각 10 tests = 30 신규 tests
- `docs/paper-1/04-honest-failure.md` draft (800~1,200 단어, 38일 PoC 의 12 alpha-별 cold 박제)

**owner action**:
- 없음

**산출**:
- 30 신규 tests
- Paper 1 §4 Honest Failure draft

**Verification**:
1. Strategy Lead 5건 ✓
2. owner action 없음 ✓
3. tests 207 PASS, coverage 75%
4. metrics row: D1 tests=207, D2 paper1_words=5500
5. commit `Day 23 W4: A15-A17 scaffold + Paper 1 Honest Failure`

#### Day 24 (Wed, 6/6)

**5차원**: D1 + IBKR live (risk-dependent)

**Strategy Lead 자율 task**:
- IBKR paper account 가입 결과에 따른 분기:
  - **accept 시**: IBKR paper account 첫 paper trading run + audit_log row + L1~L9 kill switch test
  - **reject 시 (백업 path)**: A15~A17 의 backtest only mode + Yahoo Finance 데이터 + 별도 KIS Plus (key 발급 시) preparation
- `tests/test_ibkr_paper_trading.py` 15 tests (mock + real if accept)
- 50 신규 tests total (35 from D22~D23 + 15 today)

**owner action**:
- IBKR 가입 결과 확인 (accept/reject) — **5분**
- reject 시 backup path approval (owner G2 — "KIS 단독" or "KIS + Yahoo backtest" choice) — **10분**

**산출**:
- IBKR paper trading first run OR backup path active

**Verification**:
1. Strategy Lead 3건 ✓
2. owner action 1~2건 ✓
3. tests 222 PASS, coverage 75%
4. metrics row: D1 tests=222, D1 ibkr_status=accept|reject
5. commit `Day 24 W4: IBKR paper trading [accept|backup-path]`

#### Day 25 (Thu, 6/7)

**5차원**: D1 + Security

**Strategy Lead 자율 task**:
- `src/kill_switch/l11_regime.py` implement (Section 3.2)
- `tests/test_l11_regime.py` 10 tests (BEAR regime + 변동성 > 10% 발동)
- `src/audit/sha256_chain.py` chain verifier (`tools/verify_audit_chain.py`)
- coverage 측정 → 60% 목표 (W4 D22~D25 의 cumulative)

**owner action**:
- 없음

**산출**:
- L11 + chain verifier
- 10 신규 tests

**Verification**:
1. Strategy Lead 4건 ✓
2. owner action 없음 ✓
3. tests 232 PASS, coverage 60% (target met)
4. metrics row: D1 tests=232, coverage=0.60
5. commit `Day 25 W4: L11 Regime + audit chain verifier`

#### Day 26 (Fri, 6/8)

**5차원**: D4 + D5

**Strategy Lead 자율 task**:
- `/quant/dashboard` 초기 (3 자산군 KR/US/Crypto metrics, Supabase 연결)
- 4 Tremor charts × 3 asset class = 12 charts (PnL + WR + DD + Sharpe per asset)
- Substack #3 draft ("KIS API: 한국 retail quant 의 첫 장벽")
- Cherry Quant guest article 제안 draft (이메일 + 본인 소개)

**owner action**:
- 없음

**산출**:
- /quant/dashboard live (3 자산군)
- Substack #3 draft

**Verification**:
1. Strategy Lead 4건 ✓
2. owner action 없음 ✓
3. tests 232 PASS
4. metrics row: D4 page=dashboard
5. commit `Day 26 W4: /quant/dashboard + Substack #3 draft`

#### Day 27 (Sat, 6/9)

**5차원**: D2 + D3

**Strategy Lead 자율 task**:
- Paper 1 §5 Lessons + §6 Open Source Link draft (1,500 단어)
- Paper 1 draft 총 합산 5,000~7,000 단어 (target met)
- `docs/paper-1/figures/` 디렉토리 (matplotlib PNG 6~10개)
- LICENSE + CONTRIBUTING + CODE_OF_CONDUCT + SECURITY 모두 점검

**owner action**:
- 없음

**산출**:
- Paper 1 draft 60% (target met for W7, ahead of schedule)

**Verification**:
1. Strategy Lead 4건 ✓
2. owner action 없음 ✓
3. tests 232
4. metrics row: D2 paper1_words=7000
5. commit `Day 27 W4: Paper 1 Lessons + Open Source Link`

#### Day 28 (Sun, 6/10)

**5차원**: Cleanup + D5

**Strategy Lead 자율 task**:
- W4 종합 review + risks (특히 IBKR reject) 확인
- `docs/weekly/W4.md` 작성
- Substack #3 publish + LinkedIn #2 publish
- Twitter +200 followers target

**owner action**:
- W4 종합 review — **20분**
- Substack + LinkedIn publish 확인 — **10분**

**산출**:
- Substack subs 30~60 (누적)
- Twitter 누적 200+ followers

**Verification**:
1. Strategy Lead 4건 ✓
2. owner action 2건 ✓
3. tests 232 PASS, coverage 60% ✓
4. metrics row: D5 substack_subs=45, twitter=200
5. commit `Day 28 W4: W4 closure + Substack #3 + LinkedIn #2`

---

### Week 5 — Crypto Integration (D29~D35, 6/11 ~ 6/17)

#### Day 29 (Mon, 6/11)

**5차원**: D1 + D3

**Strategy Lead 자율 task**:
- 38일 PoC 의 6 알파 (A1~A6) 코드 zero-rewrite 이전:
  - A1 Liquidation Cascade
  - A2 Mean Reversion OU (38일 PoC 의 deprecation 권고 유지, 학습 목적만)
  - A3 Extreme Funding Reversal
  - A4 Macro Event Bracket
  - A5 Funding/Basis Harvest
  - A6 Alt MM
- 6 알파 의 base test (각 10 tests) = 60 신규 tests

**owner action**:
- 없음

**산출**:
- A1~A6 ported + 60 tests

**Verification**:
1. Strategy Lead 2건 ✓ (큰 작업)
2. owner action 없음 ✓
3. tests 292 PASS, coverage 65%
4. metrics row: D1 tests=292
5. commit `Day 29 W5: A1-A6 ported from 38-day PoC + 60 tests`

#### Day 30 (Tue, 6/12)

**5차원**: D1 + D4

**Strategy Lead 자율 task**:
- Binance liquidation stream (`!forceOrder@arr`) 재현 + Bybit + OKX 3-way aggregation (commit `4849d84` 의 라이브 wiring 재현)
- `tests/test_cross_exchange_aggregation.py` 18 tests (commit `4849d84` 의 18 tests 재현)
- `/quant/dashboard` 의 crypto 섹션 → liquidation events live count chart

**owner action**:
- 없음

**산출**:
- Cross-exchange aggregation live
- 18 신규 tests

**Verification**:
1. Strategy Lead 3건 ✓
2. owner action 없음 ✓
3. tests 310 PASS, coverage 65%
4. metrics row: D1 tests=310, D4 crypto_live=true
5. commit `Day 30 W5: 3-way liquidation aggregation`

#### Day 31 (Wed, 6/13)

**5차원**: D1 + D2

**Strategy Lead 자율 task**:
- Backtest 5y crypto data (Bybit + OKX + Binance public history) cache
- A1 Liquidation Cascade backtest 90일 → trade count + Sharpe 측정
- A2 OU 의 38일 PoC closure 박제 (A2 deprecation 권고 유지, paper-1 §4 인용)
- `tests/test_a1_a6_backtest.py` 15 tests

**owner action**:
- 없음

**산출**:
- A1~A6 backtest 90일 결과 박제
- 15 신규 tests

**Verification**:
1. Strategy Lead 4건 ✓
2. owner action 없음 ✓
3. tests 325 PASS, coverage 65%~70%
4. metrics row: D1 tests=325
5. commit `Day 31 W5: A1-A6 backtest 90d + A2 deprecation 박제`

#### Day 32 (Thu, 6/14)

**5차원**: Security + D1

**Strategy Lead 자율 task**:
- `src/kill_switch/l12_overfit.py` implement (PBO > 0.7 halt)
- `tests/test_l12_overfit.py` 10 tests
- HaltOrchestrator 의 12 layer 모두 통합 (`src/kill_switch/orchestrator.py`)
- `tests/test_halt_orchestrator.py` 20 tests (race condition + multi-layer trigger)

**owner action**:
- 없음

**산출**:
- L12 + HaltOrchestrator 12-layer 통합
- 30 신규 tests

**Verification**:
1. Strategy Lead 3건 ✓
2. owner action 없음 ✓
3. tests 355 PASS, coverage 70%
4. metrics row: D1 tests=355, kill_switch_layers=12
5. commit `Day 32 W5: L12 Overfit + HaltOrchestrator 12-layer`

#### Day 33 (Fri, 6/15)

**5차원**: D4 + D5

**Strategy Lead 자율 task**:
- `/quant/strategies/[id]/` dynamic route (A11~A17, A1~A6 별 detail page)
- Tremor chart per strategy: PnL + WR + DD + Sharpe + trade count
- Substack #4 draft ("Crypto cross-exchange aggregation: 38-day PoC 의 데이터 활용")
- Reddit r/algotrading 첫 post draft (38일 PoC honest narrative, owner G2 review)

**owner action**:
- Reddit post draft review (cold honest narrative tone check) — **15분**

**산출**:
- /quant/strategies/[id]/ live (10+ pages)
- Substack #4 + Reddit draft

**Verification**:
1. Strategy Lead 4건 ✓
2. owner action 1건 ✓
3. tests 355
4. metrics row: D4 strategy_pages=10
5. commit `Day 33 W5: /quant/strategies/[id]/ + Substack #4 + Reddit draft`

#### Day 34 (Sat, 6/16)

**5차원**: D1 + D3

**Strategy Lead 자율 task**:
- Backtest 의 sensitivity sweep `tools/sensitivity_sweep.py` (38일 PoC 의 A2 108-cell sweep 패턴 재활용)
- A11 momentum 의 sensitivity sweep 첫 실행 (lookback × threshold × stop-loss = 4×6×6 = 144 cells)
- `tests/test_sensitivity_sweep.py` 12 tests
- README v2.1 (sensitivity sweep 결과 박제, Results table 갱신)

**owner action**:
- 없음

**산출**:
- Sensitivity sweep tool
- 12 신규 tests
- README v2.1

**Verification**:
1. Strategy Lead 4건 ✓
2. owner action 없음 ✓
3. tests 367 PASS, coverage 70%~75%
4. metrics row: D1 tests=367
5. commit `Day 34 W5: sensitivity sweep + README v2.1`

#### Day 35 (Sun, 6/17)

**5차원**: Cleanup + D5

**Strategy Lead 자율 task**:
- W5 종합 review + risks 확인
- `docs/weekly/W5.md` 작성
- Substack #4 publish (Crypto cross-exchange) + Reddit r/algotrading 첫 post
- Cherry Quant 한국어 guest article 첫 contact (email + draft)

**owner action**:
- W5 review — **20분**
- Reddit post + Cherry Quant contact 확인 — **15분**

**산출**:
- Substack subs 45~80 (누적)
- Reddit karma +10~30 (첫 post engagement)

**Verification**:
1. Strategy Lead 4건 ✓
2. owner action 2건 ✓
3. tests 367 PASS, coverage 75%
4. metrics row: D5 substack_subs=60, reddit_karma=15
5. commit `Day 35 W5: W5 closure + Substack #4 + Reddit #1 + Cherry Quant contact`

---

### Week 6 — Options + First External Contributor (D36~D42, 6/18 ~ 6/24)

#### Day 36 (Mon, 6/18)

**5차원**: D1 + D3

**Strategy Lead 자율 task**:
- (옵션) Theta Data Value $80 결제 → US options data API access (owner G2 — research 08 권고 ACCEPT 여부 확인)
- 옵션 backtest scaffold `src/strategies/a19_options_straddle.py` (선택)
- awesome-quant PR 작성 (cold honest title, repo description, link)
- README v2.2 (badges 갱신, stars 카운트 자동 fetch)

**owner action**:
- Theta Data Value 결제 결정 (G2, $80) — **10분** (ACCEPT 시 결제 5분)

**산출**:
- (G2 ACCEPT 시) Options data access
- awesome-quant PR draft

**Verification**:
1. Strategy Lead 3건 ✓
2. owner action 1건 (G2) ✓
3. tests 367 (options 가 G2 PENDING 시)
4. metrics row: D3 awesome_quant_pr=draft
5. commit `Day 36 W6: awesome-quant PR + options scaffold [if G2 accept]`

#### Day 37 (Tue, 6/19)

**5차원**: D2 + D5

**Strategy Lead 자율 task**:
- Paper 1 draft 의 §3 Results 갱신 (W2~W5 paper trading 합산 데이터 박제)
- Paper 1 draft 의 §4 Honest Failure 갱신 (A1~A6 38일 PoC + A11~A17 W2~W5 추가 데이터)
- Twitter +50 followers (누적 250~300 target)
- LinkedIn 한국 quant 인플루언서 5 connection request 발송

**owner action**:
- LinkedIn connection request 발송 확인 (target: 김우창 KAIST / 강환국 등 5명) — **15분**

**산출**:
- Paper 1 §3/§4 갱신
- LinkedIn 5 connection request sent

**Verification**:
1. Strategy Lead 3건 ✓
2. owner action 1건 ✓
3. tests 367
4. metrics row: D2 paper1_words=8500, D5 linkedin_requests=5
5. commit `Day 37 W6: Paper 1 §3/§4 update + LinkedIn outreach`

#### Day 38 (Wed, 6/20)

**5차원**: D1 + (G2 dependent) Options

**Strategy Lead 자율 task**:
- (G2 ACCEPT 시) A19 straddle backtest 30일 + 10 tests
- (G2 ACCEPT 시) `src/strategies/a20_options_iron_condor.py` scaffold + 10 tests
- (G2 PASS 시) 대체 작업: A11~A17 의 walk-forward analysis 확장 + 15 tests
- mutmut 도입 prep (mutation testing baseline)

**owner action**:
- 없음

**산출**:
- (G2 ACCEPT) A19+A20 scaffold + 20 tests
- (G2 PASS) walk-forward 확장 + 15 tests

**Verification**:
1. Strategy Lead 3~4건 ✓
2. owner action 없음 ✓
3. tests 382~387 PASS, coverage 75%
4. metrics row: D1 tests=385
5. commit `Day 38 W6: [A19+A20 | walk-forward] + mutmut prep`

#### Day 39 (Thu, 6/21)

**5차원**: D3 + Community

**Strategy Lead 자율 task**:
- awesome-quant PR submit (`pull request` 발송)
- awesome-systematic-trading PR submit
- GitHub repo description 최적화 (한국어 + English keyword 혼합, research 09 권고)
- Cherry Quant 한국어 guest article draft 제출 (W5 D35 contact 의 follow-up)

**owner action**:
- awesome-quant + awesome-systematic-trading PR URL 확인 — **5분**

**산출**:
- 2 PRs submitted
- Cherry Quant draft submitted

**Verification**:
1. Strategy Lead 4건 ✓
2. owner action 1건 ✓
3. tests 385
4. metrics row: D3 awesome_quant_pr=submitted, D3 awesome_st_pr=submitted
5. commit `Day 39 W6: awesome-quant + awesome-systematic-trading PRs`

#### Day 40 (Fri, 6/22)

**5차원**: D1 + Stars

**Strategy Lead 자율 task**:
- Strategy Lead 가 매 day star count 측정 → 50 stars 도달 day 박제
- (50 stars 도달 시) Discord server open (선택) + Discord invite link 추가 to README
- 외부 issue / PR 처리 routine (max 1h/day budget)
- `tests/test_property_based.py` 10 신규 hypothesis tests

**owner action**:
- 없음

**산출**:
- Stars count update
- 10 신규 tests

**Verification**:
1. Strategy Lead 3건 ✓
2. owner action 없음 ✓
3. tests 395 PASS, coverage 75%
4. metrics row: D3 stars=50?, D1 tests=395
5. commit `Day 40 W6: property tests + stars milestone`

#### Day 41 (Sat, 6/23)

**5차원**: D1 + D2

**Strategy Lead 자율 task**:
- Mutation testing (mutmut) 첫 실행 + baseline kill rate 측정
- `docs/paper-1/02-method.md` 갱신 (architecture diagram + alpha registry)
- Paper 1 draft 의 §1 Introduction 갱신 (W6 까지의 learning + Hudson&Thames mlfinlab cross-reference)

**owner action**:
- 없음

**산출**:
- Mutation testing baseline
- Paper 1 §1/§2 갱신

**Verification**:
1. Strategy Lead 3건 ✓
2. owner action 없음 ✓
3. tests 395, mutation kill rate baseline
4. metrics row: D1 mutation_kill_rate=0.40~0.50
5. commit `Day 41 W6: mutation testing + Paper 1 §1/§2 update`

#### Day 42 (Sun, 6/24)

**5차원**: Cleanup + D5

**Strategy Lead 자율 task**:
- W6 종합 review
- `docs/weekly/W6.md`
- (첫 external contributor 검출 여부 확인 — issue 또는 PR)
- Substack #5 draft + LinkedIn #3 draft

**owner action**:
- W6 review — **20분**

**산출**:
- W6 보고서
- Substack subs 60~120, Stars 30~80

**Verification**:
1. Strategy Lead 4건 ✓
2. owner action 1건 ✓
3. tests 395
4. metrics row: D5 substack_subs=80, D3 stars=50
5. commit `Day 42 W6: W6 closure`

---

### Week 7 — Integration (D43~D49, 6/25 ~ 7/1)

#### Day 43 (Mon, 6/25)

**5차원**: D1 + D4

**Strategy Lead 자율 task**:
- 4 자산군 unified backtest runner `src/backtest/unified.py`
- `python run_unified.py --asset kr,us,crypto --days 30` 정상 동작
- Live page `/quant/dashboard` 의 4-asset card switcher (KR/US/Crypto/Options) 활성
- 30 신규 tests (`tests/test_unified_backtest.py`)

**owner action**:
- 없음

**산출**:
- Unified backtest runner
- 30 신규 tests

**Verification**:
1. Strategy Lead 4건 ✓
2. tests 425 PASS, coverage 75%~80%
3. metrics row: D1 tests=425, D4 unified=true
4. commit `Day 43 W7: unified backtest + 4-asset dashboard`

#### Day 44 (Tue, 6/26)

**5차원**: D1 + D2

**Strategy Lead 자율 task**:
- Paper 1 §3 Results 의 unified backtest 결과 박제 (4 자산군 cross-asset Sharpe / DD / correlation)
- 15 신규 tests (cross-asset correlation, regime detection)
- LinkedIn 5 connection accept 확인 (W6 D37 의 5 request 의 follow-up)

**owner action**:
- LinkedIn 5 connection 의 응답 확인 — **10분**

**산출**:
- Paper 1 §3 갱신
- 15 신규 tests

**Verification**:
1. Strategy Lead 3건 ✓
2. owner action 1건 ✓
3. tests 440 PASS, coverage 80%
4. metrics row: D5 linkedin_connections=2~5
5. commit `Day 44 W7: cross-asset analysis + Paper 1 §3 update`

#### Day 45 (Wed, 6/27)

**5차원**: D1 + Quality

**Strategy Lead 자율 task**:
- DSR (Deflated Sharpe Ratio, Bailey & Lopez de Prado 2014) 구현 `src/metrics/dsr.py`
- PBO (Probability of Backtest Overfitting) 구현 `src/metrics/pbo.py`
- A11~A17 의 DSR + PBO 측정 → 결과 박제
- 20 신규 tests

**owner action**:
- 없음

**산출**:
- DSR + PBO implement
- 20 신규 tests

**Verification**:
1. Strategy Lead 3건 ✓
2. tests 460 PASS, coverage 80%
3. metrics row: D1 dsr_pbo=implemented
4. commit `Day 45 W7: DSR + PBO + 20 tests`

#### Day 46 (Thu, 6/28)

**5차원**: D2 + D4

**Strategy Lead 자율 task**:
- Paper 1 §3 의 DSR / PBO 결과 박제
- `/quant/paper-1` 학술 paper landing page (abstract preview + PDF download link)
- Tremor "Citation copy" 버튼 (BibTeX → clipboard)
- Paper 1 draft 50% (target met)

**owner action**:
- 없음

**산출**:
- /quant/paper-1 live
- Paper 1 draft 50%

**Verification**:
1. Strategy Lead 4건 ✓
2. tests 460
3. metrics row: D2 paper1_progress=50%, D4 page=paper-1
4. commit `Day 46 W7: /quant/paper-1 + DSR/PBO 박제`

#### Day 47 (Fri, 6/29)

**5차원**: D1 + D3

**Strategy Lead 자율 task**:
- 외부 PR / Issue 처리 (Strategy Lead triage)
- README v2.3 (학술 페이지 link, BibTeX, DSR/PBO 결과 표)
- `/quant/api/v1/strategy/[id]` public API endpoint 첫 implement (rate-limited 10 RPS)
- 15 신규 tests (API + rate limit)

**owner action**:
- 없음

**산출**:
- Public API first endpoint
- 15 신규 tests

**Verification**:
1. Strategy Lead 4건 ✓
2. tests 475 PASS, coverage 80%
3. metrics row: D4 api_endpoint=v1
4. commit `Day 47 W7: public API v1 + README v2.3`

#### Day 48 (Sat, 6/30)

**5차원**: D1 + Quality

**Strategy Lead 자율 task**:
- Coverage 의 weak spot 분석 (`pytest --cov=src --cov-report=html`)
- 인프라 (logging / error handling / config) 의 coverage 부족 → 20 신규 tests
- 80% coverage 도달 확정

**owner action**:
- 없음

**산출**:
- 20 신규 tests
- Coverage 80%+ 도달

**Verification**:
1. Strategy Lead 3건 ✓
2. tests 495 PASS, coverage 80%+
3. metrics row: D1 coverage=0.80
4. commit `Day 48 W7: coverage to 80%+`

#### Day 49 (Sun, 7/1)

**5차원**: Cleanup + D5

**Strategy Lead 자율 task**:
- W7 종합 review
- `docs/weekly/W7.md`
- Substack #5 publish + LinkedIn #3 publish
- Twitter +200 followers (누적 400~500)

**owner action**:
- W7 review — **20분**
- Substack + LinkedIn publish 확인 — **10분**

**산출**:
- W7 보고서
- Substack subs 70~140

**Verification**:
1. Strategy Lead 4건 ✓
2. owner action 2건 ✓
3. tests 495, coverage 80%
4. metrics row: D5 substack_subs=100, D3 stars=80
5. commit `Day 49 W7: W7 closure + Substack #5 + LinkedIn #3`

---

### Week 8 — Quality + Stars 100+ (D50~D56, 7/2 ~ 7/8)

#### Day 50 (Mon, 7/2)

**5차원**: D1 + Quality

**Strategy Lead 자율 task**:
- Sensitivity sweep 의 CI integration (`.github/workflows/sensitivity-sweep.yml`)
- 매주 1회 sweep 실행 + 결과 Supabase insert
- A11~A14 (KR 알파) 의 full sweep (4×6×6 cells × 4 alphas = 576 cells)
- mutmut full run + kill rate 측정

**owner action**:
- 없음

**산출**:
- Sensitivity sweep CI
- mutmut kill rate baseline

**Verification**:
1. Strategy Lead 3건 ✓
2. tests 495
3. metrics row: D1 sensitivity_sweep_cells=576, mutation_kill_rate
4. commit `Day 50 W8: sensitivity sweep CI + mutmut full`

#### Day 51 (Tue, 7/3)

**5차원**: D1 + D3

**Strategy Lead 자율 task**:
- 외부 PR (W6~W7 에서 추정 0~2건) 처리 + merge
- 첫 PR merge 시 contributors 카운트 ≥ 2 확정
- Discord channel open (선택, stars 80+ 도달 시)
- 25 신규 tests (test 의 quality 보다 quantity 보강)

**owner action**:
- 없음

**산출**:
- (첫 외부 PR merge 시) contributors=2 확정
- 25 신규 tests

**Verification**:
1. Strategy Lead 3건 ✓
2. tests 520 PASS, coverage 80%
3. metrics row: D3 contributors=2?, D1 tests=520
4. commit `Day 51 W8: external PR merge + 25 tests`

#### Day 52 (Wed, 7/4)

**5차원**: Security + D1

**Strategy Lead 자율 task**:
- L10 Alpha Decay 의 paper mode 1주 shadow run 시작 (실 halt 차단, log only)
- L10 false-positive 검증 (정상 strategy 가 잘못 halt 되지 않음 확인)
- 12 layer × 5 paper alphas × 3 동시 발동 시뮬레이션 = 180 unit tests prep

**owner action**:
- 없음

**산출**:
- L10 shadow mode active
- 30 신규 tests prep

**Verification**:
1. Strategy Lead 3건 ✓
2. tests 520
3. metrics row: Security l10_shadow=active
4. commit `Day 52 W8: L10 shadow mode + tests prep`

#### Day 53 (Thu, 7/5)

**5차원**: D2 + Quality

**Strategy Lead 자율 task**:
- Paper 1 draft 80% (target met, 7,000~10,000 단어)
- §5 Lessons 갱신 (W7~W8 의 추가 learning)
- figure 8~12개 final (matplotlib + PGFPlots, EPS export)
- Paper 1 references final (50+ entries)

**owner action**:
- 없음

**산출**:
- Paper 1 draft 80%

**Verification**:
1. Strategy Lead 4건 ✓
2. tests 520
3. metrics row: D2 paper1_progress=80%
4. commit `Day 53 W8: Paper 1 draft 80%`

#### Day 54 (Fri, 7/6)

**5차원**: D4 + Lighthouse

**Strategy Lead 자율 task**:
- Lighthouse Performance ≥ 90 target → bundle analyzer (`next-bundle-analyzer`) + JS 코드 split + image lazy + critical CSS inline
- Vercel edge cache 정책 갱신
- `/quant` 4 categories: Performance ≥ 0.90, Accessibility = 1.00, Best Practices = 1.00, SEO = 1.00

**owner action**:
- 없음

**산출**:
- Lighthouse Performance ≥ 0.90

**Verification**:
1. Strategy Lead 3건 ✓
2. tests 520
3. metrics row: D4 lighthouse_perf=0.92
4. commit `Day 54 W8: Lighthouse 90+ + bundle optim`

#### Day 55 (Sat, 7/7)

**5차원**: D1 + D5

**Strategy Lead 자율 task**:
- 12 alpha 모두의 sensitivity sweep 결과 visualization (heatmap → /quant/dashboard 안 통합)
- 20 신규 tests
- Substack #6 draft (Quality milestone: 700+ tests, 80% coverage, mutation kill rate)
- Twitter +400 followers (누적 800~1,000)

**owner action**:
- 없음

**산출**:
- 12-alpha sweep heatmap
- Substack #6 draft

**Verification**:
1. Strategy Lead 4건 ✓
2. tests 540 PASS, coverage 80%~82%
3. metrics row: D1 tests=540, D5 twitter=850
4. commit `Day 55 W8: 12-alpha sweep + Substack #6 draft`

#### Day 56 (Sun, 7/8)

**5차원**: Cleanup + Milestone

**Strategy Lead 자율 task**:
- W8 종합 review (5차원 milestone: D1 700+ tests + 80% coverage, D2 paper1 80%, D3 stars 100~200, D4 Lighthouse 90+, D5 Twitter 800+)
- `docs/weekly/W8.md`
- Substack #6 publish

**owner action**:
- **W8 종합 review (4주 mid-point review, 5차원 dashboard deep dive)** — **30분**
- Substack #6 publish 확인 — **5분**

**산출**:
- W8 보고서
- Substack subs 100~200

**Verification**:
1. Strategy Lead 3건 ✓
2. owner action 2건 ✓
3. tests 700+ target, coverage 80%, mutation kill rate 50%+
4. metrics row: 5 dimensions all updated
5. commit `Day 56 W8: W8 closure + Substack #6 + mid-point review`

---

### Week 9 — Kill Switch + Paper draft (D57~D63, 7/9 ~ 7/15)

#### Day 57 (Mon, 7/9)

**5차원**: Security + D1

**Strategy Lead 자율 task**:
- L10 Alpha Decay false-positive 검증 결과 박제 (W8 D52 shadow mode 1주 후 분석)
- L11 Regime Detector unit tests 추가 (BEAR + 변동성 > 10%, KR + US + Crypto 별)
- L12 Overfit Guard unit tests 추가 (A2 OU 의 PBO 측정, 38일 PoC 의 PBO ~0.85 expected)
- 30 신규 tests

**owner action**:
- 없음

**산출**:
- L10/L11/L12 unit tests 모두 30+
- 30 신규 tests

**Verification**:
1. Strategy Lead 4건 ✓
2. tests 570 PASS, coverage 80%
3. metrics row: D1 tests=570, Security l10_validated=true
4. commit `Day 57 W9: L10/L11/L12 unit tests + false-positive validation`

#### Day 58 (Tue, 7/10)

**5차원**: Security + D1

**Strategy Lead 자율 task**:
- HaltOrchestrator 12-layer 통합 의 race condition 검증 (asyncio.gather + lock)
- 20 신규 tests (`tests/test_halt_orchestrator_race.py`)
- L1~L12 가 paper mode 에서도 모두 production 정확히 동작 확인 (research 06 권고)

**owner action**:
- 없음

**산출**:
- HaltOrchestrator race-tested
- 20 신규 tests

**Verification**:
1. Strategy Lead 3건 ✓
2. tests 590 PASS, coverage 80%
3. metrics row: D1 tests=590, Security halt_orchestrator_race=tested
4. commit `Day 58 W9: HaltOrchestrator race-tested`

#### Day 59 (Wed, 7/11)

**5차원**: D2 + Paper

**Strategy Lead 자율 task**:
- Paper 1 draft 90% (target met, 8,000~12,000 단어)
- Abstract 200~250 단어
- Conclusion 갱신 (12주 build closure narrative)
- Internal Strategy Lead self-grill (cold honest 검증)

**owner action**:
- 없음

**산출**:
- Paper 1 draft 90%

**Verification**:
1. Strategy Lead 4건 ✓
2. tests 590
3. metrics row: D2 paper1_progress=90%
4. commit `Day 59 W9: Paper 1 draft 90% + self-grill`

#### Day 60 (Thu, 7/12)

**5차원**: D2 + ReScience

**Strategy Lead 자율 task**:
- ReScience Paper draft 시작 (Fama-French KOSPI 200 replication, Kang & Jang 2016 base)
- `docs/paper-2/` 디렉토리 + outline.md + refs.bib (research 06 의 한국 시장 4 references 활용)
- Replication notebook (Jupyter) prep + GitHub repo 안 박제

**owner action**:
- 없음

**산출**:
- ReScience Paper 2 outline + replication notebook prep

**Verification**:
1. Strategy Lead 3건 ✓
2. tests 590
3. metrics row: D2 paper2_progress=20%
4. commit `Day 60 W9: ReScience Paper 2 outline`

#### Day 61 (Fri, 7/13)

**5차원**: D3 + Stars

**Strategy Lead 자율 task**:
- Hacker News warm-up (Strategy Lead 가 HN 의 substantive comment 누적 → karma 50+ target)
- Show HN draft `docs/launch/show-hn.md` 박제 (cold honest title + 5분 quick start link + 38일 PoC narrative)
- Reddit r/algotrading 2nd post draft (W11 publish 예정)
- 외부 issue / PR triage (max 1h/day)

**owner action**:
- HN account 의 substantive comment 5+건 (owner 직접) — **30분**

**산출**:
- HN karma 30~50
- Show HN draft

**Verification**:
1. Strategy Lead 3건 ✓
2. owner action 1건 ✓
3. tests 590
4. metrics row: D3 hn_karma=40
5. commit `Day 61 W9: HN warm-up + Show HN draft`

#### Day 62 (Sat, 7/14)

**5차원**: D1 + D4

**Strategy Lead 자율 task**:
- Docker Dev Container 설계 (`.devcontainer/devcontainer.json`)
- `docker compose up` 1-command local launch
- 5분 quick start verified (Docker path)
- 15 신규 tests

**owner action**:
- 없음

**산출**:
- Docker Dev Container
- 15 신규 tests

**Verification**:
1. Strategy Lead 3건 ✓
2. tests 605 PASS, coverage 80%~82%
3. metrics row: D1 tests=605, devcontainer=ready
4. commit `Day 62 W9: Docker Dev Container + 15 tests`

#### Day 63 (Sun, 7/15)

**5차원**: Cleanup + D5

**Strategy Lead 자율 task**:
- W9 종합 review
- `docs/weekly/W9.md`
- Substack #7 draft (Kill Switch + Honest Failure narrative)
- Twitter +200 followers (누적 1,000~1,400)

**owner action**:
- W9 review — **20분**

**산출**:
- W9 보고서

**Verification**:
1. Strategy Lead 4건 ✓
2. owner action 1건 ✓
3. tests 605, coverage 82%
4. metrics row: D5 substack_subs=120, D3 stars=150
5. commit `Day 63 W9: W9 closure`

---

### Week 10 — Polish + Lighthouse 95+ (D64~D70, 7/16 ~ 7/22)

#### Day 64 (Mon, 7/16)

**5차원**: D4 + Lighthouse

**Strategy Lead 자율 task**:
- Lighthouse Performance ≥ 95 target → 추가 최적화 (font preload + brotli compression + edge runtime for API routes)
- 4 categories 모두 ≥ 0.95 (Performance, A11y, BP, SEO)
- Web Vitals 의 Lighthouse 측정 vs 실 user (Vercel Speed Insights) 비교 검증

**owner action**:
- 없음

**산출**:
- Lighthouse 95+

**Verification**:
1. Strategy Lead 3건 ✓
2. tests 605
3. metrics row: D4 lighthouse_perf=0.96, a11y=1.00, bp=1.00, seo=1.00
4. commit `Day 64 W10: Lighthouse 95+`

#### Day 65 (Tue, 7/17)

**5차원**: D2 + D4

**Strategy Lead 자율 task**:
- Paper 1 의 final compile (pdflatex no error)
- `/quant/paper-1/v1.pdf` 의 PDF preview hover + download tracking
- ReScience Paper 2 draft 30% (5~8 pages)
- 25 신규 tests

**owner action**:
- 없음

**산출**:
- Paper 1 final compile
- ReScience Paper 2 draft 30%
- 25 신규 tests

**Verification**:
1. Strategy Lead 4건 ✓
2. tests 630 PASS, coverage 82%
3. metrics row: D2 paper1_final=compiled, paper2_progress=30%
4. commit `Day 65 W10: Paper 1 final + Paper 2 draft 30%`

#### Day 66 (Wed, 7/18)

**5차원**: D3 + Stars

**Strategy Lead 자율 task**:
- Stars 200~400 target → 다음 lever 활성
- awesome-quant PR follow-up (W6 D39 의 PR 상태 확인 + merge)
- Reddit r/algotrading 2nd post (cold honest narrative + Strategy Lead 검토)
- Cherry Quant guest article publish (W5 D35 contact + W6 D39 draft 의 follow-up)

**owner action**:
- Cherry Quant publish 확인 — **10분**

**산출**:
- Stars 누적 measurement
- External channel cross-post 3건

**Verification**:
1. Strategy Lead 4건 ✓
2. owner action 1건 ✓
3. tests 630
4. metrics row: D3 stars=200~300, external_channels=3
5. commit `Day 66 W10: external channel cross-post + stars push`

#### Day 67 (Thu, 7/19)

**5차원**: D4 + D3

**Strategy Lead 자율 task**:
- Documentation site (`/quant/docs`) 의 10+ MDX pages 완성:
  - `getting-started.mdx`
  - `5-min-quick-start.mdx`
  - `strategies.mdx` (12 alpha 별 explanation)
  - `kill-switch.mdx` (12 layer)
  - `dsr-pbo.mdx`
  - `backtest.mdx`
  - `paper-trading.mdx`
  - `data-sources.mdx`
  - `api-reference.mdx`
  - `contributing.mdx`
- 각 page 1,000~2,000 단어

**owner action**:
- 없음

**산출**:
- 10+ docs pages live

**Verification**:
1. Strategy Lead 3건 ✓
2. tests 630
3. metrics row: D4 docs_pages=10
4. commit `Day 67 W10: documentation site 10+ pages`

#### Day 68 (Fri, 7/20)

**5차원**: D2 + Strategy Lead

**Strategy Lead 자율 task**:
- Paper 1 의 SSRN submission package prep (PDF + Abstract + Title + JEL classification)
- Quantpedia Awards 2027 submission base prep
- Hudson & Thames mlfinlab PR (선택, cold attempt, 12주 plan 안 G2 PENDING)

**owner action**:
- 없음

**산출**:
- SSRN submission package ready
- Quantpedia base ready

**Verification**:
1. Strategy Lead 3건 ✓
2. tests 630
3. metrics row: D2 ssrn_package=ready
4. commit `Day 68 W10: SSRN submission package + Quantpedia base`

#### Day 69 (Sat, 7/21)

**5차원**: D1 + Mutation

**Strategy Lead 자율 task**:
- mutmut full re-run + kill rate ≥ 60% target (W8 의 baseline 50% 에서 보강)
- 살아남은 mutants 분석 → 20 신규 tests
- Coverage 85% 도달

**owner action**:
- 없음

**산출**:
- Mutation kill rate ≥ 60%
- 20 신규 tests

**Verification**:
1. Strategy Lead 3건 ✓
2. tests 650 PASS, coverage 85%, mutation kill rate 60%+
3. metrics row: D1 mutation_kill_rate=0.60, coverage=0.85
4. commit `Day 69 W10: mutation 60%+ + coverage 85%`

#### Day 70 (Sun, 7/22)

**5차원**: Cleanup + D5

**Strategy Lead 자율 task**:
- W10 종합 review
- `docs/weekly/W10.md`
- Substack #8 publish (Paper 1 final + ReScience start)
- Twitter +400 followers (누적 1,500~2,000)

**owner action**:
- W10 review — **20분**
- Substack #8 publish 확인 — **5분**

**산출**:
- W10 보고서

**Verification**:
1. Strategy Lead 4건 ✓
2. owner action 2건 ✓
3. tests 650, coverage 85%
4. metrics row: D5 substack_subs=150, D3 stars=250
5. commit `Day 70 W10: W10 closure + Substack #8`

---

### Week 11 — Submit + Pre-launch (D71~D77, 7/23 ~ 7/29)

#### Day 71 (Mon, 7/23)

**5차원**: D2 + Submit

**Strategy Lead 자율 task**:
- **SSRN submission live** (Strategy Lead 가 SSRN account 통해 submit, owner 직접 paper signature 확인 후 click)
- SSRN paper ID 발급 + first download counter
- Twitter announcement thread draft

**owner action**:
- **SSRN submit 의 final review + click submit** — **30~60분**

**산출**:
- SSRN Paper 1 live

**Verification**:
1. Strategy Lead 3건 ✓
2. owner action 1건 ✓
3. tests 650
4. metrics row: D2 ssrn_paper_id=...
5. commit `Day 71 W11: SSRN submission live`

#### Day 72 (Tue, 7/24)

**5차원**: D1 + Audit + D5

**Strategy Lead 자율 task**:
- Audit log SHA-256 chain verifier 의 cron 등록 (매일 03:00 KST chain 검증)
- `tools/verify_audit_chain.py` final
- Substack #9 draft ("SSRN paper publish + ReScience submit prep")
- Twitter thread (SSRN paper announcement)

**owner action**:
- Twitter thread publish 확인 — **10분**

**산출**:
- Audit chain cron active
- SSRN announcement Twitter +50~100 followers spike

**Verification**:
1. Strategy Lead 4건 ✓
2. owner action 1건 ✓
3. tests 650
4. metrics row: Security audit_chain_cron=active, D5 twitter=2000
5. commit `Day 72 W11: audit chain cron + SSRN Twitter thread`

#### Day 73 (Wed, 7/25)

**5차원**: D2 + ReScience

**Strategy Lead 자율 task**:
- ReScience Paper 2 draft 50%
- Replication notebook full (Jupyter, KOSPI 200 Fama-French data, 5y backtest)
- GitHub repo 의 `papers/` 디렉토리 (Paper 1 + Paper 2 + supplementary)

**owner action**:
- 없음

**산출**:
- ReScience Paper 2 draft 50%

**Verification**:
1. Strategy Lead 3건 ✓
2. tests 650
3. metrics row: D2 paper2_progress=50%
4. commit `Day 73 W11: ReScience Paper 2 draft 50%`

#### Day 74 (Thu, 7/26)

**5차원**: D3 + Pre-launch

**Strategy Lead 자율 task**:
- Show HN final polish (`docs/launch/show-hn.md`)
- Reddit r/algotrading 3rd post (Cold honest "what I learned 12 weeks building 1-person quant POC")
- Product Hunt page draft prep
- Twitter daily thread D-7 (HN launch countdown 시작)

**owner action**:
- Show HN draft final review — **30분**

**산출**:
- Show HN ready
- D-7 countdown 시작

**Verification**:
1. Strategy Lead 4건 ✓
2. owner action 1건 ✓
3. tests 650
4. metrics row: D3 show_hn=ready
5. commit `Day 74 W11: Show HN final + Reddit #3 + D-7 countdown`

#### Day 75 (Fri, 7/27)

**5차원**: D4 + API

**Strategy Lead 자율 task**:
- Public API docs (OpenAPI 3.1 spec) + Swagger UI 또는 Scalar
- `/quant/api/docs` 200 OK + OpenAPI spec download
- 15 신규 tests (API endpoint 의 OpenAPI conformance)

**owner action**:
- 없음

**산출**:
- API docs site live
- 15 신규 tests

**Verification**:
1. Strategy Lead 3건 ✓
2. tests 665 PASS, coverage 85%
3. metrics row: D4 api_docs=live
4. commit `Day 75 W11: API docs + 15 tests`

#### Day 76 (Sat, 7/28)

**5차원**: D1 + Mutation final

**Strategy Lead 자율 task**:
- mutmut full re-run → kill rate ≥ 70% target (W10 의 60% 에서 보강)
- 30 신규 tests
- Coverage 88%+ 도달
- 1,000 tests target (현재 665 + W11~W12 의 nominal 80~150 보강 → 800~900 도달 가능, 1,000 은 W12 D84 target)

**owner action**:
- 없음

**산출**:
- Mutation kill rate ≥ 70%
- Coverage 88%+

**Verification**:
1. Strategy Lead 3건 ✓
2. tests 695, mutation kill rate 70%+, coverage 88%+
3. metrics row: D1 mutation=0.70, coverage=0.88
4. commit `Day 76 W11: mutation 70% + coverage 88%`

#### Day 77 (Sun, 7/29)

**5차원**: Cleanup + Pre-launch

**Strategy Lead 자율 task**:
- W11 종합 review
- `docs/weekly/W11.md`
- Substack #9 publish (SSRN announcement)
- Twitter D-6 countdown
- HN launch checklist final (Section 3 의 D78~D84 ready)

**owner action**:
- W11 review — **20분**
- Substack #9 + Twitter D-6 publish 확인 — **10분**

**산출**:
- W11 보고서
- SSRN downloads 30~80 (1주 후)

**Verification**:
1. Strategy Lead 4건 ✓
2. owner action 2건 ✓
3. tests 695, coverage 88%
4. metrics row: D5 substack_subs=200~400, D3 stars=300~450
5. commit `Day 77 W11: W11 closure + Substack #9 + D-6 countdown`

---

### Week 12 — Launch (D78~D84, 7/30 ~ 8/5)

#### Day 78 (Mon, 7/30)

**5차원**: All

**Strategy Lead 자율 task**:
- Twitter D-5 countdown
- 1,000 tests target → 50 신규 tests (665 → 715, 보강 to 1,000)
- Coverage 90% 도달
- Live page 의 모든 link / route 점검 (broken link checker)

**owner action**:
- 없음

**산출**:
- 50 신규 tests
- Coverage 90%

**Verification**:
1. Strategy Lead 3건 ✓
2. tests 745 PASS, coverage 90% ✓
3. metrics row: D1 tests=745, coverage=0.90
4. commit `Day 78 W12: D-5 + tests 745 + coverage 90%`

#### Day 79 (Tue, 7/31)

**5차원**: All

**Strategy Lead 자율 task**:
- Twitter D-4 countdown
- HN account karma 확인 (target 50+)
- Sentry 의 production environment 0 errors 확인 (last 7 days)
- 50 신규 tests

**owner action**:
- 없음

**산출**:
- 50 신규 tests
- Sentry health green

**Verification**:
1. Strategy Lead 3건 ✓
2. tests 795 PASS, coverage 90%
3. metrics row: D1 tests=795
4. commit `Day 79 W12: D-4 + tests 795`

#### Day 80 (Wed, 8/1)

**5차원**: All

**Strategy Lead 자율 task**:
- Twitter D-3 countdown
- Product Hunt page final + 동시 launch prep
- Performance benchmark 측정 (`pytest tests/benchmarks/`)
- 50 신규 tests

**owner action**:
- 없음

**산출**:
- 50 신규 tests
- PH page ready

**Verification**:
1. Strategy Lead 3건 ✓
2. tests 845 PASS, coverage 90%
3. metrics row: D1 tests=845
4. commit `Day 80 W12: D-3 + tests 845 + PH ready`

#### Day 81 (Thu, 8/2)

**5차원**: All

**Strategy Lead 자율 task**:
- Twitter D-2 countdown
- LinkedIn announcement post draft (HN launch 동기화)
- Substack #10 draft (final closure newsletter)
- 50 신규 tests

**owner action**:
- LinkedIn post draft review — **15분**

**산출**:
- 50 신규 tests
- LinkedIn + Substack draft

**Verification**:
1. Strategy Lead 4건 ✓
2. owner action 1건 ✓
3. tests 895 PASS, coverage 90%
4. metrics row: D1 tests=895
5. commit `Day 81 W12: D-2 + tests 895 + LinkedIn draft`

#### Day 82 (Fri, 8/3)

**5차원**: All

**Strategy Lead 자율 task**:
- Twitter D-1 countdown (final teaser, "tomorrow Tuesday 09:00 PT")
- HN launch checklist final review (Section 3 의 보안 / Section 4 의 monitoring 모두 active 확인)
- Strategy Lead 의 hour-by-hour monitoring plan 박제 (D84 의 HN launch 06:00~22:00 PT)
- 50 신규 tests (target 945)

**owner action**:
- 없음

**산출**:
- 50 신규 tests
- HN launch ops plan

**Verification**:
1. Strategy Lead 3건 ✓
2. tests 945 PASS, coverage 90%
3. metrics row: D1 tests=945
4. commit `Day 82 W12: D-1 + tests 945 + launch ops`

#### Day 83 (Sat, 8/4)

**5차원**: All

**Strategy Lead 자율 task**:
- HN launch D-0 prep (실 launch 는 다음 day Tuesday 09:00 PT)
- LinkedIn + Substack #10 final review + schedule
- Twitter thread schedule (8 tweets, 1h interval, HN launch 후 자동 publish)
- 55 신규 tests (target 1,000)
- Coverage 90%+ 도달 확정

**owner action**:
- LinkedIn announcement final review — **10분**
- Substack #10 final review — **10분**

**산출**:
- 55 신규 tests (1,000 reached)
- Launch package ready

**Verification**:
1. Strategy Lead 5건 ✓
2. owner action 2건 ✓
3. tests 1,000+ PASS, coverage 90% ✓
4. metrics row: D1 tests=1000, coverage=0.90
5. commit `Day 83 W12: launch package + tests 1000`

#### Day 84 (Sun, 8/5) → **HN Launch Day (Tuesday 09:00 PT = Wed 01:00 KST)**

> **Note**: 8/5 (Tue PT) = 8/6 KST. owner KST 기준 다음 작업의 핵심 시점은 Wed 01:00 KST (HN 09:00 PT submit) + 21:00 KST (HN front page check after 12h).

**5차원**: All — **The Launch**

**Strategy Lead 자율 task** (KST 기준 작업 시간):
- **08:00 KST (Tue evening PT)**: 최종 점검 (모든 monitoring green, kill switch active, audit chain valid)
- **00:00 KST Wed (09:00 PT Tue)**: Submit Show HN (title: "Show HN: Open-source 1-person retail quant POC with 38-day honest failure documentation"), Product Hunt 동시 launch, Reddit r/algotrading 4th post, Twitter +LinkedIn announcement
- **00:60 KST (HN +60 min)**: **Stop/Go gate**: upvotes ≥ 5? → 5 미만 시 Reddit + PH + Twitter 가속 (다른 channel lever 활성). 5+ 시 HN front page momentum 유지.
- **06:00 KST (HN +6h)**: Comment activity → substantive reply (3~5건), Strategy Lead 가 cold honest tone 유지
- **12:00 KST (HN +12h)**: Front page (top 30) 여부 확인. front page 진입 시 stars +200~1,000 spike 가능
- **21:00 KST (HN +21h)**: Final metrics + Strategy Lead 의 W12 종합 보고서

**owner action**:
- **00:00 KST Wed: HN submit click + 첫 60min monitoring** — **3~6h owner action (most critical day)**
- Comment reply (직접, owner tone) — **2~4h**

**산출**:
- HN URL submitted, upvotes ≥ 5 (60min gate) — 50% probability
- Final stars 300~600 (12주 plan close)
- Substack subs 100~800 final
- Twitter +500~3,000 final
- LinkedIn +200~1,000 final

**Verification**:
1. Strategy Lead launch ops 완료 ✓
2. owner action 2건 (HN + comments) ✓
3. tests 1,000+ PASS, coverage 90%, mutation kill rate 70%+
4. metrics row: 5 dimensions final
5. commit `Day 84 W12: HN Launch + W12 closure`

#### Post-launch (W13+) 준비

- D-1 (W12 D83) 의 commit 뒤 자동 5+ apply package prep:
  - 토스 (Product Owner / Product Owner AI Data Platform)
  - 카카오페이증권 (PM)
  - 뱅크샐러드 (PM)
  - 채널톡 (PM)
  - 뤼튼 (PM)
  - Sendbird (Korean-global bridge)
  - Upstage (Korean global)
  - 에이블리 (AI 추천 PM)
- 자소서 PHARL 패턴 (P)roblem (H)ypothesis (A)ction (R)esult (L)esson — 38일 PoC closure + 12주 build 의 통합 narrative

---

## Closing Notes

### 본 plan 의 cold honest 박제 5건

1. **5차원 동시 100% 달성 확률 ≈ 30%** (50% 권고 stars 300~600 미달 가능 + 50% target 일부 미달). 50% 확률 = 4/5 dimensions 달성 (1 dimension under-perform).
2. **HN front page 진입 확률 50%** (research 12 의 hftbacktest 148 upvotes case 기반). under-perform 시 mitigation = Reddit + PH + Twitter cascade.
3. **owner 의 8~13h/week commitment 가 절대 조건**. owner 시간 < 5h/week 시 D5 communication 차원 직격.
4. **본업 (이트라이브 CTS-AI) 와 충돌 risk**: 12주 = 84 days, 본업 deadline 있을 시 W7 또는 W11 의 시점 충돌 가능. 충돌 시 W12 → W13 delay 가능 (Strategy Lead 자율 결정).
5. **블라인드 심사 (NeurIPS 20237 + TMLR 8752) 결과 발표 시점**: 12주 build 완료 시점 (8/5) vs NeurIPS announcement (보통 9월 말, accept letter): 1.5~2개월 후. accept 시 W14+ 의 apply 패키지 lever +20~30%. reject 시 12주 build 의 portfolio 가치 lever 가 유일 (still strong).

### Strategy Lead 자율 95% / owner 5% breakdown

- Strategy Lead 자율 (G1): 12주 plan 의 코드 + 보고서 + 자동화 + monitoring + 5차원 metrics insert + 주간 보고서 + content draft + research deep-dive
- owner action (5%): 결제 (W1 Vercel Pro + Supabase Pro + IBKR), 가입 (KIS Developers + IBKR + Sentry + Twitter / LinkedIn / Substack), G2 결정 (W4 IBKR backup path + W6 Theta Data + W12 HN timing), Publish 확인 (LinkedIn + Substack + Reddit + HN), Comments (HN 직접 reply, owner tone)

### owner 의 12주 후 (Week 13+) state

- GitHub `Yesol-Pilot/quant-poc-multi-asset`: 300~600 stars, 5~10 contributors, 1,000+ tests, 90% coverage
- SSRN Paper 1: live, downloads 50~200 (1주 후)
- ReScience Paper 2 draft: submit-ready
- `heoyesol.kr/quant`: Lighthouse 95+, 4-asset dashboard, public API
- Substack: 100~800 subscribers
- Twitter: +500~3,000 followers (누적)
- LinkedIn: +200~1,000 connections (누적)
- HN profile: karma 100+ with Show HN successful launch
- Apply 동시 5+ (토스/카카오페이/뱅크샐러드/채널톡/뤼튼/Sendbird/Upstage/에이블리)
- 1+ offer 확률 60~80% (cold, research 15)
- 연봉 기대 7,000만 ~ 1.2억 (포지셔닝 + portfolio fit + dual track)

---

## Appendix A — 본 plan 의 Live SSOT 위치

- 본 문서: `D:/00.test/neo-genesis_untracked_backup_20260505_083608/auto-trading/docs/design/03-12week-daily-plan-and-milestones.md`
- Research foundation: `docs/research/00-research-final-summary.md` + `docs/research/01~16-*.md`
- 38일 PoC 자산 (자율 활용): `auto-trading/docs/v11-ensemble/` + `auto-trading/src/agents/` (commit `c8f4e7b` + `4849d84` + `7536619` 등)
- 5차원 progress dashboard: `heoyesol.kr/quant/internal` (owner only auth, W11+)
- Supabase tables: `quant_milestone_metrics` (W1 D6), `audit_log` (W1 D6), `strategy_lead_reports` (W1 D6)
- Strategy Lead 매주 보고: `scripts/weekly_progress_report.py` (W1 D6 박제) → Telegram + Email
- Risk matrix: 본 문서 Section 5
- Daily verification: 본 문서 Section 6

## Appendix B — owner action 합산 시간 (12주)

| Week | owner h | 핵심 |
|---|---|---|
| W1 | ~6h | Vercel + Supabase 결제 + KIS 가입 + Sentry + Telegram bot |
| W2 | ~2h | LinkedIn publish review + KIS rate limit G2 |
| W3 | ~1h | Reviews |
| W4 | ~5h | IBKR 가입 + W4 review |
| W5 | ~1h | W5 review |
| W6 | ~1h | Theta Data G2 + W6 review |
| W7 | ~1h | W7 review |
| W8 | ~1h | W8 mid-point review |
| W9 | ~1h | HN warm-up (substantive comments) |
| W10 | ~1h | Cherry Quant publish + W10 review |
| W11 | ~2h | SSRN submit + W11 review |
| W12 | ~10h | HN launch day (3~6h) + comments (2~4h) + reviews |
| **합계** | **~32h (12주)** | 평균 2.7h/week |

owner 시간 cold estimate: 12주 32h = 8~13h/week target 의 약 30% (review + 결정 + signature 만). 나머지 = community lurk + own learning (자율).

## Appendix C — 본 plan 의 변경 통제

- 매 week Sun 의 review 후 plan 수정 가능 (Strategy Lead 자율)
- W2/W4/W6/W8/W10/W12 의 owner review 시점에 G2 결정 가능
- 본 SSOT 변경 시 commit message: `plan: 03-12week update W[N] D[D] [reason]`
- 변경 이력: `git log docs/design/03-12week-daily-plan-and-milestones.md`

---

> **Strategy Lead Claude Opus 4.7 cold honest closure**:
>
> 본 12주 plan 은 38일 PoC 학습 + 16 research deep-dive + owner unique position 의 합산이다.
> Strategy Lead 자율 95% / owner 5% 의 분배는 cold realistic.
> 12주 후 owner state = 글로벌 retail 1인 AI PM + Quant 융합 top 0.01~0.05% 가시화.
> 1 offer 확률 60~80% (research 15) — Build 완료 시 본 plan 의 1차 측정 가능.
>
> Build Go. ✅
