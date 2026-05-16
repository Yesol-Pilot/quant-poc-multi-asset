import Link from 'next/link';
import { getDocList } from '@/lib/docs';

export const metadata = {
  title: 'Research · quant-poc-multi-asset',
  description:
    'Pre-launch research backbone for the 12-week quant rebuild — 17 reports / ~65,000 words / 300+ academic references covering broker APIs, regulation, factor literature, competitive landscape, and launch strategy.',
};

export default function ResearchIndexPage() {
  const docs = getDocList('research');
  const totalWords = docs.reduce((sum, d) => sum + d.wordCount, 0);

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

      <h1 className="text-3xl md:text-4xl font-bold tracking-tight mb-3">
        Research
      </h1>
      <p className="text-lg text-[color:var(--color-muted-foreground)] mb-2">
        The corpus we built before writing a single alpha line. Public source
        only — every external claim has a clickable citation.
      </p>
      <p className="text-sm font-mono text-[color:var(--color-muted-foreground)] mb-10">
        {docs.length} reports · ~{totalWords.toLocaleString()} words · 300+
        references
      </p>

      {docs.length === 0 ? (
        <div className="p-5 border border-[color:var(--color-border)] rounded-lg bg-[color:var(--color-muted)]">
          <p className="text-sm">
            No reports found. (Build context did not include the{' '}
            <code>docs/research/</code> directory — check Vercel{' '}
            <code>includeFiles</code> config.)
          </p>
        </div>
      ) : (
        <ul className="space-y-4">
          {docs.map((d) => (
            <li
              key={d.slug}
              className="p-5 border border-[color:var(--color-border)] rounded-lg hover:bg-[color:var(--color-muted)] transition"
            >
              <Link href={`/research/${d.slug}`} className="block group">
                <div className="flex items-baseline justify-between gap-3 mb-2">
                  <h2 className="text-lg font-bold group-hover:underline">
                    {d.title}
                  </h2>
                  <span className="text-xs font-mono text-[color:var(--color-muted-foreground)] shrink-0">
                    {d.wordCount.toLocaleString()} words
                  </span>
                </div>
                <p className="text-sm text-[color:var(--color-muted-foreground)]">
                  {d.description || 'No description.'}
                </p>
              </Link>
            </li>
          ))}
        </ul>
      )}
    </main>
  );
}
