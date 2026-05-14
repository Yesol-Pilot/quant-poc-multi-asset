import Link from 'next/link';
import { fetchAlphas, type AlphaRow } from '@/lib/supabase-server';

export const metadata = {
  title: 'Dashboard · quant-poc-multi-asset',
  description:
    'Live paper-trade dashboard. Reads from Supabase (read-only, RLS-gated). Backtest/PnL panels land W2-W4.',
};

// Force revalidation on every request (server rendered) so the dashboard
// reflects the latest Supabase state. W3+ may switch to ISR with revalidate.
export const dynamic = 'force-dynamic';

const ASSET_CLASS_LABEL: Record<string, string> = {
  korean_equity: '🇰🇷 Korean equity',
  us_equity: '🇺🇸 US equity / ETF',
  us_option: '📈 US options',
  crypto: '₿ Crypto (archive)',
};

const STATUS_BADGE_CLASS: Record<string, string> = {
  active: 'bg-green-500/15 text-green-600',
  in_progress: 'bg-yellow-500/15 text-yellow-700',
  paused: 'bg-orange-500/15 text-orange-600',
  planned: 'bg-slate-500/15 text-slate-600',
  archived: 'bg-zinc-500/15 text-zinc-500',
  deprecated: 'bg-red-500/15 text-red-600',
};

function AlphaRowBlock({ a }: { a: AlphaRow }) {
  return (
    <tr className="border-b border-[color:var(--color-border)] hover:bg-[color:var(--color-muted)]">
      <td className="py-2 pr-3 font-mono text-xs">{a.id}</td>
      <td className="py-2 pr-3 font-medium">{a.name}</td>
      <td className="py-2 pr-3 text-sm">
        {ASSET_CLASS_LABEL[a.asset_class] ?? a.asset_class}
      </td>
      <td className="py-2 pr-3">
        <span
          className={`text-xs px-2 py-0.5 rounded font-mono ${
            STATUS_BADGE_CLASS[a.status] ?? 'bg-[color:var(--color-muted)]'
          }`}
        >
          {a.status}
        </span>
      </td>
      <td className="py-2 pr-3 text-sm font-mono">{a.timeframe ?? '—'}</td>
    </tr>
  );
}

export default async function DashboardPage() {
  const alphas = await fetchAlphas();

  // Bucket by asset_class for the summary chips.
  const byClass = alphas.reduce<Record<string, number>>((acc, a) => {
    acc[a.asset_class] = (acc[a.asset_class] ?? 0) + 1;
    return acc;
  }, {});
  const byStatus = alphas.reduce<Record<string, number>>((acc, a) => {
    acc[a.status] = (acc[a.status] ?? 0) + 1;
    return acc;
  }, {});

  return (
    <main className="min-h-screen px-6 py-12 mx-auto max-w-5xl">
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
        Alpha catalog from Supabase, RLS-gated public read.
        Paper PnL + kill-switch event stream wire up in W2 (KIS mock) and
        expand through W4 (IBKR paper).
      </p>

      {/* Summary chips */}
      <section className="mb-10">
        <h2 className="text-xl font-bold mb-4">Catalog snapshot</h2>
        {alphas.length === 0 ? (
          <div className="p-5 border border-[color:var(--color-border)] rounded-lg bg-[color:var(--color-muted)]">
            <p className="font-mono text-sm">
              <span className="inline-block w-2 h-2 rounded-full bg-yellow-500 mr-2"></span>
              {`No data — Supabase env vars not present at build time. (W1 D2 provisioned ${'`'}NEXT_PUBLIC_SUPABASE_URL${'`'}; if you see this on production, the build cached without env.)`}
            </p>
          </div>
        ) : (
          <>
            <div className="grid grid-cols-2 md:grid-cols-4 gap-3 mb-4">
              <div className="p-4 border border-[color:var(--color-border)] rounded-lg">
                <p className="text-xs text-[color:var(--color-muted-foreground)] mb-1">
                  Total alphas
                </p>
                <p className="text-2xl font-bold">{alphas.length}</p>
              </div>
              {Object.entries(byClass).map(([cls, n]) => (
                <div
                  key={cls}
                  className="p-4 border border-[color:var(--color-border)] rounded-lg"
                >
                  <p className="text-xs text-[color:var(--color-muted-foreground)] mb-1">
                    {ASSET_CLASS_LABEL[cls] ?? cls}
                  </p>
                  <p className="text-2xl font-bold">{n}</p>
                </div>
              ))}
            </div>
            <div className="flex flex-wrap gap-2 text-xs">
              {Object.entries(byStatus).map(([s, n]) => (
                <span
                  key={s}
                  className={`px-2 py-1 rounded font-mono ${
                    STATUS_BADGE_CLASS[s] ?? 'bg-[color:var(--color-muted)]'
                  }`}
                >
                  {s}: {n}
                </span>
              ))}
            </div>
          </>
        )}
      </section>

      {/* Alpha table */}
      {alphas.length > 0 && (
        <section className="mb-10">
          <h2 className="text-xl font-bold mb-4">Alpha catalog (live)</h2>
          <div className="overflow-x-auto border border-[color:var(--color-border)] rounded-lg">
            <table className="min-w-full text-sm">
              <thead className="bg-[color:var(--color-muted)] text-left">
                <tr>
                  <th className="py-2 px-3 font-mono text-xs">ID</th>
                  <th className="py-2 px-3">Name</th>
                  <th className="py-2 px-3">Asset class</th>
                  <th className="py-2 px-3">Status</th>
                  <th className="py-2 px-3 font-mono text-xs">Timeframe</th>
                </tr>
              </thead>
              <tbody>
                {alphas.map((a) => (
                  <AlphaRowBlock key={a.id} a={a} />
                ))}
              </tbody>
            </table>
          </div>
        </section>
      )}

      <section className="mb-10">
        <h2 className="text-xl font-bold mb-4">What lands next</h2>
        <ul className="space-y-2 leading-relaxed text-sm">
          <li>
            <strong>W2:</strong> KIS mock paper PnL ingest from{' '}
            <code>trades_paper</code>, first A11 sector-rotation cells.
          </li>
          <li>
            <strong>W4:</strong> IBKR paper ingest (port 7497), A15~A18 US
            equity layer.
          </li>
          <li>
            <strong>W6:</strong> Realtime kill-switch event stream from{' '}
            <code>kill_switch_log</code>.
          </li>
          <li>
            <strong>W8:</strong> Backtest grid (DSR, PBO, sensitivity) on the
            full alpha set.
          </li>
          <li>
            <strong>W11:</strong> Public read-only API at <code>/api/v1/*</code>{' '}
            for anyone who wants to verify the numbers without scraping.
          </li>
        </ul>
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
