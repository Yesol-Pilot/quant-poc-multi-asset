-- ─────────────────────────────────────────────────────────
-- quant-poc-multi-asset — Initial Schema v1.0
-- Migration: 00001_initial_schema
-- Date: 2026-05-14
-- Reference: docs/design/01-architecture-spec.md §3
-- ─────────────────────────────────────────────────────────

-- Extensions
create extension if not exists "uuid-ossp";
create extension if not exists "pgcrypto";

-- Enums
create type asset_class as enum (
  'korean_equity',
  'us_equity',
  'us_option',
  'crypto'  -- archive only
);

create type alpha_status as enum (
  'planned',
  'in_progress',
  'active',
  'paused',
  'archived',
  'deprecated'
);

create type trade_side as enum ('long', 'short', 'flat');

create type kill_switch_layer as enum (
  'L1_order_rate',
  'L2_max_drawdown',
  'L3_correlation',
  'L4_exchange_health',
  'L5_mmr',
  'L6_adl_queue',
  'L7_env_guard',
  'L8_stablecoin_depeg',
  'L9_funding_spike',
  'L10_alpha_decay',
  'L11_regime',
  'L12_overfit'
);

create type regime_type as enum ('bull', 'bear', 'horizontal', 'volatile');

-- ─────────────────────────────────────────────────────────
-- 1. alphas — 21+ alpha catalog
-- ─────────────────────────────────────────────────────────
create table alphas (
  id text primary key,                       -- e.g. 'A11', 'A12', 'A1', 'A2'
  name text not null,
  asset_class asset_class not null,
  status alpha_status not null default 'planned',
  description text,
  origin_paper text,                          -- academic reference (Author, Year, Title)
  origin_doi text,
  capital_pct numeric(5,4),                   -- e.g. 0.05 = 5%
  timeframe text,                             -- e.g. '1d', '5m'
  params jsonb default '{}'::jsonb,           -- alpha-specific parameters
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create index idx_alphas_status on alphas (status);
create index idx_alphas_asset_class on alphas (asset_class);

-- ─────────────────────────────────────────────────────────
-- 2. trades_paper — Paper trading ledger
-- ─────────────────────────────────────────────────────────
create table trades_paper (
  id uuid primary key default uuid_generate_v4(),
  alpha_id text not null references alphas(id) on delete cascade,
  symbol text not null,
  side trade_side not null,
  entry_at timestamptz not null,
  entry_price numeric(20,8) not null,
  exit_at timestamptz,
  exit_price numeric(20,8),
  size numeric(20,8) not null,
  pnl numeric(20,8) generated always as (
    case
      when side = 'long' and exit_price is not null then (exit_price - entry_price) * size
      when side = 'short' and exit_price is not null then (entry_price - exit_price) * size
      else null
    end
  ) stored,
  fee numeric(20,8) default 0,
  slippage_bps numeric(8,4),
  regime regime_type,
  meta jsonb default '{}'::jsonb,
  created_at timestamptz not null default now()
);

create index idx_trades_paper_alpha on trades_paper (alpha_id);
create index idx_trades_paper_entry_at on trades_paper (entry_at desc);
create index idx_trades_paper_symbol on trades_paper (symbol);

-- ─────────────────────────────────────────────────────────
-- 3. backtest_runs — Backtest configuration + summary
-- ─────────────────────────────────────────────────────────
create table backtest_runs (
  id uuid primary key default uuid_generate_v4(),
  alpha_id text not null references alphas(id) on delete cascade,
  config jsonb not null,                    -- alpha params + period + universe
  data_period_start date not null,
  data_period_end date not null,
  total_trades integer,
  win_rate numeric(6,4),
  sharpe_ratio numeric(8,4),
  deflated_sharpe_ratio numeric(8,4),
  probability_backtest_overfit numeric(6,4),
  max_drawdown numeric(8,4),
  profit_factor numeric(8,4),
  passed_acceptance_gate boolean not null default false,
  acceptance_gate_reason text,
  status text not null default 'pending',    -- pending / running / complete / failed
  started_at timestamptz not null default now(),
  completed_at timestamptz
);

create index idx_backtest_runs_alpha on backtest_runs (alpha_id);
create index idx_backtest_runs_status on backtest_runs (status);
create index idx_backtest_runs_dsr on backtest_runs (deflated_sharpe_ratio desc);

-- ─────────────────────────────────────────────────────────
-- 4. backtest_results — Detailed metrics + equity curve
-- ─────────────────────────────────────────────────────────
create table backtest_results (
  id uuid primary key default uuid_generate_v4(),
  run_id uuid not null references backtest_runs(id) on delete cascade,
  equity_curve jsonb not null,                 -- [{ts, equity}, ...]
  metrics_json jsonb not null,                 -- full statistics
  regime_breakdown jsonb,                       -- bull/bear/horizontal/volatile
  factor_exposure jsonb,                        -- Fama-French style
  created_at timestamptz not null default now()
);

create index idx_backtest_results_run on backtest_results (run_id);

-- ─────────────────────────────────────────────────────────
-- 5. sensitivity_sweep — Parameter grid results
-- ─────────────────────────────────────────────────────────
create table sensitivity_sweep (
  id uuid primary key default uuid_generate_v4(),
  alpha_id text not null references alphas(id) on delete cascade,
  param_grid jsonb not null,                   -- {param: [v1, v2, v3]}
  results_json jsonb not null,                  -- per-cell results
  total_cells integer not null,
  passed_acceptance integer not null default 0,
  acceptance_gate_rule text not null,           -- e.g. "WR>=50 & PF>=1.3 & Sharpe>=1.0"
  created_at timestamptz not null default now()
);

create index idx_sensitivity_sweep_alpha on sensitivity_sweep (alpha_id);

-- ─────────────────────────────────────────────────────────
-- 6. kill_switch_log — Layer events
-- ─────────────────────────────────────────────────────────
create table kill_switch_log (
  id uuid primary key default uuid_generate_v4(),
  layer kill_switch_layer not null,
  triggered_at timestamptz not null default now(),
  recovered_at timestamptz,
  reason text not null,
  affected_alphas text[] default '{}'::text[],
  meta jsonb default '{}'::jsonb,
  trading_mode text not null default 'paper'  -- always 'paper' Phase 1
);

create index idx_kill_switch_log_triggered on kill_switch_log (triggered_at desc);
create index idx_kill_switch_log_layer on kill_switch_log (layer);

-- ─────────────────────────────────────────────────────────
-- 7. portfolio_state — Real-time snapshot (every minute)
-- ─────────────────────────────────────────────────────────
create table portfolio_state (
  id uuid primary key default uuid_generate_v4(),
  snapshot_at timestamptz not null default now(),
  total_equity numeric(20,8) not null,         -- in USD (paper)
  by_asset_class jsonb not null,                -- {korean_equity: X, us_equity: Y, ...}
  by_alpha jsonb not null,                      -- {A11: X, A12: Y, ...}
  active_alphas integer not null default 0,
  open_positions integer not null default 0,
  current_regime regime_type,
  kill_switch_status text default 'normal',     -- normal / warning / halted
  meta jsonb default '{}'::jsonb
);

create index idx_portfolio_state_snapshot on portfolio_state (snapshot_at desc);

-- ─────────────────────────────────────────────────────────
-- 8. macro_events — FOMC / CPI / NFP / Earnings calendar
-- ─────────────────────────────────────────────────────────
create table macro_events (
  id uuid primary key default uuid_generate_v4(),
  event_name text not null,                     -- 'FOMC', 'CPI', 'NFP', 'Earnings'
  ts_kst timestamptz not null,                  -- always KST stored
  severity text not null default 'normal',      -- normal / high / critical
  source text,                                  -- 'Fed', 'BLS', 'BOK', 'company'
  market_impact text,                           -- post-event analysis
  meta jsonb default '{}'::jsonb,
  created_at timestamptz not null default now()
);

create index idx_macro_events_ts on macro_events (ts_kst desc);
create index idx_macro_events_severity on macro_events (severity);

-- ─────────────────────────────────────────────────────────
-- 9. liquidation_events_crypto_archive — 38-day PoC archive
-- ─────────────────────────────────────────────────────────
create table liquidation_events_crypto_archive (
  id uuid primary key default uuid_generate_v4(),
  event_time timestamptz not null,
  exchange text not null,                       -- 'binance', 'bybit', 'okx'
  symbol text not null,
  side trade_side not null,
  price numeric(20,8) not null,
  quantity numeric(20,8) not null,
  notional_usd numeric(20,8) not null,
  meta jsonb default '{}'::jsonb,
  inserted_at timestamptz not null default now()
);

create index idx_liq_archive_event_time on liquidation_events_crypto_archive (event_time desc);
create index idx_liq_archive_exchange on liquidation_events_crypto_archive (exchange);
create index idx_liq_archive_symbol on liquidation_events_crypto_archive (symbol);

-- ─────────────────────────────────────────────────────────
-- 10. research_papers — SSRN / ReScience / arXiv tracking
-- ─────────────────────────────────────────────────────────
create table research_papers (
  id uuid primary key default uuid_generate_v4(),
  paper_id text unique not null,                -- e.g. 'paper-1', 'rescience-1'
  title text not null,
  venue text not null,                          -- 'SSRN', 'ReScience', 'arXiv', 'TMLR', 'NeurIPS'
  status text not null default 'draft',         -- draft / submitted / under_review / accepted / rejected / published
  abstract text,
  doi text,
  pdf_url text,
  preprint_url text,
  github_url text,
  submission_date date,
  decision_date date,
  metadata jsonb default '{}'::jsonb,
  created_at timestamptz not null default now()
);

create index idx_research_papers_status on research_papers (status);
create index idx_research_papers_venue on research_papers (venue);

-- ─────────────────────────────────────────────────────────
-- 11. public_api_logs — Rate limiting + analytics
-- ─────────────────────────────────────────────────────────
create table public_api_logs (
  id uuid primary key default uuid_generate_v4(),
  endpoint text not null,
  method text not null default 'GET',
  ip_hash text not null,                        -- hashed for privacy
  status_code integer not null,
  response_time_ms integer,
  rate_limit_remaining integer,
  meta jsonb default '{}'::jsonb,
  ts timestamptz not null default now()
);

create index idx_public_api_logs_ts on public_api_logs (ts desc);
create index idx_public_api_logs_endpoint on public_api_logs (endpoint);

-- ─────────────────────────────────────────────────────────
-- 12. newsletter_subscribers — Substack mirror (optional)
-- ─────────────────────────────────────────────────────────
create table newsletter_subscribers (
  id uuid primary key default uuid_generate_v4(),
  email_hash text unique not null,              -- bcrypt or similar
  locale text not null default 'en',            -- 'ko' / 'en'
  subscribed_at timestamptz not null default now(),
  unsubscribed_at timestamptz,
  source text                                   -- 'site_form', 'substack_sync', etc.
);

create index idx_newsletter_locale on newsletter_subscribers (locale);

-- ─────────────────────────────────────────────────────────
-- Row-Level Security (RLS) — all tables default deny
-- ─────────────────────────────────────────────────────────

alter table alphas enable row level security;
alter table trades_paper enable row level security;
alter table backtest_runs enable row level security;
alter table backtest_results enable row level security;
alter table sensitivity_sweep enable row level security;
alter table kill_switch_log enable row level security;
alter table portfolio_state enable row level security;
alter table macro_events enable row level security;
alter table liquidation_events_crypto_archive enable row level security;
alter table research_papers enable row level security;
alter table public_api_logs enable row level security;
alter table newsletter_subscribers enable row level security;

-- Public read access for non-sensitive tables (dashboard + API)
create policy "Public read alphas" on alphas for select using (true);
create policy "Public read trades_paper" on trades_paper for select using (true);
create policy "Public read backtest_runs" on backtest_runs for select using (true);
create policy "Public read backtest_results" on backtest_results for select using (true);
create policy "Public read sensitivity_sweep" on sensitivity_sweep for select using (true);
create policy "Public read kill_switch_log" on kill_switch_log for select using (true);
create policy "Public read portfolio_state" on portfolio_state for select using (true);
create policy "Public read macro_events" on macro_events for select using (true);
create policy "Public read research_papers" on research_papers for select using (
  status in ('submitted', 'under_review', 'accepted', 'published')
);

-- Write access ONLY via service role key (server-side)
-- Anonymous/authenticated users cannot insert/update/delete

-- ─────────────────────────────────────────────────────────
-- Triggers — updated_at auto-update
-- ─────────────────────────────────────────────────────────
create or replace function update_updated_at()
returns trigger as $$
begin
  new.updated_at = now();
  return new;
end;
$$ language plpgsql;

create trigger trg_alphas_updated
  before update on alphas
  for each row execute function update_updated_at();

-- ─────────────────────────────────────────────────────────
-- Seed: 21+ alphas (planned state, populated as built)
-- ─────────────────────────────────────────────────────────
insert into alphas (id, name, asset_class, status, description, origin_paper) values
  -- Crypto archive (38-day PoC)
  ('A1', 'Liquidation Cascade', 'crypto', 'archived', 'Binance/Bybit/OKX liquidation cluster reversal', 'cryptofeed (2024) Liquidation cascade study'),
  ('A2', 'Mean-Reversion OU', 'crypto', 'deprecated', '108/108 sensitivity sweep failure', 'Cartea, Jaimungal, Penalva (2015) Ch 6'),
  ('A3', 'Extreme Funding', 'crypto', 'archived', '4-condition fade strategy', 'Alexander et al. (2023)'),
  ('A4', 'Macro Event Bracket', 'crypto', 'archived', 'FOMC/CPI/NFP event bracket', 'Bali, Demir, Tehranian (2008)'),
  ('A6', 'Alt-coin MM', 'crypto', 'archived', 'Avellaneda-Stoikov engine spec only', 'Avellaneda, Stoikov (2008)'),
  -- Korean equities (planned W2~3)
  ('A11', 'Korean ETF Sector Rotation', 'korean_equity', 'planned', 'KOSPI 200 sector monthly rotation', 'Lakonishok, Shleifer, Vishny (1994)'),
  ('A12', 'KOSPI Mean Reversion', 'korean_equity', 'planned', '5-day large-cap mean reversion', 'De Bondt, Thaler (1985)'),
  ('A13', 'Korea Pair Trading', 'korean_equity', 'planned', 'Cointegrated KOSPI 200 pair', 'Engle, Granger (1987)'),
  ('A14', 'PEAD on KOSPI', 'korean_equity', 'planned', 'Quarterly earnings momentum', 'Bernard, Thomas (1989)'),
  -- US equities (planned W4~6)
  ('A15', 'US Factor Investing', 'us_equity', 'planned', 'Fama-French 5-factor (US only)', 'Fama, French (2015)'),
  ('A16', 'US Risk Parity (Dalio All Weather)', 'us_equity', 'planned', 'VTI + TLT + GLD + DBC equal risk', 'Bridgewater All Weather'),
  ('A17', 'US PEAD', 'us_equity', 'planned', 'Russell 2000 small-cap PEAD', 'Bernard, Thomas (1989)'),
  ('A18', 'US Sector Momentum', 'us_equity', 'planned', '11 SPDR sectors 12-1 momentum', 'Jegadeesh, Titman (1993)'),
  -- US options (planned W7~8)
  ('A19', 'Covered Call', 'us_option', 'planned', 'SPY/QQQ monthly covered call', 'CBOE BXM index'),
  ('A20', 'Volatility Risk Premium', 'us_option', 'planned', 'VIX futures short', 'Bakshi, Kapadia (2003)'),
  ('A21', 'Iron Condor', 'us_option', 'planned', 'Low volatility regime iron condor', 'Various practitioner');

-- ─────────────────────────────────────────────────────────
-- End of initial schema
-- ─────────────────────────────────────────────────────────
