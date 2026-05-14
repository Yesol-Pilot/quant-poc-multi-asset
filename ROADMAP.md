# Roadmap — 12 Weeks (2026-05-14 ~ 2026-08-05)

> Live status. Updated weekly. See [docs/design/03-12week-daily-plan-and-milestones.md](docs/design/03-12week-daily-plan-and-milestones.md) for the 84-day daily plan.

---

## Phase Overview

```
W1 (5/14~5/20)   Setup           : repo public + Live page scaffold + accounts                [in progress]
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

## Week 1 (5/14 ~ 5/20) — Setup [in progress, D1~D4 done]

### D1 (Tue 5/14) — Foundations [done]
- [x] Directory created (`D:/00.test/002.products-sbu/quant-poc-multi-asset/`)
- [x] LICENSE (MIT)
- [x] DISCLAIMER (en + ko)
- [x] README v0 (en + ko, Honest Failure hero, project-only framing)
- [x] .gitignore (Node + Python + Vercel + Supabase + secrets)
- [x] ROADMAP (this file)
- [x] ARCHITECTURE.md (12 tables map + tech stack)
- [x] CONTRIBUTING.md (academic standards + Kill Switch invariants)
- [x] SECURITY.md (12-Layer threat model + disclosure)
- [x] CODE_OF_CONDUCT.md (Contributor Covenant v2.1)
- [x] CHANGELOG.md (Keep a Changelog format)
- [x] pnpm-workspace.yaml + root package.json (pnpm 9.15 + turbo)
- [x] pyproject.toml (Python 3.11+ / `ib_async` not `ib_insync` / ruff + mypy + pytest)
- [x] tsconfig.base.json (TS 5.7 strict)
- [x] `.github/workflows/ci.yml` (paper-only-guard + Node + Python jobs)
- [x] `.github/workflows/weekly-progress-telegram.yml` (Mon 08:00 KST → @Claude_alert_sol_bot)
- [x] git init + first commit
- [x] GitHub repo public + remote push (`Yesol-Pilot/quant-poc-multi-asset`)

### D2 (Wed 5/15) — Infrastructure provisioning [done]
- [x] Supabase project created (`mpwxsfsxinasjtgqxsdu`, ap-northeast-2, PG 17.6)
- [x] 12-table schema applied (`00001_initial_schema.sql` migration)
- [x] 16 alphas seeded (A1~A6 archive, A11~A21 planned)
- [x] Vercel project linked (`prj_iInBkKiPUrDTM7FCSc2W7XVIF1OV`, team `yesol-pilot's projects`)
- [x] 3 env vars set (NEXT_PUBLIC_SUPABASE_URL/ANON_KEY + NEXT_TELEMETRY_DISABLED)
- [x] Custom domain `quant.heoyesol.kr` (Vercel verified=true)
- [x] Cloudflare CNAME `quant.heoyesol.kr → cname.vercel-dns.com` (record `ce552781`)

### D3 (Thu 5/16) — Dashboard scaffold [done]
- [x] `apps/live-dashboard` Next 15 + React 19 + Tailwind v4 + Tremor + next-intl
- [x] Devcontainer (`.devcontainer/devcontainer.json`, Universal:2 + Node 20 + Py 3.11 + Docker-in-Docker)
- [x] `vitest.config.ts` + `src/test/setup.ts` (jsdom + jest-dom)
- [x] `vercel.json` (icn1 region + security headers)
- [x] `.env.example` (TRADING_MODE=paper, IBKR_PORT=7497, KIS mock)
- [x] `apps/live-dashboard/src/app/page.tsx` (Hero −15.1% + 5-Dim + 4 assets + heoyesol.kr redirect)
- [x] `apps/live-dashboard/src/app/page.test.tsx` (5 Vitest tests, all pass intent)
- [x] `apps/live-dashboard/src/app/layout.tsx` (metadata + OG + sticky disclaimer footer)
- [x] `apps/live-dashboard/src/app/globals.css` (OKLCH tokens + Honest Failure styles)

### D4 (Fri 5/17) — Docs sync + pages + i18n + marketing drafts [done]
- [x] 17 research reports synced (`docs/research/00~16.md`, ~65,000 words / 300+ refs)
- [x] 4 design specs synced (`docs/design/01~04.md`, Architecture + Alphas + 12wk plan + Live page v2.0)
- [x] `apps/live-dashboard/src/app/about/page.tsx` (project mission, project-only framing)
- [x] `apps/live-dashboard/src/app/disclaimer/page.tsx` (en + ko regulatory, live-trading guards)
- [x] `apps/live-dashboard/src/app/dashboard/page.tsx` (placeholder + what-will-be-here + status)
- [x] `messages/en.json` + `messages/ko.json` (next-intl catalogs, wire-up W2)
- [x] `src/i18n/request.ts` (next-intl scaffold, defaultLocale=ko, locales=[ko, en])
- [x] `docs/marketing/profile-bios.md` (Twitter/LinkedIn/Substack bios, dual-language)
- [x] `docs/marketing/substack-issue-01-draft.md` (Honest Failure inaugural issue)
- [x] `docs/marketing/twitter-pinned-tweet.md` (single pin + 5-tweet thread + 3 A/B variants)
- [x] `docs/marketing/linkedin-launch-post.md` (en + ko launch posts + engagement playbook)

### D5~D7 (Sat 5/18 ~ Mon 5/20) — Owner-action window + buffer
- [ ] Owner: KIS Developers signup (2~3h, blocking W2 D8 KIS integration)
- [ ] Owner: Twitter/LinkedIn handles confirmed → bios deployed
- [ ] Owner: Substack publication created → publication name decided
- [ ] Owner: GitHub repo secrets — `CLAUDE_ALERT_BOT_TOKEN` + `OWNER_TELEGRAM_CHAT_ID` (3 min, activates weekly cron)
- [ ] Owner: Discord server skeleton (optional, W3+)
- [ ] Strategy Lead: Vercel first deployment trigger (push event will auto-deploy)
- [ ] Strategy Lead: Verify `https://quant.heoyesol.kr` returns 200 with hero
- [ ] Strategy Lead: Run `pnpm test` in `apps/live-dashboard` once env is up (Vitest jsdom)
- [ ] Strategy Lead: Run `pytest tests/test_smoke.py` (7 smoke tests)
- [ ] Strategy Lead: Lighthouse first-run baseline (target ≥85 for W1, ≥95 for W11)

---

## Cumulative Deliverables Status (end of W1 D4)

| Dimension | Target (Week 12) | Current (W1 D4) |
|---|---|---|
| **D1 Code** | 1,000+ tests / 90% coverage | 12 tests (5 Vitest + 7 pytest) / coverage NA |
| **D2 Academic** | SSRN 1 + ReScience 1 submitted | 0 / 0 (drafts open W9) |
| **D3 OSS** | GitHub 300~600 stars | Public, 0 stars (organic launch W2 D9) |
| **D4 Live** | Lighthouse 95+ / heoyesol.kr/quant | scaffold pushed, deployment pending |
| **D5 Communication** | Newsletter 100~800 subs | 3 marketing drafts ready, 0 subs |

---

## Auto-update

This file is updated weekly by Strategy Lead (Claude Opus 4.7) every Monday 08:00 KST.

**Next update**: 2026-05-19 (Mon, Week 1 D6 → D7 transition with deployment numbers).
