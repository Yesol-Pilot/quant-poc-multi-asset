# ADR-0005 — Supabase RLS public-read, anon key only on the dashboard

- Status: Accepted
- Date: 2026-05-14 (W2 D8 prep)
- Decider: Strategy Lead (autonomous G1)
- Supersedes: —
- Superseded by: —

## Context

The live dashboard (`/dashboard`) needs to read the `alphas` table (and later
`trades_paper`, `kill_switch_log`, `backtest_results`) and render them. The
question: how does a public, open-source, statically-deployed Next.js site read
from Supabase without leaking write access or requiring a login?

Options for the read path:

1. **Service-role key in the server component.** Full DB access. A leak (build
   log, env misconfig, accidental client bundle) is catastrophic.
2. **A bespoke API layer** that proxies reads with its own auth. More moving
   parts; overkill for read-only public data.
3. **Anon key + Row Level Security (RLS) public-read policies.** The anon key
   is designed to be public (it ships in `NEXT_PUBLIC_*` and is visible in the
   browser). RLS policies decide what it can see.

## Decision

Use the anon key with RLS public-read policies. Specifically:

- `supabase/migrations/00001_initial_schema.sql` enables RLS on every table and
  grants `select` to `anon` only on the tables that are safe to publish
  (`alphas`, `trades_paper`, `backtest_results`, `kill_switch_log`,
  `sensitivity_sweep`, `macro_events`, `research_papers`). No `insert`/`update`/
  `delete` for `anon` anywhere.
- `apps/live-dashboard/src/lib/supabase-server.ts` constructs the client from
  `NEXT_PUBLIC_SUPABASE_URL` + `NEXT_PUBLIC_SUPABASE_ANON_KEY` only. There is no
  service-role key anywhere in the Next.js app.
- Writes (paper-trade inserts, kill-switch logging) happen from the Python
  runner using the service-role key, which lives only in the runner's
  environment (never in the web app, never in the repo).

## Consequences

- **Leak-safe by construction.** The anon key being public is fine — RLS is the
  actual boundary. Even if someone copies the anon key from the page source,
  they can only `select` the same public data the page already shows.
- **No API layer to maintain** for the read path (the W11 public `/api/v1/*`
  surface is an additive convenience, not a security requirement).
- **Write path is physically separated.** The web app cannot write to the DB
  even if compromised, because it never holds a write-capable key.
- **Risk: a forgotten table.** If a future migration adds a sensitive table and
  forgets to scope its RLS, anon might read it. Mitigation: the migration
  template enables RLS-deny-by-default; a table is invisible until a policy
  explicitly grants `select`.

## Alternatives considered

1. Service-role key in server component — rejected: catastrophic blast radius.
2. Bespoke authenticated API — rejected: unnecessary for public read-only data.
3. **Anon key + RLS public-read** ✅ chosen.

## References

- `supabase/migrations/00001_initial_schema.sql` (RLS policies)
- `apps/live-dashboard/src/lib/supabase-server.ts` (anon-only client)
- Supabase RLS docs: https://supabase.com/docs/guides/database/postgres/row-level-security
- Neo Genesis prior art: the 2026-05-20 RLS-enable sweep on `neogenesis-main`
  (18 tables) — the lesson that RLS-off public tables are a real incident class.
