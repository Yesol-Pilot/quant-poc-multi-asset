# Contributing

Welcome 👋 — and thank you for considering a contribution to **quant-poc-multi-asset**.

> **TL;DR**: Open issues for discussion → forks/PRs welcome → all PRs require passing tests + 1+ review. This is a **personal portfolio + academic publication** project; we move at the maintainer's review cadence (~weekly).

---

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to uphold this code.

## What Kinds of Contributions Are Welcome?

✅ Welcome:
- 🐛 **Bug fixes** (especially Kill Switch, backtest math, data adapters)
- 📚 **Documentation improvements** (Korean ↔ English parity, tutorials, examples)
- 🧪 **Test coverage** (we target 90%+)
- 🔬 **Academic citation improvements** (more rigorous references, corrections)
- 🌐 **Translations** (currently Korean + English, more welcome)
- 🚀 **Performance optimizations**
- 🔌 **New broker adapters** (Korean retail or international, paper-mode only by default)

🟡 Discuss first (open an issue):
- 🎯 **New alpha implementations** (must include academic references + backtest results)
- 🏗️ **Architecture changes**
- 📦 **New top-level dependencies**

❌ Not accepted:
- 🚫 Live-trading code paths (this is **paper-trading + educational only**)
- 🚫 Closed-source or paid API integrations without free alternatives
- 🚫 Investment advice / recommendations / signals in documentation
- 🚫 Cherry-picked backtest results without DSR/PBO/regime breakdown

---

## How to Contribute

### 1. Open an Issue First

For non-trivial changes, **open an issue** to discuss before writing code. This saves both your time and ours.

Use the templates:
- 🐛 Bug report
- ✨ Feature request
- 📖 Documentation
- 🔬 Academic correction

### 2. Fork and Branch

```bash
git clone https://github.com/Yesol-Pilot/quant-poc-multi-asset
cd quant-poc-multi-asset
git checkout -b feature/your-feature-name
```

Branch naming:
- `feature/short-description` — new functionality
- `fix/short-description` — bug fix
- `docs/short-description` — documentation
- `test/short-description` — test coverage
- `refactor/short-description` — refactoring

### 3. Develop Locally

```bash
# Install
pnpm install
python -m venv .venv && source .venv/bin/activate
pip install -e .[dev]

# Run tests (must pass before commit)
pnpm test          # Vitest (Node.js)
pytest             # Python
pnpm lint          # ESLint + Prettier
ruff check .       # Python linter
mypy packages/     # Python type check

# Run a quick backtest
pnpm backtest:a12  # KOSPI Mean Reversion sample
```

### 4. Commit Conventions

We use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add A22 Crypto volatility carry alpha
fix(kill-switch): correct L7 environment guard check
docs: clarify KIS API rate limit handling
test: add 14 edge cases for A11 sector rotation
refactor(backtest): extract DSR calculation
chore(deps): bump Next.js to 15.3
```

Commit messages can be Korean or English — both are fine.

### 5. Pull Request

- Clear title (matches commit convention)
- Description: what / why / how tested
- Link to issue (if applicable)
- Pass all CI checks (Vitest + pytest + lint + type)
- Update CHANGELOG.md (if user-facing change)
- Update relevant docs

### 6. Review Process

- 1+ maintainer review required
- Maintainer responds within ~1 week (this is a personal project; please be patient)
- We use "squash and merge" for clean history
- Comments may include cold-honest feedback — that's the project's style; please don't take it personally

---

## Testing Standards

- **Unit tests**: New code must include unit tests. Coverage target: 90%+.
- **Integration tests**: New broker/data adapters require integration tests (mocked external services).
- **Backtest verification**: New alpha must include DSR, PBO, regime breakdown, OOS validation.
- **No flaky tests**: Use Vitest `retry: 0`, fix root cause not retry count.

## Academic Standards

- Every alpha must cite **original peer-reviewed paper** in its module docstring.
- Citations follow APA-ish format: `Author (Year) "Title", Journal, DOI/URL`.
- Korean market alpha must check **Korean-specific academic evidence** (Chui-Titman-Wei 2000 for momentum, Kang 2018 for FF5, etc.).
- See [docs/research/06-academic-references.md](docs/research/06-academic-references.md) for the 62-reference base set.

## Documentation Standards

- All public functions/classes have docstrings (TSDoc / Python docstring)
- Korean documentation + English documentation in parallel (we maintain both)
- Code blocks must be runnable (no pseudo-code in docs)
- Diagrams use Mermaid where possible

## Security

See [SECURITY.md](SECURITY.md) for vulnerability reporting.

Critical security rules:
- 🚫 Never commit `.env`, `.env.local`, secrets, API keys
- 🚫 Never disable Kill Switch in tests (use mocks)
- 🚫 Never bypass `enforce_paper_only()` in production code paths
- ✅ All credentials go in Supabase Vault or Vercel env (not in code, not in repo)

## Disclaimer

Contributors agree their contributions are licensed under the same MIT License as the project, and that nothing in their contribution constitutes investment advice or solicitation. See [DISCLAIMER.md](DISCLAIMER.md).

---

**Questions?** Open a [Discussion](https://github.com/Yesol-Pilot/quant-poc-multi-asset/discussions) or email [dpthf1537@gmail.com](mailto:dpthf1537@gmail.com).

Maintainer: 허예솔 (Yesol Huh)
