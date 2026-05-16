import type { MetadataRoute } from 'next';
import { getDocList } from '@/lib/docs';

const BASE_URL = 'https://quant.heoyesol.kr';

/**
 * sitemap.xml — generated at build time.
 *
 * Static routes + every research/design doc page (slug-based).
 * W3+: pull dynamic alpha pages from Supabase `alphas` table.
 */
export default function sitemap(): MetadataRoute.Sitemap {
  const now = new Date();

  const staticRoutes: MetadataRoute.Sitemap = [
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
    {
      url: `${BASE_URL}/research`,
      lastModified: now,
      changeFrequency: 'monthly',
      priority: 0.8,
    },
    {
      url: `${BASE_URL}/design`,
      lastModified: now,
      changeFrequency: 'monthly',
      priority: 0.7,
    },
  ];

  const researchPages: MetadataRoute.Sitemap = getDocList('research').map(
    (d) => ({
      url: `${BASE_URL}/research/${d.slug}`,
      lastModified: now,
      changeFrequency: 'monthly',
      priority: 0.6,
    }),
  );

  const designPages: MetadataRoute.Sitemap = getDocList('design').map((d) => ({
    url: `${BASE_URL}/design/${d.slug}`,
    lastModified: now,
    changeFrequency: 'monthly',
    priority: 0.6,
  }));

  return [...staticRoutes, ...researchPages, ...designPages];
}
