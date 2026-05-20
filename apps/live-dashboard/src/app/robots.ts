import type { MetadataRoute } from 'next';

const BASE_URL = 'https://quant.heoyesol.kr';

/**
 * robots.txt — generated at build time.
 *
 * Open crawl for everything except API surfaces (which return JSON, not pages).
 * Internal-only paths can be added to `disallow` later.
 */
export default function robots(): MetadataRoute.Robots {
  return {
    rules: [
      // AI search engines / agents — explicit full allow (agent-era visibility)
      { userAgent: 'GPTBot', allow: '/' },
      { userAgent: 'ChatGPT-User', allow: '/' },
      { userAgent: 'OAI-SearchBot', allow: '/' },
      { userAgent: 'PerplexityBot', allow: '/' },
      { userAgent: 'ClaudeBot', allow: '/' },
      { userAgent: 'anthropic-ai', allow: '/' },
      { userAgent: 'Google-Extended', allow: '/' },
      { userAgent: 'Applebot-Extended', allow: '/' },
      { userAgent: 'CCBot', allow: '/' },
      // general crawlers
      {
        userAgent: '*',
        allow: '/',
        disallow: ['/api/'],
      },
    ],
    sitemap: `${BASE_URL}/sitemap.xml`,
    host: BASE_URL,
  };
}
