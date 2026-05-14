import type { NextConfig } from 'next';
import createNextIntlPlugin from 'next-intl/plugin';

const withNextIntl = createNextIntlPlugin('./src/i18n/request.ts');

const nextConfig: NextConfig = {
  reactStrictMode: true,

  // Subpath deployment under heoyesol.kr/quant (when integrated via rewrites)
  // Standalone: keep basePath empty; integration handled by Vercel rewrites
  basePath: process.env.NEXT_PUBLIC_BASE_PATH || '',

  // typedRoutes intentionally disabled for W1 scaffold:
  // - Landing page has placeholder `href: '#'` strings in a .map() that
  //   can't satisfy the RouteImpl<string> constraint.
  // - Re-enable in W3+ once /dashboard has real typed routes wired.
  // Reference: https://nextjs.org/docs/app/api-reference/config/next-config-js/typedRoutes
  experimental: {
    optimizePackageImports: ['@tremor/react', 'lucide-react'],
  },

  // Security headers (basic; refined in middleware later)
  async headers() {
    return [
      {
        source: '/(.*)',
        headers: [
          { key: 'X-Frame-Options', value: 'DENY' },
          { key: 'X-Content-Type-Options', value: 'nosniff' },
          { key: 'Referrer-Policy', value: 'strict-origin-when-cross-origin' },
          {
            key: 'Permissions-Policy',
            value: 'camera=(), microphone=(), geolocation=()',
          },
        ],
      },
    ];
  },

  // Image domains
  images: {
    remotePatterns: [
      { protocol: 'https', hostname: 'avatars.githubusercontent.com' },
      { protocol: 'https', hostname: 'github.com' },
    ],
  },

  // Disable telemetry phone-home
  // (export NEXT_TELEMETRY_DISABLED=1 in CI)
};

export default withNextIntl(nextConfig);
