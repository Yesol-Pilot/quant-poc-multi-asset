import { render, screen } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import HomePage from './page';

describe('HomePage (smoke)', () => {
  it('renders the Honest Failure hero with -15.1%', () => {
    render(<HomePage />);
    // The -15.1% is the core narrative anchor per Design 4 v2.0
    expect(screen.getByText(/−15\.1%/)).toBeInTheDocument();
  });

  it('renders 5-Dimension Excellence cards', () => {
    render(<HomePage />);
    expect(screen.getByText(/5-Dimension Excellence/i)).toBeInTheDocument();
    // 5 dimensions D1~D5
    for (const dim of ['D1 Code', 'D2 Academic', 'D3 OSS', 'D4 Live', 'D5 Community']) {
      expect(screen.getByText(dim)).toBeInTheDocument();
    }
  });

  it('renders 4 asset class cards', () => {
    render(<HomePage />);
    expect(screen.getByText(/4 Asset Classes/i)).toBeInTheDocument();
    expect(screen.getByText(/Korean Equities/i)).toBeInTheDocument();
    expect(screen.getByText(/US Equities & ETFs/i)).toBeInTheDocument();
    expect(screen.getByText(/US Options/i)).toBeInTheDocument();
    expect(screen.getByText(/Crypto \(archive\)/i)).toBeInTheDocument();
  });

  it('links to GitHub repo (star CTA)', () => {
    render(<HomePage />);
    const githubLink = screen.getByText(/Star on GitHub/i).closest('a');
    expect(githubLink).toHaveAttribute(
      'href',
      'https://github.com/Yesol-Pilot/quant-poc-multi-asset',
    );
  });

  it('redirects career inquiries to heoyesol.kr main site (project-only enforcement)', () => {
    render(<HomePage />);
    // Per Design 4 v2.0: site is project-only, NOT career portfolio
    expect(screen.getByText(/heoyesol.kr/i)).toBeInTheDocument();
    expect(
      screen.getByText(/This site focuses on the project/i),
    ).toBeInTheDocument();
  });
});
