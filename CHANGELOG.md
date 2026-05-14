# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

Week 1 (5/14 ~ 5/20) — Setup phase. All entries below land on the same date until the first tag (v0.1.0 at end of W1).

### Added — W1 D1 (2026-05-14, Tue) — Foundations

- Initial directory layout under `D:/00.test/002.products-sbu/quant-poc-multi-asset/`
- LICENSE (MIT, Copyright (c) 2026 허예솔 / Yesol Huh)
- DISCLAIMER (Korean Capital Markets Act + US SEC language, dual-language)
- README v0 (Honest Failure hero anchored on −15.1%, project-only framing, no career pitch)
- .gitignore (Node + Python + Vercel + Supabase + secrets patterns)
- ROADMAP.md (12-week phase plan)
- ARCHITECTURE.md (system overview + 12-table map + tech stack table)
- CONTRIBUTING.md (academic standards + Kill Switch invariants)
- SECURITY.md (12-layer threat model + responsible disclosure)
- CODE_OF_CONDUCT.md (Contributor Covenant v2.1)
- CHANGELOG.md (this file)
- pnpm-workspace.yaml (`packages/*` + `apps/*`)
- Root `package.json` (pnpm 9.15.0 + Node 20 + turbo)
- pyproject.toml (Python 3.11+, `ib_async>=2.0` not deprecated `ib_insync`, ruff + mypy + pytest)
- tsconfig.base.json (TypeScript 5.7 strict)
- `.github/workflows/ci.yml` (paper-only-guard blocks port 7496 and `openapi.koreainvestment.com`; Node + Python jobs; docs-check)
- `.github/workflows/weekly-progress-telegram.yml` (cron `0 23 * * 0` = Mon 08:00 KST → `@Claude_alert_sol_bot`)

### Added — W1 D2 (2026-05-15, Wed) — Infrastructure

- Supabase project `mpwxsfsxinasjtgqxsdu` (ap-northeast-2, Postgres 17.6) provisioned via master access token
- `supabase/migrations/00001_initial_schema.sql` applied: 12 tables (alphas, trades_paper, backtest_runs, backtest_results, sensitivity_sweep, kill_switch_log, portfolio_state, macro_events, liquidation_events_crypto_archive, research_papers, public_api_logs, newsletter_subscribers) + 6 enums + public-read RLS policies + 16 seed alphas (A1~A6 archive, A11~A21 planned)
- `supabase/config.toml` (project_id, realtime enabled)
- Vercel project `prj_iInBkKiPUrDTM7FCSc2W7XVIF1OV` linked to `Yesol-Pilot/quant-poc-multi-asset`, framework nextjs, rootDirectory `apps/live-dashboard`, monorepo build commands set
- 3 Vercel environment variables (production+preview+development): `NEXT_PUBLIC_SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_ANON_KEY`, `NEXT_TELEMETRY_DISABLED=1`
- Cloudflare CNAME `quant.heoyesol.kr → cname.vercel-dns.com` created (zone `4e032e6a...`, record `ce552781f5684b4227abcb231faec9e9`, proxied=false for Vercel)
- Vercel custom domain `quant.heoyesol.kr` added and verified=true

### Added — W1 D3 (2026-05-16, Thu) — Dashboard scaffold

- `apps/live-dashboard/package.json` (Next 15.1 + React 19 + Tailwind v4 + Tremor + next-intl + supabase-ssr + zod + recharts + lucide)
- `apps/live-dashboard/next.config.ts` (basePath support + security headers + image domains)
- `apps/live-dashboard/tsconfig.json` (extends root, `@/*` alias)
- `apps/live-dashboard/postcss.config.mjs` (`@tailwindcss/postcss` v4)
- `apps/live-dashboard/src/app/globals.css` (OKLCH design tokens + Honest Failure framing + LIVE pulse animation + sticky disclaimer footer styles)
- `apps/live-dashboard/src/app/layout.tsx` (metadata + Open Graph ko_KR default + en_US alt + sticky disclaimer footer)
- `apps/live-dashboard/src/app/page.tsx` (Hero −15.1% + 5-Dim cards + 4 asset class cards + maintainer/heoyesol.kr redirect)
- `apps/live-dashboard/vitest.config.ts` (jsdom + v8 coverage)
- `apps/live-dashboard/src/test/setup.ts` (`@testing-library/jest-dom`)
- `apps/live-dashboard/src/app/page.test.tsx` (5 tests: Hero, 5-Dim, 4 assets, GitHub CTA, heoyesol.kr redirect)
- `apps/live-dashboard/.gitignore`
- `.devcontainer/devcontainer.json` (Universal:2 + Node 20 + Python 3.11 + Docker-in-Docker + 13 VS Code extensions + ports 3000/54321-54323)
- `vercel.json` (icn1 region + security headers + monorepo buildCommand from root)
- `.env.example` (TRADING_MODE=paper default, IBKR_PORT=7497, KIS mock URL)
- `tests/test_smoke.py` (7 tests: repo layout + OSS files + pyproject + core import + KIS live URL guard + IBKR 7496 guard + .env.example paper-mode check)
- `packages/core/__init__.py` + `version.py` (Python package shell)

### Added — W1 D4 (2026-05-17, Fri) — Pages, i18n, marketing, docs sync

- `apps/live-dashboard/src/app/about/page.tsx` — project mission, 5-dimension breakdown, project-only framing, maintainer block, MIT license link, disclaimer redirect
- `apps/live-dashboard/src/app/disclaimer/page.tsx` — dual-language regulatory disclaimer (English + 한국어 자본시장법 정합), live-trading CI guards documented, contact routing
- `apps/live-dashboard/src/app/dashboard/page.tsx` — placeholder with explicit Week-by-Week wire-up plan, current status indicators, links to repo surfaces
- `apps/live-dashboard/messages/en.json` — English next-intl message catalog (meta + nav + hero + fiveDim + assets + footer)
- `apps/live-dashboard/messages/ko.json` — 한국어 next-intl message catalog (동일 구조)
- `apps/live-dashboard/src/i18n/request.ts` — next-intl request config (defaultLocale=ko, locales=[ko, en], timeZone=Asia/Seoul, scaffold-only for W1, full wire-up W2)
- `docs/research/00~16.md` — 17 research reports synced from prior PoC workspace (~65,000 words / 300+ references) covering KIS/IBKR/options/factor/risk/PEAD/microstructure/competitive analysis/regulatory landscape/macro events
- `docs/design/01~04.md` — 4 design specs synced: Architecture (11,238w), Alpha specifications (12,414w), 12-week daily plan (17,909w), Live page product spec v2.0 (14,413w)
- `docs/marketing/profile-bios.md` — Twitter/LinkedIn/Substack/Discord/Reddit bio drafts (KR+EN dual), ~70-min owner action checklist, cross-link consistency rules
- `docs/marketing/substack-issue-01-draft.md` — inaugural issue (English + 한국어), Honest Failure hook, weekly newsletter format (one number / one lesson / one link), pre-publish checklist
- `docs/marketing/twitter-pinned-tweet.md` — pinned tweet + 5-tweet thread + 3 A/B variants (research-credibility / methodology / Korean-retail) + pre-publish checklist + engagement playbook
- `docs/marketing/linkedin-launch-post.md` — launch posts (English ~1,800 chars + 한국어 ~1,400 chars) + pre-publish checklist + first-48h engagement playbook

### Referenced

- 17 Research reports from `docs/research/` (linked from README)
- 4 Design specs from `docs/design/` (linked from ARCHITECTURE.md + ROADMAP)
- 3 marketing drafts ready for owner-action publish in W2

### Infrastructure decisions (locked-in W1)

- Vercel team: `yesol-pilot's projects` (`team_YQwNNAv4XjpyZALb2O8A67tL`)
- Supabase organization: `Yesol-Pilot's Org` (`ysaiicjlqepunpevjell`)
- GitHub user: `Yesol-Pilot` (id `86992002`) — `neogenesislab` is explicitly forbidden per CLAUDE.md §1.1
- Domain: `quant.heoyesol.kr` (subdomain of canonical career site, deliberately separate)
- Region: ap-northeast-2 (Supabase) + icn1 (Vercel) — single-region, Seoul-anchored
- License: MIT (allows commercial use of Kill Switch invariants and academic methodology)

---

## Pre-history

This project is a **continuation of a 38-day Crypto PoC** (2026-04-05 ~ 2026-05-12) that resulted in:

- 191 paper trades, 37.7% win rate, **−15.1% paper PnL**
- 0 of 108 sensitivity-sweep cells passed acceptance on A2 (flagship mean-reversion)
- Production-grade 9-Layer Kill Switch (commit `c8f4e7b`)
- Cross-exchange aggregation (Binance + Bybit + OKX, commits `c8f4e7b` ~ `4849d84`)
- Honest closure (2026-05-12) and pivot to **12-week multi-asset rebuild**

That PoC's lessons inform every alpha and Kill Switch layer in this repo. The 9-layer kill switch is reused verbatim (with three new layers — L10 Alpha Decay, L11 Regime, L12 Overfit — added on top).

For full PoC retrospective: see [docs/research/07-competitive-analysis.md](docs/research/07-competitive-analysis.md) and the upcoming **Paper 1 (SSRN)** scheduled for W9~W12.

---

[Unreleased]: https://github.com/Yesol-Pilot/quant-poc-multi-asset/compare/v0.0.0...HEAD
