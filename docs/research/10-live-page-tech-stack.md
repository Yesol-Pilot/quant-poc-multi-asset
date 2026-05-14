# #10 Live page 기술 스택 + SEO/GEO

> Tier B Publish 영역 #10 / 한국 retail 1인 AI 네이티브 PM portfolio
> 작성: 2026-05-14 (Strategy Lead Claude Opus 4.7)
> Cold honest. 광고성 X. retail 1인 실제 가능한 path 만.

---

## Executive Summary (5 핵심 발견)

1. **도메인 권고: `heoyesol.kr/quant` (subdomain)** + 별도 `openquant.kr` 옵션 보류. 이유: (a) `heoyesol.kr` 이미 GA4 + Vercel 정착 → 신규 도메인 SEO 부트스트랩 6~12개월 손해, (b) 한국 retail 검색 시 `heoyesol.kr` 의 누적 authority 활용, (c) NeurIPS + TMLR 학술 citation 시 도메인 일관성 (`heoyesol.kr/quant/paper-1`), (d) 비용 $11/년 (이미 정착).

2. **기술 스택 권고: Next.js 15 + Vercel Pro + Docusaurus 3.x dual subdomain**. dynamic dashboard (실시간 paper trading metrics) 는 Next.js, 학술 documentation 은 Docusaurus. Astro 는 매력적 (40% 빠른 load, 90% less JS) 이지만 Recharts/Tremor + Supabase Realtime websocket 의 dynamic 요구 — Next.js 가 fit.

3. **Dashboard chart 권고: Tremor (Recharts wrapper)**. 이유: (a) 38일 PoC metric 시각화에 충분 (1만+ data points 불필요), (b) shadcn/ui 스타일 통일 (owner 의 11 SBU 정합), (c) Recharts 의 3.6M weekly downloads = 가장 안정적 React chart 생태계. ECharts/Plotly 는 학술 figure 용 overkill, Chart.js 는 React 친화도 낮음.

4. **SEO target keywords cold 결정**:
   - 한국어 P0: "1인 퀀트", "AI 자동매매 후기", "한국 퀀트 봇 오픈소스"
   - 영문 P0: "1-person quant portfolio", "Korean retail quant", "honest failure trading"
   - 한국어 P1: "Bayesian quant", "multi-asset 백테스트", "퀀트 38일"
   - 영문 P1: "multi-asset retail quant", "Korea stock backtest open source", "transparent quant failure"
   - keyword 가 unique → 경쟁 낮음 + owner brand 정착 가능

5. **GEO (Generative Engine Optimization) cold 권고**: llms.txt 는 symbolic only (Google 공식 발표 "no AI system uses llms.txt"). 실효 strategy = (a) Common Crawl CCBot 허용 (`robots.txt` 명시), (b) ClaudeBot / GPTBot / PerplexityBot allow, (c) 직접 답변 패턴 ("Q: ... A: ...") 콘텐츠 작성, (d) Common Crawl 누적 (cc-bot contact 이미 owner 가 record 함, 활용 가능), (e) Wikipedia notability seed (NeurIPS+TMLR cited 후 검토).

---

## 1. 도메인 결정

### 1.1 option 비교

| Option | 비용 | SEO | 신뢰도 | 12주 setup |
|---|---|---|---|---|
| `heoyesol.kr/quant` (subdomain path) | $0 추가 | A+ (기존 authority 상속) | A+ | 2h |
| `quant.heoyesol.kr` (subdomain) | $0 추가 | A (subdomain separate) | A+ | 4h |
| `openquant.kr` 별도 | $11/년 | C (신규 0 authority) | B | 8h + 6~12개월 SEO |
| `quantpoc.com` 별도 | $11/년 | C | C (한국 retail 신뢰도 약함) | 8h + 6~12개월 |
| `1personquant.com` 별도 | $11/년 | C | B | 8h + 6~12개월 |

### 1.2 한국 retail 1인 모범 사례 검토

- **개인 quant 블로거 (한국)**: 대부분 Tistory / Velog / Brunch 기반 (자체 도메인 0). 신뢰도 약함 (commodity blog hosting).
- **개인 portfolio 도메인 (한국)**: heoyesol.kr 처럼 본명 기반 도메인이 약 5~10% (전체 quant 블로거 중). 신뢰도 강함.
- **글로벌 retail quant**: Robert Carver (`qoppac.blogspot.com`) / Marcos Lopez de Prado (`quantresearch.org`) / Ernest Chan (`epchan.blogspot.com`) — 본명 + .org 또는 corp 도메인.

### 1.3 권고: `heoyesol.kr/quant` (path subdomain)

cold 이유:
- 기존 `heoyesol.kr` 의 GA4 ID + Search Console verification + Vercel project 그대로 활용
- 11 SBU portfolio 와 일관 navigation
- 학술 citation `https://heoyesol.kr/quant/paper-2026-01` 가 BibTeX `url=` 에 영구 valid (도메인 별도 시 owner 가 서비스 종료하면 dead link)
- subdomain (`quant.heoyesol.kr`) 보다 path (`heoyesol.kr/quant`) 가 SEO 합산 강점 (Google 의 subdomain vs subdirectory 논쟁 — 2026 기준 subdirectory 우세)

### 1.4 별도 `openquant.kr` 또는 `1personquant.com` 검토

12개월 후 stars > 2,000 + sponsorship > $300/월 도달 시점에 검토. 12주 plan 안에서는 비권고 (분산 비용 > 학습 이득).

---

## 2. 기술 스택

### 2.1 Next.js 15 vs Astro 5 cold 비교

| 항목 | Next.js 15 | Astro 5 |
|---|---|---|
| First Load JS | 80~120 KB | 5~30 KB |
| Lighthouse Performance | 80~90 | 95~100 |
| Real-time websocket | Native (App Router + Server Components) | Possible (Islands) but verbose |
| i18n | Built-in (next-intl + middleware) | 약함 (third-party astro-i18next) |
| Hosting | Vercel native | Cloudflare Pages 최적 |
| Build time (1,000 pages) | 60~120s | 10~30s |
| Learning curve | 중상 | 중하 |
| 외부 contributor 친화 | A+ (React 표준) | B (Astro Islands 학습 필요) |

### 2.2 권고: Next.js 15 + Vercel Pro (subdomain) + Docusaurus (docs)

**근거**:
- owner 의 11 SBU 가 모두 Next.js → 학습/유지 cost 0
- Vercel Pro $20/월 이미 owner 가 사용 (재배포 cost 0)
- dynamic dashboard (실시간 trading metrics WebSocket) 가 핵심 — Astro 의 Islands 가 가능하지만 Next.js 가 더 자연스러움
- Docusaurus 는 학술 docs 영역만 (`/docs` path 또는 별도 subdomain)

**대안 (Astro 진영 강함)**:
- Astro 5 + Cloudflare Pages = $0/월 (Vercel Pro 의 $20/월 절감)
- 12개월 후 owner 가 11 SBU 일부를 Astro 마이그레이션 검토 가능 (현 시점 X)

### 2.3 Documentation framework cold 비교

| 항목 | Docusaurus 3.x | Nextra 4 | MkDocs Material |
|---|---|---|---|
| i18n (한+영) | A+ (built-in React-Intl) | B (Next.js i18n) | C (mkdocs-i18n plugin) |
| Versioning | A+ | B | A (mike plugin) |
| MDX support | A+ | A+ (Next.js native) | C (raw markdown only) |
| Plugin ecosystem | A+ (50+ official) | B | A |
| Setup time | 8 min | 3 min | 60 sec |
| 2026 maintenance status | Active | Active | **Maintenance mode (Nov 2025)** |
| 외부 contributor 친화 | A (React 표준) | A (Next.js) | B (Python knowledge) |

**권고**: **Docusaurus 3.x**. 이유:
- 한국+영문 i18n 가 Docusaurus 의 강점
- versioning (12주 plan 의 1.0 → 2.0 학습 진화 시각화)
- React 표준 → owner Next.js 경험 활용
- MkDocs Material 의 maintenance mode 진입 (2025-11) 은 risk
- Nextra 는 Next.js 표준이지만 i18n 약함

### 2.4 단일 stack 시나리오 (간소화 권고)

`heoyesol.kr/quant` 안에 모두 Next.js 로 통합:
- `/quant` = dashboard (실시간 chart, Tremor)
- `/quant/docs` = MDX-based docs (Next.js App Router)
- `/quant/blog` = 학술 update blog
- `/quant/api` = public API endpoint

장점: 단일 codebase, single deploy. 단점: docs versioning 약함.

**12주 plan 권고**: 단일 Next.js stack 시작, docs versioning 필요 시 (12개월 후) Docusaurus 분리.

---

## 3. Dashboard 실시간 chart

### 3.1 React chart library cold 비교

| Library | Weekly DL | Bundle | 강점 | 약점 |
|---|---|---|---|---|
| Recharts | 3.6M | 410 KB | React virtual DOM 친화, SVG | 10k+ data points 느림 |
| Chart.js | 5.2M | 200 KB | Canvas, 안정적 | React 통합 verbose |
| Plotly.js | 600K | 3.5 MB | 학술 figure, 3D, 통계 차트 | Bundle 거대, overkill |
| ECharts | 1.4M | 1.0 MB | 100k+ data points, Canvas | API verbose, China focus |
| Tremor | 200K | Recharts 의존 | shadcn/ui 스타일 | Recharts 한계 상속 |
| Visx (Airbnb) | 300K | tree-shakable | D3 wrapper | 학습 곡선 |
| Nivo | 250K | 600 KB | 다양한 chart type | maintenance 감소 |

### 3.2 권고: Tremor (Recharts wrapper)

**근거**:
- 38일 PoC metric 시각화 = 일일/주간/월간 + 4 asset 비교 → 10k data points 절대 도달 안 함
- shadcn/ui 스타일 정합 (owner 의 11 SBU 시각 일관성)
- Recharts 3.6M weekly downloads 의 안정성 상속
- Tremor 자체 200K weekly downloads, Vercel founder Guillermo Rauch 추천

**비권고**:
- Plotly: 학술 figure 에는 좋지만 dashboard overkill, 3.5MB bundle 으로 Lighthouse 점수 하락
- ECharts: 100k+ data points 필요할 때 (1인 retail 절대 도달 X)
- D3 direct: 학습 곡선 + 1인 운영 cost

### 3.3 실시간 paper trading metrics (WebSocket via Supabase Realtime)

```typescript
// Next.js App Router + Supabase Realtime
import { createBrowserClient } from '@supabase/ssr'

const supabase = createBrowserClient(URL, ANON_KEY)

useEffect(() => {
  const channel = supabase
    .channel('quant-trades')
    .on('postgres_changes', {
      event: 'INSERT',
      schema: 'public',
      table: 'paper_trades'
    }, (payload) => {
      setTrades((prev) => [...prev, payload.new])
    })
    .subscribe()
  return () => supabase.removeChannel(channel)
}, [])
```

cold 주의:
- Supabase Pro 의 Realtime = 500 동시 connections (1인 retail 의 visitor 가 동시 500 이상 도달 가능성 6개월 내 ~10% — 12주 plan 안에서 무시 가능)
- egress 250GB/월 — chart 데이터 자체는 작지만, polling vs websocket 결정 필요 (websocket 권고)

### 3.4 4 자산군 visualization 권고 레이아웃

```
┌─────────────────────────────────────────┐
│ Hero: 38-day PoC overview               │
│  WR 37.7% | PnL -15.1% | Sharpe 0.0    │
├─────────────────────────────────────────┤
│ Live Paper Trading (last 7 days)        │
│  [Line chart: cumulative PnL by asset]  │
├──────────────────┬──────────────────────┤
│ Korean stocks    │ US options           │
│  [bar: WR]       │  [bar: WR]           │
├──────────────────┼──────────────────────┤
│ Crypto perps     │ Multi-asset combined │
│  [bar: WR]       │  [scatter: alpha]    │
├─────────────────────────────────────────┤
│ Recent trades table (last 20)           │
└─────────────────────────────────────────┘
```

---

## 4. Supabase Pro 활용

### 4.1 권고 schema

```sql
-- 1. 학술 references (D6 62 references + 신규)
create table public.academic_references (
  id uuid primary key default gen_random_uuid(),
  title text not null,
  authors text[] not null,
  year int not null,
  doi text,
  url text,
  category text,  -- "MARL", "CausalSafety", "Quant", etc.
  created_at timestamp default now()
);

-- 2. Portfolio metadata (4 asset)
create table public.portfolio_assets (
  symbol text primary key,
  asset_class text not null,  -- "kr_equity", "us_option", "crypto_perp", "us_etf"
  full_name text,
  market text,  -- "KOSPI", "NASDAQ", "BINANCE"
  added_at timestamp default now()
);

-- 3. Paper trades (realtime feed)
create table public.paper_trades (
  id bigserial primary key,
  symbol text references public.portfolio_assets(symbol),
  side text check (side in ('long', 'short')),
  qty numeric not null,
  entry_price numeric not null,
  entry_time timestamp not null,
  exit_price numeric,
  exit_time timestamp,
  pnl_pct numeric,
  alpha_id text  -- "A1_liquidation_cascade", "A4_macro_event", etc.
);

-- 4. Daily metrics (aggregated)
create table public.daily_metrics (
  date date primary key,
  total_trades int,
  win_rate numeric,
  pnl_pct numeric,
  sharpe numeric,
  max_dd numeric,
  liquidations_observed int
);

-- 5. GA4 events mirror (analytics, optional)
create table public.page_events (
  id bigserial primary key,
  path text not null,
  event_name text not null,
  user_session_hash text,  -- IP hash, no PII
  ts timestamp default now()
);
```

### 4.2 Branching (test env)

Supabase Pro 의 branching = test/prod 분리. 권고 flow:
- `main` branch = production (heoyesol.kr/quant)
- `dev` branch = local development
- `staging` branch = pre-production verification (12주 plan 의 W10 도입)

### 4.3 Daily backups + PITR

Supabase Pro 의 PITR (Point-in-Time Recovery) = 7일 retention. 권고:
- 자동 daily backup (Supabase 기본 — 추가 cost 0)
- 외부 backup (월 1회 `pg_dump` 로 Cloudflare R2 / S3 저장 — quant 데이터 영구 보존 학술 가치)
- Backup script GitHub Actions 권고 (월 1회 cron)

### 4.4 8GB DB + 250GB egress

cold 측정:
- 38일 PoC 의 paper_trades = 191 rows × 200 bytes = 38KB
- 12주 plan 종료 시점 paper_trades = 3,000 rows × 200 bytes = 600KB
- liquidation_events = 60일 × 5,000 events/일 × 100 bytes = 30MB
- academic_references = 62 rows × 1KB = 62KB
- **총합 < 100MB** → 8GB 한계의 1.25% 사용 (한도 여유 100배)

egress 250GB/월:
- visitor 1,000/일 × chart load 50KB × 30일 = 1.5GB/월 → 한도의 0.6%
- 100,000 visitors/일 (실현 안 됨) 도달 시 한도 60% — 12개월 안에서 무시 가능

**결론**: Supabase Pro $25/월 이 12주 plan 충분. Free tier ($0) 도 가능하지만 Pro 의 Realtime 500 connections + PITR + branching 가치 명확.

---

## 5. SEO / GEO 최적화

### 5.1 Google Search Console + Bing Webmaster + IndexNow

**필수 setup (12주 plan W1)**:
- Google Search Console = `heoyesol.kr` 이미 verify (owner 정착)
- Bing Webmaster Tools = `heoyesol.kr` 신규 추가 (Bing index = ChatGPT-via-Bing-search citation 의 backbone)
- IndexNow = Bing + Yandex 즉시 index 신호 (`<your-key>.txt` root upload)

### 5.2 한국 + 영문 sitemap 분리

```xml
<!-- /sitemap.xml -->
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap>
    <loc>https://heoyesol.kr/sitemap-quant-en.xml</loc>
    <lastmod>2026-05-14</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://heoyesol.kr/sitemap-quant-ko.xml</loc>
    <lastmod>2026-05-14</lastmod>
  </sitemap>
</sitemapindex>
```

각 언어 sitemap 안에 hreflang 명시:
```xml
<url>
  <loc>https://heoyesol.kr/quant</loc>
  <xhtml:link rel="alternate" hreflang="en" href="https://heoyesol.kr/quant"/>
  <xhtml:link rel="alternate" hreflang="ko" href="https://heoyesol.kr/quant/ko"/>
</url>
```

### 5.3 Target keywords cold 결정 (volume + competition)

**한국어 P0 (월 검색량 추정 + 경쟁)**:
- "1인 퀀트" (~500/월, 경쟁 낮음) — owner brand 정착 가능
- "AI 자동매매 후기" (~2,000/월, 경쟁 높음) — 38일 honest failure 가 contrarian
- "한국 퀀트 봇 오픈소스" (~200/월, 경쟁 매우 낮음) — unique
- "퀀트 백테스트 후기" (~800/월, 경쟁 중간)

**영문 P0**:
- "1-person quant portfolio" (~50/월, 경쟁 거의 0) — unique brand
- "Korean retail quant" (~80/월, 경쟁 거의 0) — geographic differentiation
- "honest failure trading" (~100/월, 경쟁 낮음) — contrarian
- "multi-asset retail quant" (~150/월, 경쟁 중간)

**Naver 친화 keyword**:
- Naver 는 "퀀트 봇" (~3,500/월) Google 대비 2~3배 검색량
- "주식 자동매매 만들기" (~5,000/월) — 한국 retail 의 큰 풀
- 단, 검색 결과 페이지가 Naver 블로그 (Tistory + Naver Blog) 위주 → 본인 도메인 노출 약함
- 권고: Naver SEO 직접 추격 X, Google + 영문 글로벌 채널 우선

### 5.4 schema.org structured data

Article schema (각 docs 페이지):
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "38-Day Quant POC: Honest Failure Documentation",
  "author": {
    "@type": "Person",
    "name": "Yesol Heo",
    "url": "https://heoyesol.kr"
  },
  "datePublished": "2026-05-14",
  "publisher": {
    "@type": "Organization",
    "name": "OpenQuantKR"
  }
}
```

SoftwareSourceCode schema (GitHub repo link):
```json
{
  "@type": "SoftwareSourceCode",
  "name": "quant-poc-multi-asset",
  "codeRepository": "https://github.com/Yesol-Pilot/quant-poc-multi-asset",
  "programmingLanguage": "Python",
  "license": "https://opensource.org/licenses/MIT"
}
```

### 5.5 Open Graph + Twitter Cards

```html
<meta property="og:title" content="38-day quant POC honest failure" />
<meta property="og:description" content="1-person retail quant across KR/US/crypto..." />
<meta property="og:image" content="https://heoyesol.kr/quant/og-image.png" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:creator" content="@yesol_pilot" />
```

cold 권고: og:image 는 1,200×630 + 학술 figure + 한국+영문 dual title.

---

## 6. Performance 목표

### 6.1 Lighthouse 목표

| Metric | 목표 | 현실 (Next.js 15) | 최적화 priority |
|---|---|---|---|
| Performance | 95+ | 75~90 | P0 |
| SEO | 100 | 95~100 | P1 |
| Accessibility | 95+ | 85~95 | P1 |
| Best Practices | 100 | 95~100 | P2 |

### 6.2 First Contentful Paint < 1.0s

권고:
- Next.js Server Components (default in App Router)
- 이미지 `next/image` lazy load + AVIF 포맷
- Tremor chart 는 client-side only — `dynamic(() => import(...), { ssr: false })` 사용

### 6.3 Total Bundle < 200KB

cold 측정:
- Next.js 15 baseline = 80KB (App Router)
- React 18 + Tailwind = +20KB
- Tremor + Recharts = +120KB → **합산 220KB**
- 가능: dynamic import 로 chart 페이지만 load → main page < 100KB
- 대안: Tremor 대신 simpler chart 사용 (custom SVG) → bundle 절감 80KB

### 6.4 Edge Functions (rate limiting)

Vercel Edge Functions ($0 추가, Pro 포함):
- `/api/*` rate limit 100 req/IP/분 (Upstash Redis 또는 Vercel KV)
- public API 의 abuse 차단

```typescript
// middleware.ts
import { Ratelimit } from '@upstash/ratelimit'

const ratelimit = new Ratelimit({
  redis: ...,
  limiter: Ratelimit.slidingWindow(100, '60 s')
})

export async function middleware(req) {
  const ip = req.ip ?? 'anonymous'
  const { success } = await ratelimit.limit(ip)
  if (!success) return new Response('Rate limit', { status: 429 })
}
```

---

## 7. GEO (Generative Engine Optimization, AI search)

### 7.1 ChatGPT / Perplexity / Claude / Gemini 학습 데이터 inclusion 현실

cold 인지:
- **Common Crawl CCBot** = 가장 큰 학습 데이터 source (75% 사이트가 차단 — 차단 X 가 advantage)
- **GPTBot (OpenAI)** = ChatGPT 학습 + Bing 검색 backbone
- **ClaudeBot (Anthropic)** = Claude 학습 데이터
- **PerplexityBot** = Perplexity 실시간 검색 + 학습
- **Google-Extended** = Bard/Gemini 학습 데이터

robots.txt 권고:
```
User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-User
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: CCBot
Allow: /

User-agent: Bytespider
Disallow: /
```

cold 주의:
- `Bytespider` (ByteDance/TikTok) 는 일반적으로 차단 권고 (training 사용 불투명)
- `CCBot` allow 가 가장 중요 (Common Crawl = 모든 LLM 학습의 backbone)

### 7.2 llms.txt — cold honest

llms.txt 실효성 검증 (2026-05):
- Google 공식 발표 (2025-06): "no AI system currently uses llms.txt"
- Anthropic / OpenAI 도 공식 사용 확인 안 함
- 300,000 도메인 SERanking 연구 (2025-11): "doesn't improve AI citations measurably"

**그럼에도 권고**: `llms.txt` 작성. 이유:
- Anthropic / Cloudflare / Stripe / Vercel 가 공식 publish → 산업 표준 signaling
- 미래 (12~24개월) 사용 가능성 잔존
- Cost 0 (15분 작성)

`heoyesol.kr/llms.txt` 예시:
```markdown
# heoyesol.kr - Yesol Heo Portfolio

> 1-person AI-native PM portfolio. Korean retail quant, MARL research, causal safety.

## Quant POC
- [38-day Honest Failure](/quant/closure-note): Multi-asset retail quant POC closure
- [Research Reports](/quant/docs/research): 11-area research with 100+ citations
- [Live Dashboard](/quant): Real-time paper trading metrics

## Academic Papers
- [NeurIPS 2026 #20237 (under review)](/papers/marl-commitment-floors): MARL safety
- [TMLR 2026 #8752 (under review)](/papers/whylab-causal-safety): Causal safety

## Contact
- GitHub: [Yesol-Pilot](https://github.com/Yesol-Pilot)
- Email: dpthf1537@gmail.com
```

### 7.3 Citable structured content

cold 권고:
- 매 페이지 첫 200 단어 안에 "TL;DR" 또는 "Summary" 박스 — LLM 이 그대로 citation
- "Q: ... A: ..." 형식 FAQ section (Perplexity 친화)
- 수치는 마크다운 표로 (LLM parsing 친화)
- 출처 (URL + 인용일) 마크다운 link 로 — citation chain 형성

### 7.4 Common Crawl inclusion (owner cc-bot contact record 활용)

owner 가 cc-bot 와 contact 한 record (BIBLE.md 또는 CREDENTIAL_BIBLE.md 안 어디에 박제됨 — 정확한 위치는 owner 가 보유). 활용:
- cc-bot 운영 측 contact 가 있다면 crawl 우선순위 부여 요청 가능
- 표준 절차: `https://commoncrawl.org/contact-us/` 통해 사이트 추가 요청
- Common Crawl 누적 = 모든 LLM 학습 데이터 inclusion 의 단일 entry point

### 7.5 Wikipedia notability seed

12주 plan 안에서는 어려움. 그러나 NeurIPS + TMLR 1편씩 accept 시점에 (12~18개월 후) Wikipedia article notability 기준 충족 가능:
- 학술 paper 2편 cited (Notability threshold)
- News coverage 1~2건 (Show HN + Korean tech media)
- 본인 직접 작성 금지 (conflict of interest) → 외부 contributor 가 작성

---

## 8. Public API (rate-limited)

### 8.1 사용 시나리오

외부 개발자가 backtest 실행 가능:
```bash
curl https://heoyesol.kr/quant/api/backtest \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"strategy": "liquidation_cascade", "start": "2026-01-01", "end": "2026-03-31"}'
```

응답:
```json
{
  "trades": 47,
  "win_rate": 0.34,
  "pnl_pct": -0.082,
  "sharpe": -0.21,
  "honest_note": "Spec failure confirmed. See docs."
}
```

### 8.2 Rate limit + auth (Supabase RLS)

- Anonymous: 10 req/IP/일 (Vercel Edge middleware)
- API key (free signup): 100 req/일
- Pro tier ($5/월 future): 1,000 req/일
- 12주 plan 안에서는 anonymous 만 권고 (auth 도입은 사용자 5+명 도달 시)

### 8.3 OpenAPI spec

```yaml
openapi: 3.0.0
info:
  title: quant-poc-multi-asset API
  version: 0.1.0
paths:
  /backtest:
    post:
      summary: Run backtest
      ...
```

GitHub repo `/docs/api/openapi.yaml` 박제 → Swagger UI auto-serve (`/api/docs`).

---

## 9. Cold Honest 권고 (12주 plan timing)

### 9.1 12주 plan 단계별 Live page 활동

| 주 | 활동 | 시간 |
|---|---|---|
| W1 | Next.js project setup + Supabase Pro schema + Vercel deploy | 8h |
| W2 | Hero page + 38-day PoC overview + Tremor chart | 12h |
| W3 | i18n (한+영) + sitemap + Search Console + Bing | 6h |
| W4 | Realtime paper trading dashboard | 10h |
| W5 | Docs section (MDX 또는 Docusaurus 분리) | 8h |
| W6 | Open Graph + Twitter Cards + schema.org | 4h |
| W7 | llms.txt + robots.txt + GEO 최적화 | 3h |
| W8 | Public API (anonymous, rate-limited) | 6h |
| W9 | Performance 최적화 (Lighthouse 95+) | 6h |
| W10 | Analytics (GA4 + PostHog) 통합 | 4h |
| W11 | Korean SEO 콘텐츠 (5 blog posts) | 12h |
| W12 | English SEO 콘텐츠 (3 blog posts) + share 발사 | 10h |

총합 ~89h. owner 본업 + 11 SBU + Sora + quant 운영 일정과 정합 가능 범위.

### 9.2 자본 비용 (외부 의존성)

| 항목 | 월 비용 | 12주 |
|---|---|---|
| Domain `heoyesol.kr` (기존) | $0 | $0 |
| Vercel Pro (이미 owner 사용) | $0 추가 | $0 |
| Supabase Pro | $25 | $75 |
| Upstash Redis (rate limit) | $0 (free tier) | $0 |
| Cloudflare (분석, optional) | $0 | $0 |
| **합계** | **$25/월** | **$75** |

D8 자본 권고 ($0~$278) 안 fit. Tier A 권고 (Theta Data Value + Polygon Starter) 가 quant 데이터 비용 — Live page 자체 비용은 $75/12주 로 minimal.

### 9.3 Visibility 예측 (12주 종료 시)

| Metric | 보수 | 중도 | 낙관 |
|---|---|---|---|
| Monthly visitors | 500 | 2,000 | 8,000 |
| Avg session duration | 1:30 | 2:30 | 4:00 |
| Search Console impressions | 5,000/월 | 25,000/월 | 80,000/월 |
| Clicks | 100/월 | 500/월 | 2,000/월 |
| LLM citation (Perplexity/Claude/ChatGPT) | 0~2 | 3~10 | 15~30 |

LLM citation 측정 어려움 — Perplexity 직접 검색 ("1인 퀀트", "Korean retail quant") + Claude 직접 질문 으로 manual verification.

### 9.4 외부 정책 변경 risk (cold honest)

- **Vercel Pro 가격 변경** (낮음 — 2년 stable): $20/월 → $30/월 가능성, 대안 Cloudflare Pages ($0).
- **Supabase 8GB 변경** (낮음): 가격 인상 가능, 대안 self-hosted PostgreSQL (Hetzner $5/월).
- **Google Search Console API 변경** (중간): rate limit 변경 가능, 모니터링 필요.
- **Anthropic ClaudeBot / OpenAI GPTBot crawler rate 변경** (높음): allow/deny 외 owner control 없음. cold 수용.
- **Naver SEO 알고리즘 변경** (높음, 잦음): 한국 retail 트래픽 의존 시 risk. **권고: Naver 의존 X, Google + 글로벌 우선**.
- **`heoyesol.kr` DNS 변경 risk** (낮음): owner 가 직접 보유. 단, 4년 후 renewal 잊으면 squatting 위험 — multi-year renewal 권고.

### 9.5 38일 PoC 외부 정책 변경 실패 패턴 차단

- **단일 외부 의존성 회피**: Vercel + Supabase 둘 다 정착이지만, monthly export (`pg_dump` GitHub Actions) + 정적 Next.js export 가능성 유지 → 단일 platform 종속 회피.
- **Domain ownership 영구**: `heoyesol.kr` registrar 가 2026-05 시점 정착. 10년 갱신 권고 (대량 cost X, $40~$100).
- **Source control = Git (Yesol-Pilot/* GitHub)**: live page 의 모든 콘텐츠 = git history → Vercel 종료 시 다른 host 즉시 deploy 가능.
- **Cold honest 콘텐츠**: 38일 PoC failure 그대로 시각화 — Quantpedia / Hudson&Thames 등 future contraction 시에도 owner의 unique value (transparency) 가 destination 으로 작동.

---

## 10. References

- [Next.js 15 vs Astro 5 (WPPoland)](https://wppoland.com/en/astro-5-vs-nextjs-15-comparison-2026/) — 2026-05-14 인용
- [Astro vs Next.js (Cipher Projects)](https://cipherprojects.com/blog/posts/nextjs-vs-astro-which-one-fits-your-project/) — 2026-05-14 인용
- [Docusaurus introduction](https://docusaurus.io/docs/) — 2026-05-14 인용
- [Nextra alternatives (AlternativeTo)](https://alternativeto.net/software/nextra/) — 2026-05-14 인용
- [MkDocs Material maintenance mode (squidfunk)](https://squidfunk.github.io/mkdocs-material/alternatives/) — 2026-05-14 인용
- [Recharts vs Chart.js vs Nivo 2026 (PkgPulse)](https://www.pkgpulse.com/guides/recharts-vs-chartjs-vs-nivo-vs-visx-react-charting-2026) — 2026-05-14 인용
- [Tremor — Tailwind chart components](https://www.tremor.so/) — 2026-05-14 인용
- [Supabase Pro pricing (Metacto)](https://www.metacto.com/blogs/the-true-cost-of-supabase-a-comprehensive-guide-to-pricing-integration-and-maintenance) — 2026-05-14 인용
- [Supabase egress management](https://supabase.com/docs/guides/platform/manage-your-usage/egress) — 2026-05-14 인용
- [Korean SEO Naver vs Google 2026 (InterAd)](https://www.interad.com/en/korean-seo) — 2026-05-14 인용
- [Naver vs Google 2026 (LinkAssistant)](https://www.link-assistant.com/news/naver-vs-google-in-korea.html) — 2026-05-14 인용
- [GEO 2026 Guide (LLMrefs)](https://llmrefs.com/generative-engine-optimization) — 2026-05-14 인용
- [llms.txt May 2026 Honest Guide (Codersera)](https://codersera.com/blog/llms-txt-complete-guide-2026/) — 2026-05-14 인용
- [ClaudeBot crawler docs (Anthropic Help Center)](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler) — 2026-05-14 인용
- [AI User-Agent Landscape 2026 (NoHacks)](https://nohacks.co/blog/ai-user-agents-landscape-2026) — 2026-05-14 인용
- [Vercel Pro Pricing 2026 (Schematic HQ)](https://schematichq.com/blog/vercel-pricing) — 2026-05-14 인용
- [Cloudflare Pages Pricing 2026 (DevToolReviews)](https://www.devtoolreviews.com/reviews/cloudflare-pages-pricing-bandwidth-limits-2026) — 2026-05-14 인용
- [Common Crawl CCBot Guide (AICrawlerCheck)](https://aicrawlercheck.com/blog/what-is-ccbot-common-crawl) — 2026-05-14 인용

— END —
