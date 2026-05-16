/**
 * Filesystem reader for the project's documentation corpus.
 *
 * Reads `docs/research/*.md` and `docs/design/*.md` from the *repo root*
 * (two levels up from `apps/live-dashboard/`). Each file becomes a page
 * at `/research/<slug>` or `/design/<slug>` where slug = filename minus
 * `.md` extension. The title comes from the first `# heading`; the
 * description comes from the first non-quote, non-empty paragraph that
 * follows.
 *
 * Called from React Server Components only. Do not import from
 * "use client" components — `fs` is unavailable in the browser bundle.
 */
import fs from 'node:fs';
import path from 'node:path';

const REPO_ROOT = path.resolve(process.cwd(), '..', '..');
const RESEARCH_DIR = path.join(REPO_ROOT, 'docs', 'research');
const DESIGN_DIR = path.join(REPO_ROOT, 'docs', 'design');

export type DocSection = 'research' | 'design';

export type DocMeta = {
  slug: string;       // filename without .md, e.g. "01-korea-securities-job-market"
  title: string;      // first # heading content
  description: string; // first non-quote prose paragraph (trimmed, max ~280 chars)
  wordCount: number;
  section: DocSection;
};

export type DocFull = DocMeta & {
  body: string;       // full markdown source (the # heading is stripped — we render title separately)
};

function dirFor(section: DocSection): string {
  return section === 'research' ? RESEARCH_DIR : DESIGN_DIR;
}

function parseFirstHeading(md: string): string {
  for (const line of md.split('\n')) {
    const trimmed = line.trim();
    if (trimmed.startsWith('# ') && !trimmed.startsWith('## ')) {
      return trimmed.slice(2).trim();
    }
  }
  return '';
}

function parseFirstParagraph(md: string): string {
  // Skip the title line + any blockquote (e.g. "> 작성: 2026-05-14")
  // and grab the first non-empty prose paragraph.
  const lines = md.split('\n');
  let titleSeen = false;
  let collecting: string[] = [];

  for (const raw of lines) {
    const line = raw.replace(/\r$/, '');
    if (!titleSeen) {
      if (line.startsWith('# ')) titleSeen = true;
      continue;
    }
    const stripped = line.trim();
    if (stripped.startsWith('>')) continue;
    if (stripped.startsWith('#')) {
      if (collecting.length > 0) break;
      continue;
    }
    if (stripped === '') {
      if (collecting.length > 0) break;
      continue;
    }
    if (stripped.startsWith('---')) {
      if (collecting.length > 0) break;
      continue;
    }
    collecting.push(stripped);
  }

  const joined = collecting.join(' ').replace(/\s+/g, ' ').trim();
  return joined.length > 280 ? joined.slice(0, 277) + '…' : joined;
}

function stripTitleLine(md: string): string {
  const lines = md.split('\n');
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (line === undefined) continue;
    const trimmed = line.trim();
    if (trimmed.startsWith('# ') && !trimmed.startsWith('## ')) {
      return [...lines.slice(0, i), ...lines.slice(i + 1)].join('\n');
    }
  }
  return md;
}

function countWords(md: string): number {
  // Strip code blocks first so we don't count fences/syntax noise.
  const stripped = md
    .replace(/```[\s\S]*?```/g, ' ')
    .replace(/`[^`]+`/g, ' ')
    .replace(/[#*_>|\-]/g, ' ');
  const tokens = stripped.split(/\s+/).filter(Boolean);
  return tokens.length;
}

export function getDocList(section: DocSection): DocMeta[] {
  let entries: string[];
  try {
    entries = fs.readdirSync(dirFor(section));
  } catch {
    return [];
  }
  const docs = entries
    .filter((f) => f.endsWith('.md') && !f.toLowerCase().startsWith('readme'))
    .map((file) => {
      const slug = file.replace(/\.md$/, '');
      const fullPath = path.join(dirFor(section), file);
      const raw = fs.readFileSync(fullPath, 'utf-8');
      const title = parseFirstHeading(raw) || slug;
      const description = parseFirstParagraph(raw);
      return {
        slug,
        title,
        description,
        wordCount: countWords(raw),
        section,
      } satisfies DocMeta;
    });
  // Numeric prefix (00-, 01-, ...) → ordered list.
  docs.sort((a, b) => a.slug.localeCompare(b.slug));
  return docs;
}

export function getDoc(section: DocSection, slug: string): DocFull | null {
  const safe = /^[a-z0-9][a-z0-9-]*$/.test(slug);
  if (!safe) return null;

  const fullPath = path.join(dirFor(section), `${slug}.md`);
  if (!fs.existsSync(fullPath)) return null;

  const raw = fs.readFileSync(fullPath, 'utf-8');
  return {
    slug,
    title: parseFirstHeading(raw) || slug,
    description: parseFirstParagraph(raw),
    wordCount: countWords(raw),
    section,
    body: stripTitleLine(raw),
  };
}
