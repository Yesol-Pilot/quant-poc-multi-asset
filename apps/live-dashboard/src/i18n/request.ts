/**
 * next-intl request config — Week 1 scaffold.
 *
 * Wire-up timing:
 *   W1 (this commit) : config + message catalogs only; page.tsx unchanged.
 *   W2               : middleware.ts + [locale] route restructure + useTranslations() in pages.
 *
 * The dual-locale default is intentionally `ko` (Korean) because the primary
 * audience for the Honest Failure narrative is Korean retail learners and the
 * KIS Developers integration. English (`en`) is the SEO and recruiter-overflow
 * locale.
 */
import { getRequestConfig } from 'next-intl/server';

export const locales = ['ko', 'en'] as const;
export const defaultLocale = 'ko' as const;
export type Locale = (typeof locales)[number];

export default getRequestConfig(async ({ locale }) => {
  const resolved = (locales as readonly string[]).includes(locale)
    ? (locale as Locale)
    : defaultLocale;

  return {
    locale: resolved,
    messages: (await import(`../../messages/${resolved}.json`)).default,
    timeZone: 'Asia/Seoul',
  };
});
