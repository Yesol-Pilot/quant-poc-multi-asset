"""Smoke tests — Week 1 baseline.

Verify package layout, imports, and CI guards function as expected.
"""

import os
import re
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).parent.parent


def test_repo_root_exists() -> None:
    """Sanity check that the test runner can find the repo root."""
    assert REPO_ROOT.exists()
    assert (REPO_ROOT / "README.md").exists()
    assert (REPO_ROOT / "LICENSE").exists()


def test_disclaimer_required_files() -> None:
    """All standard OSS files are present."""
    required = [
        "README.md",
        "LICENSE",
        "DISCLAIMER.md",
        "CONTRIBUTING.md",
        "SECURITY.md",
        "CODE_OF_CONDUCT.md",
        "CHANGELOG.md",
        "ROADMAP.md",
        "ARCHITECTURE.md",
        ".gitignore",
    ]
    for f in required:
        assert (REPO_ROOT / f).exists(), f"Missing required file: {f}"


def test_pyproject_well_formed() -> None:
    """pyproject.toml exists and contains key sections."""
    py = REPO_ROOT / "pyproject.toml"
    assert py.exists()
    text = py.read_text(encoding="utf-8")
    assert "quant-poc-multi-asset" in text
    assert "ib_async" in text  # critical: ib_insync deprecated, use ib_async
    assert 'license = { text = "MIT" }' in text


def test_core_package_importable() -> None:
    """packages/core can be imported (basic Python wiring)."""
    import sys

    sys.path.insert(0, str(REPO_ROOT / "packages"))
    from core.version import __version__, get_version

    assert __version__ == "0.1.0"
    assert get_version() == "0.1.0"


def test_no_live_kis_url_in_source() -> None:
    """CRITICAL: production KIS URL must never appear in source.

    Only `openapivts.koreainvestment.com` (mock) is allowed in Phase 1.
    `openapi.koreainvestment.com` (live) is a CI-blocking violation.
    """
    forbidden = re.compile(r"openapi\.koreainvestment\.com(?!:?29443)")  # live URL pattern
    for ext in ("*.py", "*.ts", "*.tsx", "*.js", "*.json"):
        for f in REPO_ROOT.rglob(ext):
            # Skip _archive, docs (allowed mentions for educational purposes),
            # node_modules, and this test file
            parts = set(f.parts)
            if "_archive" in parts or "docs" in parts or "node_modules" in parts:
                continue
            if f.name == "test_smoke.py":
                continue
            text = f.read_text(encoding="utf-8", errors="ignore")
            for line in text.splitlines():
                if "openapivts" in line:  # mock - allowed
                    continue
                assert not forbidden.search(line), (
                    f"❌ LIVE KIS URL detected in {f}: {line.strip()}"
                )


def test_no_live_ibkr_port_in_source() -> None:
    """CRITICAL: IBKR live port 7496 must never appear in source.

    Only port 7497 (paper) is allowed in Phase 1.
    """
    live_port_pattern = re.compile(r"\b7496\b")
    paper_port_pattern = re.compile(r"\b7497\b")
    for ext in ("*.py", "*.ts", "*.tsx", "*.js"):
        for f in REPO_ROOT.rglob(ext):
            parts = set(f.parts)
            if "_archive" in parts or "docs" in parts or "node_modules" in parts:
                continue
            if f.name == "test_smoke.py":
                continue
            text = f.read_text(encoding="utf-8", errors="ignore")
            for line_num, line in enumerate(text.splitlines(), start=1):
                if live_port_pattern.search(line):
                    # Allow inside comments explicitly forbidding live port
                    if "NEVER" in line.upper() or "FORBIDDEN" in line.upper() or "BLOCKED" in line.upper():
                        continue
                    pytest.fail(
                        f"❌ LIVE IBKR port 7496 detected in {f}:{line_num}: {line.strip()}"
                    )


def test_env_example_has_paper_mode_default() -> None:
    """`.env.example` must default TRADING_MODE to paper."""
    env_example = REPO_ROOT / ".env.example"
    assert env_example.exists()
    text = env_example.read_text(encoding="utf-8")
    assert "TRADING_MODE=paper" in text
    # IBKR port must be 7497 (paper) in defaults
    assert "IBKR_PORT=7497" in text
    # KIS base URL must be the mock (openapivts) in defaults
    assert "openapivts.koreainvestment.com" in text
