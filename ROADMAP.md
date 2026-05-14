# Roadmap — 12 Weeks (2026-05-14 ~ 2026-08-05)

> Live status. Updated weekly. See [docs/design/03-12week-daily-plan-and-milestones.md](docs/design/03-12week-daily-plan-and-milestones.md) for 84-day daily plan.

---

## Phase Overview

```
W1 (5/14~5/20)   Setup           : repo public + Live page scaffold + accounts
W2 (5/21~5/27)   KIS Integration : KIS API + A11 first build + paper trading start
W3 (5/28~6/3)    Korean Alphas   : A12 + A13 + A14 + Backtest harness
W4 (6/4~6/10)    US Layer Start  : IBKR Korea paper account + A15 (US Factor) + A16 (Risk Parity)
W5 (6/11~6/17)   US Alphas       : A17 (US PEAD) + A18 (Sector Momentum)
W6 (6/18~6/24)   Options Layer   : A19 (Covered Call) + A20 (VRP) + Theta Data ($80)
W7 (6/25~7/1)    Iron Condor + Integration : A21 + full backtest harness
W8 (7/2~7/8)     DSR / PBO       : Statistical rigor + Sensitivity Sweep + Polygon Starter ($198)
W9 (7/9~7/15)    Paper 1 draft   : "1-Person Multi-Strategy Honest Failure" (SSRN draft 50%)
W10 (7/16~7/22)  ReScience + Paper polish : FF5 KOSPI 200 replication draft
W11 (7/23~7/29)  Pre-launch      : Lighthouse 95+ + Public API + Docs site
W12 (7/30~8/5)   LAUNCH          : SSRN submit + ReScience submit + Hacker News Show HN
```

---

## Week 1 (5/14 ~ 5/20) — Setup [in progress]

### D1 (Tue 5/14)
- [x] Directory created (`D:/00.test/002.products-sbu/quant-poc-multi-asset/`)
- [x] LICENSE (MIT)
- [x] DISCLAIMER (en + ko)
- [x] README v0 (en + ko)
- [x] .gitignore
- [x] ROADMAP (this file)
- [ ] CONTRIBUTING.md
- [ ] SECURITY.md
- [ ] CODE_OF_CONDUCT.md
- [ ] CHANGELOG.md
- [ ] pnpm-workspace.yaml + package.json (root)
- [ ] Python pyproject.toml
- [ ] tsconfig.base.json
- [ ] .github/workflows/ci.yml (Vitest + pytest baseline)
- [ ] git init + first commit
- [ ] GitHub repo public + remote push

### D2~D7
- KIS Developers 가입 (owner action, 2~3h)
- Twitter / LinkedIn / Substack accounts
- Vercel project create (Vercel Pro 활성)
- Supabase project create (Supabase Pro 활성)
- Docker / Dev Container setup
- 16 Research + 3 Design docs sync to repo

---

## Cumulative Deliverables Status

| Dimension | Target (Week 12) | Current |
|---|---|---|
| **D1 Code** | 1,000+ tests / 90% coverage | 0 / 0% |
| **D2 Academic** | SSRN 1 + ReScience 1 submitted | 0 / 0 |
| **D3 OSS** | GitHub 300~600 stars | 0 |
| **D4 Live** | Lighthouse 95+ / heoyesol.kr/quant | not deployed |
| **D5 Communication** | Newsletter 100~800 subs | 0 |

---

## Auto-update

This file is updated weekly by Strategy Lead (Claude Opus 4.7) every Monday 08:00 KST.

**Next update**: 2026-05-19 (Mon, Week 1 D6 → D7 transition)
