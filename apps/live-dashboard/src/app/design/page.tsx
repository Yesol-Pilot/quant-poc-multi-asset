import Link from 'next/link';
import { getDocList } from '@/lib/docs';

export const metadata = {
  title: 'Design specs · quant-poc-multi-asset',
  description:
    'Architecture, alpha specifications, 12-week daily plan, and live-page product spec — the design documents that turned the research backbone into a buildable 84-day schedule.',
};

export default function DesignIndexPage() {
  const docs = getDocList('design');
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
        Design specifications
      </h1>
      <p className="text-lg text-[color:var(--color-muted-foreground)] mb-2">
        The decisions made between "we have research" and "we have a working
        repo." Every alpha, every API surface, every CI guard is anchored
        somewhere here.
      </p>
      <p className="text-sm font-mono text-[color:var(--color-muted-foreground)] mb-10">
        {docs.length} specs · ~{totalWords.toLocaleString()} words
      </p>

      {docs.length === 0 ? (
        <div className="p-5 border border-[color:var(--color-border)] rounded-lg bg-[color:var(--color-muted)]">
          <p className="text-sm">
            No specs found. (Build context did not include the{' '}
            <code>docs/design/</code> directory.)
          </p>
        </div>
      ) : (
        <ul className="space-y-4">
          {docs.map((d) => (
            <li
              key={d.slug}
              className="p-5 border border-[color:var(--color-border)] rounded-lg hover:bg-[color:var(--color-muted)] transition"
            >
              <Link href={`/design/${d.slug}`} className="block group">
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
