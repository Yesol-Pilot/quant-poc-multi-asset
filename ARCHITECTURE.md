# Architecture

> Full spec: [docs/design/01-architecture-spec.md](docs/design/01-architecture-spec.md) (11,238 words / 92KB)
> 빠른 overview only — full spec 으로 deep dive 시작.

## System Architecture (high-level)

```
┌─────────────────────────────────────────────────────────────────┐
│                        Multi-Asset Layer                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐         │
│  │  Korean  │  │   US     │  │  Options │  │  Crypto  │         │
│  │  Equity  │  │  Equity  │  │   (US)   │  │ (archive)│         │
│  │  (KIS)   │  │  (IBKR)  │  │  (IBKR)  │  │          │         │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘         │
└──────────────────────────┬──────────────────────────────────────┘
                           │
        ┌──────────────────┴──────────────────┐
        ▼                                     ▼
┌────────────────┐                    ┌────────────────┐
│ Strategy Layer │                    │ Risk Layer     │
│ - 21+ Alphas   │ ◄────── feedback ──┤ - 12-Layer KS  │
│ - Multi-agent  │                    │ - DSR/PBO/Reg  │
│ - LLM Views    │                    │ - Sensitivity  │
└────────┬───────┘                    └────────┬───────┘
         │                                     │
         └──────────────────┬──────────────────┘
                            ▼
                ┌──────────────────────┐
                │ Execution Layer      │
                │ - Paper trading      │
                │ - Order routing      │
                │ - Reconciliation     │
                └──────────┬───────────┘
                           │
        ┌──────────────────┴──────────────────┐
        ▼                                     ▼
┌────────────────┐                    ┌────────────────┐
│ Live Dashboard │                    │ Public API     │
│ heoyesol.kr/   │                    │ (rate-limited) │
│ quant          │                    │                │
└────────────────┘                    └────────────────┘

        Supabase Pro (Postgres + Realtime + Edge Functions + Vault)
        ↑
        ├── alphas, trades_paper, backtest_runs, kill_switch_log,
        │   portfolio_state, macro_events, sensitivity_sweep,
        │   liquidation_events_crypto_archive, research_papers,
        │   public_api_logs (12 tables total)
        │
        Multi-agent: Claude (Strategy Lead) + Codex (parallel) + Gemini (runtime)
```

## Tech Stack

| Layer | Choice | Why |
|---|---|---|
| Frontend (Live page) | Next.js 15 + Tremor + Vercel Pro | React ecosystem + Vercel Pro analytics |
| Database | Supabase Pro ($25/mo, 8GB) | Postgres + Realtime + RLS |
| Backend (Strategy) | Python + Node.js dual | Python = backtest/ML, Node.js = realtime |
| LLM (Runtime) | Gemini 2.5 Flash ($100 budget) | Cost effective, macro/news sentiment |
| LLM (Build) | Claude Opus 4.7 (Max plan) | Strategy Lead multi-agent orchestration |
| Broker (KR) | KIS Developers REST (모의투자) | Production grade, free paper |
| Broker (US) | IBKR TWS API + `ib_async` | Paper account, options, intraday free |
| Monorepo | pnpm workspace + Python venv | Dual-language support |
| CI/CD | GitHub Actions | Free, integrated |
| Containers | Docker / Dev Container | Reproducibility |
| License | MIT | Maximum reuse, no patent grant complexity |

## Module Structure

```
quant-poc-multi-asset/
├── packages/
│   ├── @qpm/core              shared utilities (TS + Python)
│   ├── @qpm/alphas            21+ alpha implementations
│   ├── @qpm/risk              9-Layer Kill Switch + DSR/PBO
│   ├── @qpm/backtest          Backtest harness + Sensitivity sweep
│   ├── @qpm/exchanges         KIS / IBKR / Crypto adapters
│   ├── @qpm/orchestrator      Multi-agent (Claude/Codex/Gemini)
│   └── @qpm/dashboard         Next.js Live page (shared components)
├── apps/
│   ├── live-dashboard         heoyesol.kr/quant
│   ├── api                    Public API (rate-limited)
│   └── docs                   Docusaurus
├── docs/
│   ├── research/              16 Research reports
│   ├── design/                3 Design specs
│   └── tutorials/             Getting started
├── notebooks/                 Jupyter reproducibility
├── tests/                     1,000+ tests target
├── .github/workflows/         CI/CD
├── docker/                    Dev Container
└── (standard OSS files)
```

## Database Schema (12 tables)

See [docs/design/01-architecture-spec.md §3](docs/design/01-architecture-spec.md) for full SQL DDL.

Key tables:
- `alphas` — 21+ alpha configurations
- `trades_paper` — Paper trading ledger
- `backtest_runs` + `backtest_results` — DSR/PBO/Sharpe results
- `sensitivity_sweep` — Parameter grid + acceptance gate
- `kill_switch_log` — 12-Layer events
- `portfolio_state` — Real-time portfolio snapshot
- `macro_events` — FOMC/CPI/NFP/Earnings calendar
- `liquidation_events_crypto_archive` — 38-day PoC archive
- `research_papers` — SSRN/ReScience submission tracking
- `public_api_logs` — Rate limiting + usage

## Multi-Agent Orchestration

3-way agent collaboration:
- **Strategy Lead** (Claude Opus 4.7 Max plan) — build-time architecture + code review + research synthesis
- **Codex** (GPT-5 Codex CLI) — parallel implementation work
- **Gemini 2.5 Flash** — production runtime (macro/news sentiment, ~$0.02/call, $100 budget)

SSOT via `active-tasks.md` + `handoff.md` + Supabase `agent_messages` table.

## Tech Stack — Critical Findings (2026-05-14)

1. **Gemini 2.0 Flash deprecated 2026-02-18, shutdown 2026-06-01** → Gemini 2.5 Flash 사용
2. **`ib_insync` deprecated** → `ib_async` 사용 (Interactive Brokers 공식 미지원)
3. **KIS 분봉 historical 무료 부재** → Phase 1 = daily-bar alphas only
4. **TWS paper port 7497 hard guard** (`enforce_paper_only()` + CI grep `:7496` 차단)

## Next: Read [docs/design/01-architecture-spec.md](docs/design/01-architecture-spec.md) for full detail.
