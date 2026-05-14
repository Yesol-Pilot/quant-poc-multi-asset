import { render, screen } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import HomePage from './page';

// Helper: testing-library's getByText matches any element whose textContent
// includes the pattern, which for nested links can yield "multiple elements"
// errors (parent <p> + child <a> both match). Use getAllByText and assert
// at least one match exists.
const expectTextPresent = (pattern: RegExp | string) => {
  const matches = screen.getAllByText(pattern);
  expect(matches.length).toBeGreaterThan(0);
  return matches[0];
};

describe('HomePage (smoke)', () => {
  it('renders the Honest Failure hero with -15.1%', () => {
    render(<HomePage />);
    // The -15.1% is the core narrative anchor per Design 4 v2.0
    expectTextPresent(/−15\.1%/);
  });

  it('renders 5-Dimension Excellence cards', () => {
    render(<HomePage />);
    expectTextPresent(/5-Dimension Excellence/i);
    // 5 dimensions D1~D5
    for (const dim of ['D1 Code', 'D2 Academic', 'D3 OSS', 'D4 Live', 'D5 Community']) {
      expectTextPresent(dim);
    }
  });

  it('renders 4 asset class cards', () => {
    render(<HomePage />);
    expectTextPresent(/4 Asset Classes/i);
    expectTextPresent(/Korean Equities/i);
    expectTextPresent(/US Equities & ETFs/i);
    expectTextPresent(/US Options/i);
    expectTextPresent(/Crypto \(archive\)/i);
  });

  it('links to GitHub repo (star CTA)', () => {
    render(<HomePage />);
    // Filter by href: the GitHub repo CTA is the only link to this exact URL.
    // (Accessible-name regex selection multi-matches because emoji + nested
    // text in flex container can produce overlapping accessible nodes.)
    const allLinks = screen.getAllByRole('link');
    const repoLink = allLinks.find(
      (a) =>
        a.getAttribute('href') ===
        'https://github.com/Yesol-Pilot/quant-poc-multi-asset',
    );
    expect(repoLink).toBeDefined();
    expect(repoLink?.textContent ?? '').toMatch(/Star on GitHub/i);
  });

  it('redirects career inquiries to heoyesol.kr main site (project-only enforcement)', () => {
    render(<HomePage />);
    // Per Design 4 v2.0: site is project-only, NOT career portfolio.
    // getByRole({ name: /heoyesol\.kr/i }) yields multi-element error because
    // accessible-name calculation can match both the visible link and ancestors
    // with overlapping text. Filter directly by href instead.
    const allLinks = screen.getAllByRole('link');
    const heoyesolLink = allLinks.find(
      (a) => a.getAttribute('href') === 'https://heoyesol.kr',
    );
    expect(heoyesolLink).toBeDefined();
    expect(heoyesolLink).toHaveAttribute('href', 'https://heoyesol.kr');
    expectTextPresent(/This site focuses on the project/i);
  });
});
