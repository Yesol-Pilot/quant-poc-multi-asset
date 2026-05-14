import Link from 'next/link';

export const metadata = {
  title: 'Dashboard · quant-poc-multi-asset',
  description:
    'Live paper-trade dashboard. Currently scaffolding (Week 1). KIS mock + IBKR paper data wire-up starts Week 2-4.',
};

export default function DashboardPlaceholderPage() {
  return (
    <main className="min-h-screen px-6 py-12 mx-auto max-w-4xl">
      <nav className="mb-8 text-sm">
        <Link
          href="/"
          className="text-[color:var(--color-muted-foreground)] hover:text-[color:var(--color-fg)]"
        >
          ← Home
        </Link>
      </nav>

      <h1 className="text-3xl md:text-4xl font-bold mb-3">Live Dashboard</h1>
      <p className="text-lg text-[color:var(--color-muted-foreground)] mb-10">
        Scaffolding. First live numbers land in Week 2 (KIS mock paper PnL) and
        expand through Week 12.
      </p>

      <section className="mb-10">
        <h2 className="text-2xl font-bold mb-4">What will be here</h2>
        <ul className="space-y-3 leading-relaxed">
          <li>
            <strong>Live paper PnL</strong> per alpha (A11~A21), per asset
            class, and rolled up portfolio-wide. Sourced from
            <code className="mx-1">trades_paper</code> in Supabase, refreshed
            via Realtime channels.
          </li>
          <li>
            <strong>Kill-switch event stream</strong> — every L1~L12 trigger
            since deployment, with timestamp, layer, alpha, and resolution
            state. Read-only.
          </li>
          <li>
            <strong>Backtest results</strong> — Deflated Sharpe Ratio (DSR),
            Probability of Backtest Overfitting (PBO), sensitivity sweep grid
            (e.g., the 0/108 cells from the closed crypto A2 sweep). Each cell
            links to the run that produced it.
          </li>
          <li>
            <strong>Macro event calendar</strong> — CPI, FOMC, BoK announcements
            with the alphas that should pause around each event window.
          </li>
          <li>
            <strong>Public read-only API</strong> mirrored at{' '}
            <code>/api/v1/*</code> for anyone who wants to verify the numbers
            without scraping the page.
          </li>
        </ul>
      </section>

      <section className="mb-10">
        <h2 className="text-2xl font-bold mb-4">Status — Week 1</h2>
        <div className="p-5 border border-[color:var(--color-border)] rounded-lg bg-[color:var(--color-muted)]">
          <p className="font-mono text-sm mb-2">
            <span className="inline-block w-2 h-2 rounded-full bg-yellow-500 mr-2"></span>
            scaffold · no live data wired
          </p>
          <ul className="text-sm space-y-1 mt-3">
            <li>✓ Supabase project created (ap-northeast-2)</li>
            <li>✓ 12-table schema applied (initial migration)</li>
            <li>✓ 16 alphas seeded as <code>archive</code> /{' '}
              <code>planned</code></li>
            <li>○ KIS mock data ingest — Week 2</li>
            <li>○ IBKR paper data ingest — Week 4</li>
            <li>○ Tremor charts wire-up — Week 3</li>
            <li>○ Realtime kill-switch channel — Week 6</li>
            <li>○ Public read-only API — Week 11</li>
          </ul>
        </div>
      </section>

      <section className="mb-10">
        <h2 className="text-2xl font-bold mb-4">Where to look in the meantime</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
          <a
            href="https://github.com/Yesol-Pilot/quant-poc-multi-asset/commits/main"
            className="p-4 border border-[color:var(--color-border)] rounded-lg hover:bg-[color:var(--color-muted)] transition"
          >
            <p className="font-medium">Recent commits →</p>
            <p className="text-xs text-[color:var(--color-muted-foreground)]">
              GitHub commit log
            </p>
          </a>
          <a
            href="https://github.com/Yesol-Pilot/quant-poc-multi-asset/tree/main/docs/research"
            className="p-4 border border-[color:var(--color-border)] rounded-lg hover:bg-[color:var(--color-muted)] transition"
          >
            <p className="font-medium">17 research reports →</p>
            <p className="text-xs text-[color:var(--color-muted-foreground)]">
              ~65,000 words / 300+ references
            </p>
          </a>
          <a
            href="https://github.com/Yesol-Pilot/quant-poc-multi-asset/tree/main/docs/design"
            className="p-4 border border-[color:var(--color-border)] rounded-lg hover:bg-[color:var(--color-muted)] transition"
          >
            <p className="font-medium">4 design specs →</p>
            <p className="text-xs text-[color:var(--color-muted-foreground)]">
              Architecture, alphas, 84-day plan, this page
            </p>
          </a>
          <a
            href="https://github.com/Yesol-Pilot/quant-poc-multi-asset/blob/main/ROADMAP.md"
            className="p-4 border border-[color:var(--color-border)] rounded-lg hover:bg-[color:var(--color-muted)] transition"
          >
            <p className="font-medium">Roadmap →</p>
            <p className="text-xs text-[color:var(--color-muted-foreground)]">
              12-week milestone tracking
            </p>
          </a>
        </div>
      </section>

      <p className="text-sm text-[color:var(--color-muted-foreground)]">
        Read the{' '}
        <Link href="/disclaimer" className="underline">
          disclaimer
        </Link>{' '}
        before interpreting any number on this site as advice. It is not.
      </p>
    </main>
  );
}
