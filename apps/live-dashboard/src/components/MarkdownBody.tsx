import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import rehypeSlug from 'rehype-slug';
import rehypeAutolinkHeadings from 'rehype-autolink-headings';

/**
 * Server-rendered markdown body. Used by /research/[slug] and /design/[slug].
 *
 * - `remark-gfm`: tables, strikethrough, task lists
 * - `rehype-slug` + `rehype-autolink-headings`: stable anchor IDs for headings
 *   + clickable "#" link icon. Required for ToC + deep linking.
 *
 * Styling: Tailwind `prose` (from @tailwindcss/typography). Dark-mode tokens
 * inherit from `globals.css` since the plugin uses CSS variables only.
 */
export function MarkdownBody({ source }: { source: string }) {
  return (
    <article className="prose prose-neutral dark:prose-invert max-w-none prose-headings:font-bold prose-headings:tracking-tight prose-pre:bg-[color:var(--color-muted)] prose-code:before:content-none prose-code:after:content-none prose-a:underline">
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        rehypePlugins={[
          rehypeSlug,
          [
            rehypeAutolinkHeadings,
            {
              behavior: 'append',
              properties: {
                className: ['heading-anchor'],
                ariaLabel: 'Anchor',
              },
              content: { type: 'text', value: ' #' },
            },
          ],
        ]}
      >
        {source}
      </ReactMarkdown>
    </article>
  );
}
