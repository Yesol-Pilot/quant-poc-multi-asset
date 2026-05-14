import Link from 'next/link';

export const metadata = {
  title: 'Disclaimer · quant-poc-multi-asset',
  description:
    'Regulatory and risk disclaimer (Korean Capital Markets Act + US SEC). This project is research only, not investment advice, not a managed product.',
};

export default function DisclaimerPage() {
  return (
    <main className="min-h-screen px-6 py-12 mx-auto max-w-3xl">
      <nav className="mb-8 text-sm">
        <Link
          href="/"
          className="text-[color:var(--color-muted-foreground)] hover:text-[color:var(--color-fg)]"
        >
          ← Home
        </Link>
      </nav>

      <h1 className="text-3xl md:text-4xl font-bold mb-6">Disclaimer</h1>

      <p className="text-sm text-[color:var(--color-muted-foreground)] mb-10">
        Last updated: 2026-05-14. The source of truth is the{' '}
        <a
          href="https://github.com/Yesol-Pilot/quant-poc-multi-asset/blob/main/DISCLAIMER.md"
          className="underline"
        >
          DISCLAIMER.md in the repository
        </a>
        . If this page and that file ever disagree, the repository wins.
      </p>

      {/* English */}
      <section className="mb-12">
        <h2 className="text-2xl font-bold mb-4">English</h2>
        <div className="space-y-4 leading-relaxed">
          <p>
            <strong>This project is for research and educational purposes
            only.</strong> Nothing here is investment advice, a recommendation
            to buy or sell any security, derivative, or cryptocurrency, an offer
            to manage assets, or a solicitation of any kind.
          </p>
          <p>
            The maintainer is not a licensed investment adviser or broker-dealer
            in any jurisdiction. The maintainer holds <em>no</em> client funds
            and operates <em>no</em> pooled investment vehicle. All trading
            shown on this site or in the repository is paper trading executed
            against broker simulators (KIS mock API, IBKR paper port 7497,
            historical crypto exchange data).
          </p>
          <p>
            Past performance — including paper-trade performance — does not
            indicate future results. The preceding 38-day crypto PoC produced a{' '}
            <strong className="honest-failure">−15.1%</strong> paper PnL with a
            37.7% win rate across 191 trades. This was published intentionally
            to demonstrate honest reporting, not to demonstrate skill.
          </p>
          <p>
            The maintainer makes no representation or warranty as to the
            accuracy, completeness, timeliness, or fitness of any data, code, or
            documentation in this repository. Use at your own risk. By using
            this code or following any guidance herein, you agree that the
            maintainer is not liable for any loss, direct or indirect, that may
            result.
          </p>
          <p>
            All trading carries a substantial risk of loss. Options trading
            involves additional risks (theta decay, gamma risk, assignment, pin
            risk) and is not suitable for all investors. Derivatives can result
            in losses that exceed the original investment. Cryptocurrencies are
            highly volatile, may be unregulated in your jurisdiction, and can
            lose all value.
          </p>
        </div>
      </section>

      {/* Korean (자본시장법 정합) */}
      <section className="mb-12">
        <h2 className="text-2xl font-bold mb-4">한국어 (자본시장법 정합)</h2>
        <div className="space-y-4 leading-relaxed">
          <p>
            <strong>본 프로젝트는 연구·교육 목적이며 투자 권유가 아닙니다.</strong>{' '}
            이 사이트 또는 저장소에서 제공하는 어떠한 정보·코드·결과도 특정
            금융투자상품에 대한 매수/매도 권유, 자문, 일임 또는 신탁 권유로
            해석될 수 없습니다.
          </p>
          <p>
            관리자는 자본시장과 금융투자업에 관한 법률에 따른 투자자문업자 또는
            투자일임업자, 신탁업자가 아닙니다. 어떠한 고객 자금도 수탁하지
            않으며, 어떠한 풀(pool) 형태의 집합투자기구도 운영하지 않습니다.
            본 저장소에서 공개되는 모든 거래는 페이퍼(모의) 거래이며, 한국투자증권
            모의 OpenAPI(<code>openapivts.koreainvestment.com</code>), 인터랙티브
            브로커즈(IBKR) 페이퍼 계정 포트 7497, 그리고 암호화폐 거래소 과거
            데이터에 대해 시뮬레이션된 결과입니다.
          </p>
          <p>
            과거 성과(페이퍼 성과 포함)는 미래 성과를 보장하지 않습니다. 38일
            크립토 PoC는 191건의 모의 거래에 대해 승률 37.7%, 누적{' '}
            <strong className="honest-failure">−15.1%</strong>의 페이퍼 손익을
            기록했고, 이 사실은 의도적으로 공개되었습니다. 이는 "실력"의
            증명이 아니라 "정직한 보고"의 증명입니다.
          </p>
          <p>
            관리자는 본 저장소의 자료·코드·문서의 정확성, 완전성, 적시성,
            특정 목적 적합성에 대해 어떠한 보증도 하지 않습니다. 이용에 따른
            모든 책임은 이용자 본인에게 있으며, 직간접 손해에 대해 관리자는
            일체 책임지지 않습니다.
          </p>
          <p>
            모든 투자에는 원본 손실 위험이 있습니다. 옵션·파생상품 거래는 시간가치
            소멸, 감마·핀 리스크, 행사 배정 등 추가적인 위험을 수반하며 모든
            투자자에게 적합하지 않을 수 있습니다. 가상자산은 변동성이 매우
            크고 관할 법역에 따라 비규제 자산일 수 있으며 가치가 0이 될 수도
            있습니다.
          </p>
        </div>
      </section>

      {/* Live trading guards */}
      <section className="mb-12">
        <h2 className="text-2xl font-bold mb-4">
          Live trading is technically blocked
        </h2>
        <p className="leading-relaxed mb-3">
          The repository's CI workflow contains a hard guard that fails the
          build if any of the following ever appear in source:
        </p>
        <ul className="list-disc list-inside space-y-2 font-mono text-sm">
          <li>
            <code>openapi.koreainvestment.com</code> (KIS production endpoint)
          </li>
          <li>
            <code>:7496</code> (IBKR live trading port)
          </li>
          <li>
            <code>TRADING_MODE=live</code> outside of an explicit, signed
            opt-in path (which does not exist)
          </li>
        </ul>
        <p className="leading-relaxed mt-3">
          The default <code>.env.example</code> ships with{' '}
          <code>TRADING_MODE=paper</code>, <code>IBKR_PORT=7497</code>, and{' '}
          <code>KIS_BASE_URL=https://openapivts.koreainvestment.com:29443</code>{' '}
          (mock).
        </p>
      </section>

      {/* Contact */}
      <section className="mb-4">
        <h2 className="text-2xl font-bold mb-4">Contact</h2>
        <p>
          Bugs, ethics concerns, or vulnerability reports →{' '}
          <a
            href="https://github.com/Yesol-Pilot/quant-poc-multi-asset/security"
            className="underline"
          >
            GitHub Security Advisories
          </a>
          . Career inquiries →{' '}
          <a href="https://heoyesol.kr" className="underline">
            heoyesol.kr
          </a>
          .
        </p>
      </section>
    </main>
  );
}
