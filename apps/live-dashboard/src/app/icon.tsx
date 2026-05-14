import { ImageResponse } from 'next/og';

// Tells Next.js this is a static favicon — generated at build time.
export const runtime = 'edge';
export const size = { width: 32, height: 32 };
export const contentType = 'image/png';

/**
 * Favicon — the −15.1% Honest Failure anchor as glyph.
 * Black background, red-orange text. Same color logic as honest-failure span
 * in globals.css.
 */
export default function Icon() {
  return new ImageResponse(
    (
      <div
        style={{
          fontSize: 14,
          background: '#0a0a0a',
          width: '100%',
          height: '100%',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          color: '#ff6b35',
          fontWeight: 700,
          fontFamily: 'system-ui, sans-serif',
          letterSpacing: '-0.05em',
        }}
      >
        −15
      </div>
    ),
    { ...size },
  );
}
