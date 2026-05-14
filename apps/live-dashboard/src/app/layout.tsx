import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: {
    default: 'quant-poc-multi-asset',
    template: '%s | quant-poc-multi-asset',
  },
  description:
    'Honest, open source, academic-rigorous multi-asset quant project. 38-day Crypto PoC → 12-week 4-asset-class rebuild.',
  keywords: [
    'quant',
    'trading',
    'multi-asset',
    'korean-stocks',
    'us-stocks',
    'options',
    'crypto',
    'backtest',
    'deflated-sharpe-ratio',
    'ai-agent',
    'open-source',
    'honest-failure',
    'paper-trading',
    'educational',
  ],
  authors: [{ name: 'Yesol Huh', url: 'https://github.com/yesol-pilot' }],
  openGraph: {
    type: 'website',
    locale: 'ko_KR',
    alternateLocale: ['en_US'],
    url: 'https://heoyesol.kr/quant',
    siteName: 'quant-poc-multi-asset',
    title: 'quant-poc-multi-asset',
    description:
      'Honest, open source, academic-rigorous multi-asset quant project',
  },
  twitter: {
    card: 'summary_large_image',
    creator: '@yesol_pilot',
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      'max-image-preview': 'large',
      'max-snippet': -1,
    },
  },
  icons: {
    icon: '/favicon.ico',
  },
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="ko" suppressHydrationWarning>
      <body>
        {children}
        <footer className="disclaimer-footer">
          <p>
            ⚠️ Educational purpose only. Not financial advice. Not investment
            recommendation. See{' '}
            <a href="/disclaimer" className="underline">
              DISCLAIMER
            </a>{' '}
            · 자본시장법 / 가상자산이용자보호법 준수.
          </p>
        </footer>
      </body>
    </html>
  );
}
