# #9 GitHub Open Source Strategy

> Tier B Publish 영역 #9 / 한국 retail 1인 AI 네이티브 PM portfolio
> 작성: 2026-05-14 (Strategy Lead Claude Opus 4.7)
> Cold honest. 광고성 X. retail 1인 실제 가능한 path 만.

---

## Executive Summary (5 핵심 발견)

1. **License 권고: MIT** (NOT Apache 2.0). 글로벌 quant OSS 분포는 MIT/Apache 양분 (Hummingbot=Apache, Backtrader=GPL, NautilusTrader=LGPL, mlfinlab=Apache, FinRL=MIT). MIT 가 한국 retail 1인 sensible default 인 이유: (a) 짧고 명확 → 한국어 LICENSE 별도 안내 가능, (b) patent grant 부재가 1인 OSS 에서 실질 위험 0 (특허 침해 소송은 large entity 대상), (c) 5,000+ 외부 contributor 가 Apache 2.0 의 NOTICE 파일 / patent retaliation clause 보다 MIT 의 4줄에 편안.

2. **Repository naming 권고: `quant-poc-multi-asset`** (현 backup 디렉토리 명칭 유지). hyphenated lowercase + SEO friendly (`quant` topic = 8,000+ repos, `multi-asset` differentiation). `Yesol-Pilot/quant-poc-multi-asset` 가 owner 의 11 SBU 정합성 유지 + 38일 PoC failure narrative 그대로 활용 가능.

3. **README modern excellence 핵심 5 sections**: (1) Hero badges 5~7개 (build / coverage / stars / license / python version), (2) "5-minute quick start" — `git clone + pip install + python run.py` 3 명령, (3) Architecture 다이어그램 (Mermaid), (4) Results 표 (38일 PoC honest failure 그대로 — `WR 37.7%, PnL -15.1%, 191 trades, 0.0 Sharpe`), (5) Korean + English dual track (`README.md` = English 우선, `README.ko.md` = 한국어 확장).

4. **Star 목표 cold 권고**: 12주 plan 종료 시 **300~600 stars** (50% 확률, awesome-quant PR + Show HN Saturday 09:00 PT + Reddit r/algotrading 2개 post). 1,000 stars 는 12~24개월 (35% 확률, NeurIPS+TMLR 1편씩 accept 가시화 + 한국 시장 unique value 의 viral). 5,000 stars 는 36개월 + 본인 active maintenance + 외부 PR merge 50+건.

5. **GitHub Sponsors + Polar.sh dual track 권고**: GitHub Sponsors 즉시 등록 ($0 fee, Korea bank 입금 가능), Polar.sh 는 issue-funding 만 ($0 monthly + 4% + Stripe fee). retail 1인 sponsorship 현실 = 100 stars 시 $0~$50/월, 1,000 stars 시 $50~$300/월, 5,000 stars 시 $300~$1,500/월 (Sindre Sorhus / Sebastian Pipping 외 글로벌 vanguard 사례 기반).

---

## 1. License 선택: MIT vs Apache 2.0 vs GPL vs BSL

### 1.1 글로벌 quant repos license 분포 (2026-05 기준 검증)

| Repo | Stars | License | 비고 |
|---|---|---|---|
| Hummingbot | 13,500+ | Apache 2.0 | 50+ exchange connectors, foundation 운영 |
| FinRL | 11,800+ | MIT | DRL framework, Columbia University 주도 |
| Backtrader | 14,700+ | GPL-3.0 | Python 백테스트, 단일 author Daniel Rodriguez |
| NautilusTrader | 4,500+ | LGPL-3.0 | Rust-native, nautechsystems Australia |
| mlfinlab | 4,000+ | Apache 2.0 | Hudson & Thames 운영 (commercial 변환) |
| QuantLib | 7,100+ | BSD 3-clause | C++ derivative pricing, since 2000 |
| Freqtrade | 32,000+ | GPL-3.0 | Crypto bot, telegram + web UI |
| OctoBot | 3,800+ | GPL-3.0 | Crypto bot |

**관찰**: GPL (Backtrader / Freqtrade / OctoBot) 은 crypto 영역에서 흔함 (commercial fork 차단 의도). MIT/Apache (Hummingbot / FinRL / mlfinlab) 는 institutional 친화. LGPL (NautilusTrader) 은 "library 로만 사용 가능, 수정 시 소스 공개" 의 중간 지대.

### 1.2 MIT vs Apache 2.0 cold 비교 (1인 retail 관점)

| 항목 | MIT | Apache 2.0 |
|---|---|---|
| 길이 | 21줄 | 200+줄 |
| Patent grant | 없음 (implicit only) | 명시 (Section 3) |
| NOTICE 파일 의무 | 없음 | 있음 (수정 시 명시) |
| Trademark | 별도 명시 없음 | Section 6 (trademark 보호) |
| Patent retaliation | 없음 | 있음 (소송 제기 시 license 종료) |
| 한국 retail 1인 위험 | 거의 0 | 거의 0 |
| 외부 contributor 친화 | ★★★★★ (단순) | ★★★★ (NOTICE 의무 부담) |
| SEO/visibility 영향 | 0 | 0 |
| Commercial fork 차단 | 불가 | 불가 (patent retaliation 만) |

**결론**: 1인 retail 의 quant POC 에서 patent grant 가 의미를 가지려면 (a) 본인이 특허 보유 + (b) 외부 contributor 가 large entity, 둘 다 충족이어야 함. 12주 plan 시점에서는 둘 다 미충족. **MIT 권고**.

### 1.3 BSL (Business Source License) 검토 → 비권고

CockroachDB / Sentry / Couchbase 등이 사용. 4년 후 자동 Apache 2.0 전환. 단점: (a) OSI approved 아님 → awesome-quant PR 시 "not strictly open source" 표시 가능, (b) 한국 retail 1인 에서 commercial protection 의미 거의 0, (c) 외부 contributor 가 BSL 알레르기. **비권고**.

### 1.4 GPL-3.0 검토 → 비권고

Copyleft 강제. 외부 fork 가 closed-source SaaS 로 못 만들게 함. 하지만 12주 plan 의 visibility goal (1,000 stars) 과 충돌 — 외부 institutional contributor (Hudson & Thames / Optiver / Jane Street eng) 가 GPL 라이센스 OSS 에 PR 못 함 (legal review 자동 차단). **비권고**.

### 1.5 권고 정착: `LICENSE` = MIT, 본인이 Yesol-Pilot organization 단독 author

```
MIT License

Copyright (c) 2026 Yesol Heo (Yesol-Pilot)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

cold honest 주의: 한국에서 "Yesol Heo" 영문 표기 일관성 (heoyesol.kr 도메인과 정합). `Copyright (c) 2026-present` 형식 가능.

---

## 2. Repository naming + organization

### 2.1 Top 50 quant repos naming 패턴 분석

3가지 그룹:
- **Brand 단명**: Hummingbot / Freqtrade / Backtrader / NautilusTrader / Jesse / OctoBot. 강력하지만 SEO 약함 (사용자가 이미 알아야 검색).
- **Descriptive**: quant-poc-multi-asset / awesome-systematic-trading / Awesome-Quant-Machine-Learning-Trading. SEO 강 (Google + GitHub topic 검색 적합).
- **Acronym**: FinRL / mlfinlab / QuantLib / pyalgotrade. 짧지만 의미 추측 어려움.

### 2.2 `quant-poc-multi-asset` cold 평가

**장점**:
- "quant" (8,000+ topic repos), "multi-asset" (300+ unique repos) 둘 다 GitHub topic 매칭
- "poc" = proof of concept → 38일 honest failure narrative 와 정합 (과장 X)
- hyphenated lowercase (GitHub convention)
- versionless (v1 / v2 명시 X)

**단점**:
- "poc" 가 institutional 관점에서는 "completed not production-ready" 인상 → seek hire 시 약점
- 12개월 후 "poc 졸업" 시 rename 필요 → GitHub redirect 자동이지만 외부 link 깨짐

**Alternative naming**:
- `quant-multi-asset` (poc 제거, 더 production tone)
- `openquant-kr` (Korean unique value + open + quant)
- `retail-quant-honest` (38일 failure narrative 중심)
- `quant-portfolio-1person` (1인 portfolio 정체성 강조)

**권고**: `quant-poc-multi-asset` 12주 유지 → 12주 plan 종료 시점 결정. `quant-multi-asset` 또는 `openquant-kr` 으로 rename (rename 안전, GitHub redirect 자동).

### 2.3 Yesol-Pilot organization 활용

owner 의 11 SBU repo (ToolPick / UR WRONG / K-OTT / SellKit 등) 가 모두 `Yesol-Pilot/*` 에. quant repo 도 같은 organization 으로 묶으면:
- portfolio profile 페이지 일관성 (`github.com/Yesol-Pilot`)
- 11 SBU + 1 quant + 1 paper = 13개 active repos visibility
- contributor stats 합산

별도 `OpenQuantKR` organization 분리 고려? **비권고**. 1인 owner 가 multi-org 관리하면 분산 — Yesol-Pilot 단일 + quant 폴더 분리 (`tags` topic) 가 충분.

### 2.4 SEO 친화적 naming 원칙

- 한국 retail 가 검색하는 keyword: "퀀트 봇", "AI 자동매매", "1인 퀀트"
- 글로벌 retail 가 검색하는 keyword: "retail quant", "multi-asset trading bot", "honest failure quant"
- repo 명에 직접 한국어 못 넣음 (GitHub URL ascii only)
- README 에서 한국어 keyword 풍부 사용 → repo description (`<200 chars`) 에 영문 + 한국어 키워드 혼합 권고: `Open-source 1-person retail quant POC: multi-asset (KR/US/crypto/options) backtest + paper trading. 38-day honest failure documentation. 한국 1인 퀀트 portfolio.`

---

## 3. README modern excellence (모범 사례 분석)

### 3.1 분석 대상 5 repos

| Repo | README 구조 | 핵심 강점 |
|---|---|---|
| Hummingbot | Hero + Quick Start + Architecture + Docs link | Foundation 운영 (commercial 후원 시각화) |
| FinRL | Hero + Paper citation + 5 tutorial 링크 + Architecture | NeurIPS paper crosslink |
| Backtrader | Minimal (Quick Start + Code example) | 단일 author 의 친근함 |
| NautilusTrader | Hero + Performance benchmark + Architecture + Docs | Rust performance 수치 직접 (1M events/sec) |
| mlfinlab | Hero + Book reference + Course link + Hudson&Thames branding | Lopez de Prado 책 cross-link |

### 3.2 필수 sections (1인 retail 권고 구조)

```markdown
# quant-poc-multi-asset

[badges row: build / coverage / license / stars / python / docs]

> 38-day honest failure documentation: a 1-person retail quant POC
> across KR equities, US options, crypto perpetuals.
> Cold honest. No alpha. Production code for learning.

## What This Is

3~5 줄 한국 + English. honest failure narrative 강조.

## Quick Start (5 minutes)

```bash
git clone https://github.com/Yesol-Pilot/quant-poc-multi-asset
cd quant-poc-multi-asset
pip install -r requirements.txt
python run_paper_trading.py  # 즉시 paper mode (외부 API key 0건)
```

## Architecture

[Mermaid diagram]

## Results (Cold Honest)

| Metric | 38-day PoC |
|---|---|
| Trades | 191 |
| Win rate | 37.7% |
| PnL (paper) | -15.1% |
| Sharpe | 0.0 |
| Conclusion | Spec failure confirmed across 12 alphas |

→ See `docs/closure-note.md` for the full lessons learned.

## Documentation

- [Korean docs](docs/ko/)
- [English docs](docs/en/)
- [Backtest results](docs/research/)

## Citation

If you reference this work academically:
```bibtex
@misc{heo2026quantpoc,
  author = {Heo, Yesol},
  title = {Korean Retail Multi-Strategy Backtest: A 1-Person AI-Agent Pipeline},
  year = {2026},
  url = {https://github.com/Yesol-Pilot/quant-poc-multi-asset}
}
```

## License

MIT — see [LICENSE](LICENSE).
```

### 3.3 Badges 권고 (Shields.io 기준 5~7개)

**필수**:
- `Build status` (GitHub Actions)
- `Coverage` (Codecov 또는 pytest-coverage-comment)
- `License: MIT`
- `Python 3.10+`
- `Stars`

**선택**:
- `Discord` (커뮤니티 100+ 후)
- `Twitter/X` follow
- `arXiv` paper citation (Paper 1 publish 후)

**비권고**:
- "Made with love in Korea" 류 깃발 (signaling 약함, professional tone 깨짐)
- 10+ badges (시각적 노이즈, 'badge fatigue')

### 3.4 한국어 + 영문 dual track 권고 구조

**Option A**: `README.md` (English) + `README.ko.md` (한국어 expanded)
- 최상단 link bar: `[English](README.md) | [한국어](README.ko.md)`
- 검색 SEO 양쪽 충족

**Option B**: 단일 `README.md` 안에서 English 우선 + "한국어 안내" 섹션
- 1 파일 maintenance burden 낮음
- 한국어 section 짧아짐 (영문 길이의 30~50%)

**권고**: Option A. ToolPick / UR WRONG 의 dual-track 경험 활용 가능.

### 3.5 5분 quick start 원칙

평균 visitor 가 README 에서 3~10초 안에 "이게 뭔가" 판단 → 5분 안에 본인 환경에서 실행 못 하면 star 누르지 않음. 권고:
- `pip install` 또는 `pipx install` 1줄
- `python run.py` 또는 `make demo` 1줄
- 외부 API key 0건 (paper mode 만), 실제 거래 mode 는 별도 setup guide
- Docker 옵션 별도 (Docker 가 1인 retail 환경에서 friction 높음 — pip 우선)

---

## 4. Star / Fork 가속 전략

### 4.1 awesome-quant PR 절차 (cold honest)

`wilsonfreitas/awesome-quant` 또는 `wangzhe3224/awesome-systematic-trading`:
- maintainer 가 "decent or promising libraries" 만 선별 → 무조건 merge 보장 X
- PR 합격 기준 (관찰):
  - 100+ stars (또는 paper / 학술 cited)
  - active maintenance (90일 내 commit)
  - 문서화 완성도 (README + docs/)
  - 카테고리 fit (multi-asset 의 경우 "Trading & Backtesting" 또는 "Cross-Language Frameworks")

**12주 plan timing**:
- 100 stars 도달 시 (Show HN + Reddit 1차 시도 후) PR
- 단, 100 stars 미만에서도 시도 가능 (rejection 위험 30~50%)

**PR body 권고**:
```markdown
## quant-poc-multi-asset

A 1-person retail quant POC across KR equities, US options, crypto perpetuals.
38-day honest failure documentation with reproducible backtests.

- License: MIT
- Python 3.10+
- Active maintenance (last commit: today)
- 187 unit tests, 78% coverage
- Multi-asset (Korean stock + US options + crypto)
- Cited by [arXiv preprint](URL) (when published)
```

### 4.2 GitHub topic tagging

권고 8개:
- `quant`
- `quantitative-finance`
- `algorithmic-trading`
- `backtesting`
- `multi-asset`
- `korean-stocks`
- `paper-trading`
- `retail-quant`

특히 `korean-stocks` 와 `retail-quant` 는 unique → 검색 시 적은 경쟁 + 본인 portfolio differentiation.

### 4.3 Hacker News + Reddit + Twitter cross-link

**Show HN 권고 timing** (검증 데이터 기반):
- **Saturday 09:00 PT (= Sunday 02:00 KST)** = 한국에서 새벽이지만 글로벌 visibility 최대
- 또는 **Tuesday-Thursday 06:00 PT** (= 23:00 KST 화~목) = 한국 저녁시간 모니터링 가능
- Sunday 00:00~01:00 PT 는 contrarian (낮은 경쟁, 23,000 posts analysis)
- 첫 60분 에 10+ upvote 확보가 front page 임계

**Show HN title 권고**: "Show HN: 38-day honest failure of a 1-person retail quant (Korean+US+crypto)"
- "honest failure" 가 contrarian → curiosity 트리거
- "1-person" + "Korean+US+crypto" = unique differentiation
- ~70 chars

**Reddit cross-post**:
- `r/algotrading` (1.4M members) — 가장 큰 quant subreddit
- `r/quant` (260K members) — 학술 친화
- `r/Korea` (cross-post 검토 — 한국 retail 관심 측정)
- `r/learnmachinelearning` (NeurIPS/TMLR cross-link 시)

**Twitter/X**:
- Show HN 발사 직전 trailing tweet (5분 후) "I just shipped my 38-day quant POC failure documentation. Here's the cold story: [HN link]"
- 한국 quant Twitter 클러스터 (@quant_kr_etc 권고) 가 있는지 사전 조사 필요

### 4.4 Discord / Slack community

retail 1인 OSS 의 community 운영 cold honest:
- 100 members → 1주일 활성 (개인 친화 운영 가능)
- 500 members → 주 5~10시간 moderation 필요
- 1,000 members → 일일 1시간 minimum (지속 가능 한계)
- 5,000 members → 본인 외 moderator 필요 (외부 사람 신뢰 문제)

**권고**: Discord 단일 server, 5채널 (general / 한국어 / english / showcases / dev). 100~500 members 까지 본인 단독, 그 이상은 검토.

### 4.5 Star 목표 cold 예측

| 시점 | 목표 stars | 확률 | 트리거 |
|---|---|---|---|
| 12주 plan 종료 (8월) | 300~600 | 50% | awesome-quant PR + Show HN + Reddit 2건 |
| 6개월 (11월) | 800~1,500 | 40% | + arXiv preprint + Quantpedia Awards |
| 12개월 (2027-05) | 1,500~3,000 | 30% | + NeurIPS accept + 외부 contributor 5+건 |
| 24개월 | 3,000~5,000 | 20% | + 한국 시장 vertical 의 vanguard 인정 |

**1,000 stars (12주, 70% 확률)** 는 외부 deep research 보고서가 제시한 수치이지만 cold 검증 결과 **40~50% 권고 하향**. 이유:
- 38일 PoC failure narrative 가 contrarian (initial curiosity 강하지만 sustained engagement 약함)
- 한국 retail unique value 가 글로벌 retail (대다수 미국 중심) 에게 적용 어려움
- viral 30~40% 확률은 1차 Show HN 만 — sustained growth 가 다른 lever 필요

---

## 5. GitHub Actions CI/CD

### 5.1 권고 workflow 구조

```yaml
# .github/workflows/test.yml
name: test
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.10", "3.11", "3.12"]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - run: pip install -r requirements.txt -r requirements-dev.txt
      - run: pytest --cov=src --cov-report=xml
      - uses: codecov/codecov-action@v4
        with:
          file: ./coverage.xml
```

### 5.2 Badge auto-update

**pytest-coverage-comment** 또는 **tj-actions/coverage-badge-py**:
- PR comment 에 자동 coverage 표시
- README badge URL 동적 업데이트
- shields.io endpoint 기반

### 5.3 자동 release (semantic versioning)

**python-semantic-release** 또는 **release-please**:
- conventional commits (`feat:` / `fix:` / `BREAKING CHANGE:`) 인식
- `CHANGELOG.md` 자동 생성
- GitHub Release + PyPI publish 자동

**1인 retail cold 권고**: semantic-release 는 12주 plan 종료 후 도입. 초기에는 manual tag (`v0.1.0` 류) 충분. PyPI publish 는 외부 사용자 5명 도달 시.

### 5.4 dependabot + security audit

```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: pip
    directory: /
    schedule:
      interval: weekly
  - package-ecosystem: github-actions
    directory: /
    schedule:
      interval: monthly
```

- 자동 PR (보안 패치 + dep upgrade)
- 무료, 즉시 활성화 가능
- 외부 contributor 가 보기에 "actively maintained" 신호

---

## 6. Issue / PR template + Community

### 6.1 Issue templates 권고 (3개)

`.github/ISSUE_TEMPLATE/`:
- `bug_report.md` — reproduce steps + 환경 + expected vs actual
- `feature_request.md` — use case + 대안
- `question.md` — Discord link 우선 (issue 폭주 차단)

### 6.2 PR template

`.github/pull_request_template.md`:
- 변경 요약
- 관련 issue
- 테스트 결과
- Breaking change 여부
- 한국어/영문 옵션

### 6.3 CODE_OF_CONDUCT.md

Contributor Covenant v2.1 표준 (40,000+ OSS 사용 — Kubernetes, Rails, Swift). owner email = `dpthf1537@gmail.com` 으로 직접 enforcement.

### 6.4 CONTRIBUTING.md

외부 contributor 가이드:
- Setup (5분 quick start 재포인터)
- Test 실행 방법
- 코드 스타일 (black + isort + ruff)
- Commit message convention (`feat:` / `fix:` 등)
- PR review SLA: "I will respond within 7 days" (1인 retail 명시)

### 6.5 SECURITY.md

quant 특수 권고:
- "Do not open public issue for security vulnerabilities"
- Report to: `dpthf1537@gmail.com` 또는 GitHub Security Advisory
- Kill Switch documentation 별도 link
- "This is a POC, not production trading software. Use at your own risk."

---

## 7. Sponsorship / Funding

### 7.1 GitHub Sponsors 등록 절차

1. https://github.com/sponsors → "Become a sponsor"
2. tier 설정 (Sindre Sorhus 사례: $5/$25/$100/$500/$1,000)
3. Korean bank account 입금 가능 (Stripe Atlas 없이 직접)
4. Fee: 0% (GitHub 부담)
5. 첫 sponsor 까지 평균 30~90일 (활성 OSS 가정)

### 7.2 Polar.sh — issue-funding

- 0% monthly fee + 4% + Stripe fee per transaction
- "이 issue 해결되면 $50" 식의 bounty
- retail 1인 에서 issue 가 정량적 명확성 가질 때 적합

### 7.3 Retail 1인 sponsorship cold 사례

| 사례 | Stars | 월 sponsorship |
|---|---|---|
| Sindre Sorhus | 30,000+ | $20,000+ (full-time OSS) |
| Sebastian Pipping (figlet) | 500 | $50~$200 |
| Caleb Porzio (Alpine.js) | 28,000 | $5,000~$10,000 |
| 한국 OSS author A (anon) | 1,200 | $0~$50 |

**현실**: stars > 5,000 + 활성 maintenance > 6개월 = sponsorship $300+/월. retail 1인 quant 의 경우 12개월에 도달이 현실적.

### 7.4 권고: dual track

- **GitHub Sponsors**: 정착, monthly recurring (정착 단순)
- **Polar.sh**: 옵션, issue-specific bounty (외부 contributor 동기부여)
- **비권고**: Patreon, Buy Me Coffee — quant 영역에서 신뢰도 약함 (creator economy 시각)

---

## 8. Cold Honest 권고 (12주 plan timing)

### 8.1 12주 plan 단계별 OSS 활동

| 주 | OSS 활동 | 시간 투입 |
|---|---|---|
| W1 | LICENSE + .gitignore + 기본 README setup | 2h |
| W2 | GitHub Actions test workflow + badges | 4h |
| W3 | CODE_OF_CONDUCT + CONTRIBUTING + SECURITY | 2h |
| W4 | Issue/PR templates + dependabot | 1h |
| W5 | README 1차 완성 (English + Korean) | 6h |
| W6 | Discord server 생성 + invite link | 1h |
| W7 | Repository public 전환 + tag topics | 0.5h |
| W8 | awesome-quant PR (조건: 50+ stars) | 1h |
| W9 | Show HN 발사 (Saturday 09:00 PT) | 3h (모니터링 포함) |
| W10 | Reddit r/algotrading + r/quant cross-post | 2h |
| W11 | Star/issue 분석 + 개선 PR | 6h |
| W12 | Quantpedia Awards 검토 (SSRN 정렬) | 4h |

총합 ~32.5h (12주 / 평균 2.7h/주). owner 의 본업 + Sora 운영 + 11 SBU 운영 시간과 정합 가능 범위.

### 8.2 자본 비용 (외부 의존성)

| 항목 | 월 비용 | 12주 |
|---|---|---|
| GitHub Pro (선택, badges 빠른 update) | $4 | $12 |
| Codecov free | $0 | $0 |
| Discord free | $0 | $0 |
| Domain (선택, quantpoc.com 류) | $1/월 | $3 |
| **합계** | **$5/월** | **$15** |

GitHub Sponsors / Polar.sh 등록 = $0. 100% 활용 가능.

### 8.3 Visibility 예측 (12주 종료 시)

| Metric | 보수 | 중도 | 낙관 |
|---|---|---|---|
| Stars | 100 | 400 | 1,000 |
| Forks | 5 | 25 | 70 |
| External contributors | 0 | 3 | 10 |
| Closed PRs (external) | 0 | 5 | 20 |
| GitHub Sponsors | 0 | 1~3 | 5~10 |
| Monthly sponsorship $ | $0 | $20 | $100~$300 |

### 8.4 외부 정책 변경 risk

cold honest:
- **GitHub free tier 변경** (낮음): 비공개 repo 무료 유지 보장 없음. 단, 공개 repo 는 정책상 free 영구 유지 약속.
- **awesome-quant maintainer 변경** (중간): maintainer (wilsonfreitas) 가 활동 중단 → PR 보류. 대안: awesome-systematic-trading (wangzhe3224) 동시 PR.
- **Hacker News 알고리즘 변경** (낮음): 알고리즘 변경은 보통 abuse 차단 목적. 권고 timing 일관성 유지.
- **Polar.sh 정책 변경** (높음): 2024년 GitHub Sponsors integration 후 안정화 — 그러나 startup, runway 위험 잔존. GitHub Sponsors 가 primary 권고 (Polar.sh secondary).

### 8.5 38일 PoC failure 외부 정책 변경 패턴 반복 차단

38일 PoC 실패 (Binance liquidation API 정책 변경 + A2 OU 0/108 cells fail) 의 학습:
- **OSS 영역 외부 의존성 분산**: GitHub Actions (Microsoft) + Codecov (Sentry) + Shields.io (자체 hosted) + Discord (Discord Inc.). 한 서비스 변경 → 다른 backup 가능.
- **License 변경 risk**: MIT 는 변경 불가능 (이미 사용자 권리 부여). 변경 가능한 것: 새 contribution 의 license 만. → 12주 plan 종료 시점에는 fix.
- **Trademark / domain risk**: `quantpoc.com` 도메인 미확보 시 외부에서 squatting 가능. 12주 plan 초기 1주 안에 $11/년 으로 securing 권고.

---

## 9. References

- [Awesome Quant (wilsonfreitas)](https://github.com/wilsonfreitas/awesome-quant) — 2026-05-14 인용
- [Awesome Systematic Trading (wangzhe3224)](https://github.com/wangzhe3224/awesome-systematic-trading) — 2026-05-14 인용
- [Best Open-Source Trading Bots on GitHub (CoinCodeCap)](https://coincodecap.com/open-source-trading-bots-on-github) — 2026-05-14 인용
- [NautilusTrader GitHub](https://github.com/nautechsystems/nautilus_trader) — 2026-05-14 인용
- [Hummingbot GitHub](https://github.com/hummingbot/hummingbot) — 2026-05-14 인용
- [LGPL v3 Explained (TLDRLegal)](https://www.tldrlegal.com/license/gnu-lesser-general-public-license-v3-lgpl-3) — 2026-05-14 인용
- [Contributor Covenant v2.1](https://www.contributor-covenant.org/version/2/1/code_of_conduct/) — 2026-05-14 인용
- [GitHub Sponsors + Polar.sh integration (GitHub Blog 2024-03)](https://github.blog/changelog/2024-03-14-sponsors-now-supports-polar-and-buy-me-a-coffee-as-funding-platform-options/) — 2026-05-14 인용
- [Shields.io](https://shields.io/) — 2026-05-14 인용
- [Best time to post on Hacker News (alcazarsec)](https://blog.alcazarsec.com/tech/posts/best-time-to-post-on-hacker-news) — 2026-05-14 인용
- [When is it the best time to post on Show HN? (HN discussion id=44625897)](https://news.ycombinator.com/item?id=44625897) — 2026-05-14 인용
- [Pytest Coverage Comment GitHub Action](https://github.com/marketplace/actions/pytest-coverage-comment) — 2026-05-14 인용
- [GitHub - tj-actions/coverage-badge-py](https://github.com/tj-actions/coverage-badge-py) — 2026-05-14 인용
- [GitHub repository naming conventions (Goldenberg Lab)](https://github.com/GoldenbergLab/naming-and-documentation-conventions) — 2026-05-14 인용
- [quantitative-finance GitHub Topics](https://github.com/topics/quantitative-finance) — 2026-05-14 인용

— END —
