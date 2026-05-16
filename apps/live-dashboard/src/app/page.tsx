import Link from 'next/link';

export default function HomePage() {
  return (
    <main className="min-h-screen px-6 py-12 mx-auto max-w-5xl">
      {/* Hero — Honest Failure framing */}
      <section className="mb-16">
        <p className="text-sm font-mono text-[color:var(--color-muted-foreground)] mb-2">
          quant-poc-multi-asset · Week 1 of 12 · open source
        </p>
        <h1 className="text-4xl md:text-6xl font-bold tracking-tight mb-4">
          38-day Crypto PoC returned{' '}
          <span className="honest-failure">−15.1%</span>
          <span className="text-[color:var(--color-muted-foreground)]">.</span>
        </h1>
        <p className="text-xl md:text-2xl text-[color:var(--color-muted-foreground)] mb-6">
          We published the failure. Now we're rebuilding across 4 asset classes,
          openly, with academic rigor.
        </p>
        <div className="flex flex-wrap gap-3">
          <a
            href="https://github.com/Yesol-Pilot/quant-poc-multi-asset"
            target="_blank"
            rel="noopener noreferrer"
            className="px-5 py-2.5 bg-[color:var(--color-primary)] text-[color:var(--color-primary-foreground)] rounded-lg font-medium hover:opacity-90 transition"
          >
            ⭐ Star on GitHub
          </a>
          <Link
            href="/dashboard"
            className="px-5 py-2.5 border border-[color:var(--color-border)] rounded-lg font-medium hover:bg-[color:var(--color-muted)] transition"
          >
            Live Dashboard →
          </Link>
        </div>
      </section>

      {/* 5-Dimension Progress (placeholder for W1) */}
      <section className="mb-16">
        <h2 className="text-2xl font-bold mb-6">5-Dimension Excellence</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-4">
          {[
            { d: 'D1 Code', target: '1,000+ tests / 90% cov', status: 'in progress' },
            { d: 'D2 Academic', target: 'SSRN 1 + ReScience 1', status: 'planned' },
            { d: 'D3 OSS', target: '300~600 GitHub stars', status: 'live' },
            { d: 'D4 Live', target: 'Lighthouse 95+', status: 'scaffold' },
            { d: 'D5 Community', target: 'Newsletter 100~800', status: 'planned' },
          ].map((dim) => (
            <div
              key={dim.d}
              className="p-4 border border-[color:var(--color-border)] rounded-lg"
            >
              <h3 className="font-bold mb-1">{dim.d}</h3>
              <p className="text-sm text-[color:var(--color-muted-foreground)] mb-2">
                {dim.target}
              </p>
              <span className="text-xs px-2 py-0.5 bg-[color:var(--color-muted)] rounded font-mono">
                {dim.status}
              </span>
            </div>
          ))}
        </div>
      </section>

      {/* 4 Asset Classes */}
      <section className="mb-16">
        <h2 className="text-2xl font-bold mb-6">4 Asset Classes (12-week build)</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {[
            {
              name: '🇰🇷 Korean Equities',
              broker: 'KIS Developers (mock)',
              alphas: 'A11~A14 (Sector Rotation / Mean Reversion / Pair / PEAD)',
              week: 'W2~3',
            },
            {
              name: '🇺🇸 US Equities & ETFs',
              broker: 'IBKR paper',
              alphas: 'A15~A18 (Factor / Risk Parity / PEAD / Sector Momentum)',
              week: 'W4~6',
            },
            {
              name: '📈 US Options',
              broker: 'IBKR paper',
              alphas: 'A19~A21 (Covered Call / VRP / Iron Condor)',
              week: 'W7~8',
            },
            {
              name: '₿ Crypto (archive)',
              broker: 'Binance + Bybit + OKX (read-only)',
              alphas: 'A1~A6 — 38-day PoC closure',
              week: 'archived',
            },
          ].map((a) => (
            <div
              key={a.name}
              className="p-5 border border-[color:var(--color-border)] rounded-lg"
            >
              <h3 className="text-lg font-bold mb-2">{a.name}</h3>
              <p className="text-sm font-mono mb-1">{a.broker}</p>
              <p className="text-sm text-[color:var(--color-muted-foreground)] mb-2">
                {a.alphas}
              </p>
              <span className="text-xs px-2 py-0.5 bg-[color:var(--color-muted)] rounded font-mono">
                {a.week}
              </span>
            </div>
          ))}
        </div>
      </section>

      {/* Docs links */}
      <section className="mb-16">
        <h2 className="text-2xl font-bold mb-6">Documentation</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
          {[
            {
              href: '/research',
              label: 'Research (17 reports)',
              note: '~65,000 words · 300+ refs',
            },
            {
              href: '/design',
              label: 'Design specs (4)',
              note: 'Architecture · alphas · plan',
            },
            {
              href: 'https://github.com/Yesol-Pilot/quant-poc-multi-asset/tree/main/docs/adr',
              label: 'ADRs (3)',
              note: 'Build / decision log',
              external: true,
            },
            {
              href: '#',
              label: 'Papers (SSRN / ReScience)',
              note: 'Coming W12',
              placeholder: true,
            },
          ].map((l) =>
            l.external ? (
              <a
                key={l.label}
                href={l.href}
                className="p-4 border border-[color:var(--color-border)] rounded-lg hover:bg-[color:var(--color-muted)] transition"
              >
                <p className="font-medium">{l.label}</p>
                <p className="text-xs text-[color:var(--color-muted-foreground)]">
                  {l.note}
                </p>
              </a>
            ) : l.placeholder ? (
              <div
                key={l.label}
                className="p-4 border border-dashed border-[color:var(--color-border)] rounded-lg opacity-60"
              >
                <p className="font-medium">{l.label}</p>
                <p className="text-xs text-[color:var(--color-muted-foreground)]">
                  {l.note}
                </p>
              </div>
            ) : (
              <Link
                key={l.label}
                href={l.href}
                className="p-4 border border-[color:var(--color-border)] rounded-lg hover:bg-[color:var(--color-muted)] transition"
              >
                <p className="font-medium">{l.label}</p>
                <p className="text-xs text-[color:var(--color-muted-foreground)]">
                  {l.note}
                </p>
              </Link>
            ),
          )}
        </div>
      </section>

      {/* About link */}
      <section className="mb-8">
        <p className="text-sm text-[color:var(--color-muted-foreground)]">
          Maintained by{' '}
          <a
            href="https://github.com/yesol-pilot"
            className="underline hover:text-[color:var(--color-fg)]"
          >
            Yesol Huh (허예솔)
          </a>
          . This site focuses on the project. For author identity / career
          inquiries, see{' '}
          <a
            href="https://heoyesol.kr"
            className="underline hover:text-[color:var(--color-fg)]"
          >
            heoyesol.kr
          </a>{' '}
          (separate main site).
        </p>
      </section>
    </main>
  );
}
