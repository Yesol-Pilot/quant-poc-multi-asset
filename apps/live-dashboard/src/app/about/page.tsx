import Link from 'next/link';

export const metadata = {
  title: 'About · quant-poc-multi-asset',
  description:
    '12-week, single-developer multi-asset quant project — what we build, why we publish failures openly, who maintains it.',
};

export default function AboutPage() {
  return (
    <main className="min-h-screen px-6 py-12 mx-auto max-w-3xl">
      <nav className="mb-8 text-sm">
        <Link
          href="/"
          className="text-[color:var(--color-muted-foreground)] hover:text-[color:var(--color-fg)]"
        >
          ← Home
        </Link>
      </nav>

      <h1 className="text-3xl md:text-4xl font-bold mb-6">About this project</h1>

      <section className="mb-10 space-y-4 leading-relaxed">
        <p>
          <strong>quant-poc-multi-asset</strong> is a 12-week, single-developer
          public build of a multi-asset quantitative trading research stack —
          Korean equities (KIS Developers, mock API only), US equities & ETFs
          (IBKR paper), US options (IBKR paper), and an archived crypto layer
          from the preceding 38-day proof-of-concept.
        </p>
        <p>
          The crypto PoC ran from 2026-04-05 to 2026-05-12. It executed 191
          paper trades with a 37.7% win rate and a{' '}
          <span className="honest-failure">−15.1%</span> paper PnL. We then{' '}
          <em>closed the experiment honestly</em> and pivoted to this rebuild —
          publishing the loss and the lessons before publishing the next alpha.
        </p>
        <p>
          Every alpha here will report Deflated Sharpe Ratio (DSR), Probability
          of Backtest Overfitting (PBO), and sensitivity sweep results. Every
          deployment passes through a 12-layer kill switch that traces its
          lineage to the PoC's production wiring.
        </p>
      </section>

      <section className="mb-10">
        <h2 className="text-2xl font-bold mb-4">5-Dimension Excellence</h2>
        <p className="mb-4 text-[color:var(--color-muted-foreground)]">
          The project is judged on five axes simultaneously. Code quality and
          academic rigor are not optional. Public openness is the constraint
          that makes the whole thing legible.
        </p>
        <ul className="space-y-3">
          <li>
            <strong>D1 Code.</strong> 1,000+ tests, 90% line coverage, CI guards
            preventing live broker endpoints from entering source.
          </li>
          <li>
            <strong>D2 Academic.</strong> One SSRN submission documenting the
            38-day failure as a 1-person multi-strategy case study. One
            ReScience replication of a public-source Korean factor paper.
            arXiv preprints are on hold while the EthicaAI + WhyLab manuscripts
            are in double-blind review.
          </li>
          <li>
            <strong>D3 OSS.</strong> MIT license, public GitHub, ADRs, weekly
            progress reports auto-pushed to Telegram + this site.
          </li>
          <li>
            <strong>D4 Live.</strong> Lighthouse ≥95, public read-only API for
            paper-trade metrics, Realtime channel for kill-switch events.
          </li>
          <li>
            <strong>D5 Community.</strong> Substack for the weekly retrospective,
            Reddit/Hacker News for milestones, Korean/English dual-track posts.
          </li>
        </ul>
      </section>

      <section className="mb-10">
        <h2 className="text-2xl font-bold mb-4">What this site is not</h2>
        <p className="leading-relaxed">
          This is <strong>not</strong> a career portfolio. It does not pitch the
          maintainer for hire, it does not collect résumés, and it does not host
          author-identity content. For career inquiries, the canonical surface
          is{' '}
          <a
            href="https://heoyesol.kr"
            className="underline hover:text-[color:var(--color-fg)]"
          >
            heoyesol.kr
          </a>{' '}
          — a separate main site maintained by the same author. This site
          focuses on the project alone.
        </p>
      </section>

      <section className="mb-10">
        <h2 className="text-2xl font-bold mb-4">Maintainer</h2>
        <p className="leading-relaxed">
          Yesol Huh (허예솔). One developer, one repository, 12 weeks. Strategy
          and supervision are partially automated through a fleet of
          configuration-driven agents; every commit is reviewed by a human
          before push, and every kill-switch invariant is verified in CI before
          merge.
        </p>
        <p className="mt-3 leading-relaxed">
          GitHub:{' '}
          <a
            href="https://github.com/Yesol-Pilot/quant-poc-multi-asset"
            className="underline hover:text-[color:var(--color-fg)]"
          >
            Yesol-Pilot/quant-poc-multi-asset
          </a>
          .
        </p>
      </section>

      <section className="mb-10">
        <h2 className="text-2xl font-bold mb-4">License</h2>
        <p>
          MIT. See{' '}
          <a
            href="https://github.com/Yesol-Pilot/quant-poc-multi-asset/blob/main/LICENSE"
            className="underline hover:text-[color:var(--color-fg)]"
          >
            LICENSE
          </a>
          .
        </p>
      </section>

      <section className="mb-4">
        <h2 className="text-2xl font-bold mb-4">Important</h2>
        <p>
          Read the{' '}
          <Link href="/disclaimer" className="underline">
            full disclaimer
          </Link>
          {' '}before reading anything else on this site.{' '}
          <strong>This is research, not financial advice.</strong>
        </p>
      </section>
    </main>
  );
}
