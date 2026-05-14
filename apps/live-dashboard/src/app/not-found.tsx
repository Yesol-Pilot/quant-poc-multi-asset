import Link from 'next/link';

export const metadata = {
  title: 'Not found · quant-poc-multi-asset',
  description: '404 — the page does not exist (yet).',
};

export default function NotFound() {
  return (
    <main className="min-h-screen px-6 py-12 mx-auto max-w-2xl">
      <p className="text-sm font-mono text-[color:var(--color-muted-foreground)] mb-2">
        404 · page not found
      </p>
      <h1 className="text-4xl md:text-5xl font-bold tracking-tight mb-4">
        The route you wanted doesn't exist{' '}
        <span className="text-[color:var(--color-muted-foreground)]">(yet)</span>
        .
      </h1>
      <p className="text-lg text-[color:var(--color-muted-foreground)] mb-6">
        Most pages on this site land in W2~W12 of the build. If you got here
        from a link, the link is from the future. If you got here by guessing,
        good guess — there's probably a route at that path eventually.
      </p>
      <div className="flex flex-wrap gap-3">
        <Link
          href="/"
          className="px-5 py-2.5 bg-[color:var(--color-primary)] text-[color:var(--color-primary-foreground)] rounded-lg font-medium hover:opacity-90 transition"
        >
          Home
        </Link>
        <Link
          href="/about"
          className="px-5 py-2.5 border border-[color:var(--color-border)] rounded-lg font-medium hover:bg-[color:var(--color-muted)] transition"
        >
          About the project
        </Link>
        <a
          href="https://github.com/Yesol-Pilot/quant-poc-multi-asset"
          className="px-5 py-2.5 border border-[color:var(--color-border)] rounded-lg font-medium hover:bg-[color:var(--color-muted)] transition"
        >
          GitHub
        </a>
      </div>
    </main>
  );
}
