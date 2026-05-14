import type { MetadataRoute } from 'next';

const BASE_URL = 'https://quant.heoyesol.kr';

/**
 * sitemap.xml — generated at build time.
 *
 * W1: static routes only (`/`, `/about`, `/disclaimer`, `/dashboard`).
 * W2+: extend with `/research/[slug]`, `/design/[slug]`, `/api-docs` etc.
 *      W3+: pull dynamic alpha pages from Supabase `alphas` table.
 */
export default function sitemap(): MetadataRoute.Sitemap {
  const now = new Date();

  return [
    {
      url: `${BASE_URL}/`,
      lastModified: now,
      changeFrequency: 'weekly',
      priority: 1.0,
    },
    {
      url: `${BASE_URL}/about`,
      lastModified: now,
      changeFrequency: 'monthly',
      priority: 0.7,
    },
    {
      url: `${BASE_URL}/disclaimer`,
      lastModified: now,
      changeFrequency: 'yearly',
      priority: 0.5,
    },
    {
      url: `${BASE_URL}/dashboard`,
      lastModified: now,
      changeFrequency: 'daily',
      priority: 0.9,
    },
  ];
}
