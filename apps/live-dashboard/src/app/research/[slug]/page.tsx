import Link from 'next/link';
import { notFound } from 'next/navigation';
import { getDoc, getDocList } from '@/lib/docs';
import { MarkdownBody } from '@/components/MarkdownBody';

export const dynamicParams = false; // 404 anything not in generateStaticParams

export function generateStaticParams() {
  return getDocList('research').map((d) => ({ slug: d.slug }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const doc = getDoc('research', slug);
  if (!doc) return { title: 'Not found · Research' };
  return {
    title: `${doc.title} · Research`,
    description: doc.description,
  };
}

export default async function ResearchSlugPage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const doc = getDoc('research', slug);
  if (!doc) notFound();

  return (
    <main className="min-h-screen px-6 py-12 mx-auto max-w-3xl">
      <nav className="mb-8 text-sm flex gap-3">
        <Link
          href="/"
          className="text-[color:var(--color-muted-foreground)] hover:text-[color:var(--color-fg)]"
        >
          ← Home
        </Link>
        <span className="text-[color:var(--color-muted-foreground)]">/</span>
        <Link
          href="/research"
          className="text-[color:var(--color-muted-foreground)] hover:text-[color:var(--color-fg)]"
        >
          Research index
        </Link>
      </nav>

      <header className="mb-8">
        <p className="text-sm font-mono text-[color:var(--color-muted-foreground)] mb-2">
          Research · {doc.wordCount.toLocaleString()} words
        </p>
        <h1 className="text-3xl md:text-4xl font-bold tracking-tight mb-2">
          {doc.title}
        </h1>
        <p className="text-sm text-[color:var(--color-muted-foreground)]">
          {doc.description}
        </p>
      </header>

      <MarkdownBody source={doc.body} />

      <footer className="mt-12 pt-8 border-t border-[color:var(--color-border)] text-sm text-[color:var(--color-muted-foreground)]">
        <p>
          Source markdown:{' '}
          <a
            href={`https://github.com/Yesol-Pilot/quant-poc-multi-asset/blob/main/docs/research/${slug}.md`}
            className="underline hover:text-[color:var(--color-fg)]"
          >
            docs/research/{slug}.md
          </a>
        </p>
      </footer>
    </main>
  );
}
