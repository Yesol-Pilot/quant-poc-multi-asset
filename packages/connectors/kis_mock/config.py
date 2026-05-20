"""KIS connector configuration — paper/mock only.

Hard invariant: the base URL MUST be the mock endpoint
(`openapivts.koreainvestment.com`). The live production endpoint is FORBIDDEN
and rejected at construction time so no code path — not even a misconfigured
env var — can point this client at production. This GUARD mirrors the CI
`paper-only-guard` but enforces it at runtime.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from urllib.parse import urlparse

# The only base URL this connector will accept. Mock/paper trading domain.
MOCK_BASE_URL = "https://openapivts.koreainvestment.com:29443"
# Allowlist — the EXACT hostname the client may talk to. Anything else is
# rejected. (Allowlist, not blocklist: a blocklist of "the live host" lets
# every other host through, including a real-money endpoint under a different
# name or a look-alike like "openapivts.evil.com".)
_ALLOWED_HOST = "openapivts.koreainvestment.com"


class LiveEndpointError(RuntimeError):
    """Raised when a non-mock (non-allowlisted) KIS endpoint is configured."""


@dataclass(frozen=True)
class KisConfig:
    app_key: str
    app_secret: str
    base_url: str = MOCK_BASE_URL
    account_no: str = ""        # 8-2 format, e.g. "12345678-01"
    account_prod: str = "01"    # product code; 01 = 위탁(cash)
    timeout_s: float = 10.0
    max_retries: int = 3

    def __post_init__(self) -> None:
        # ALLOWLIST: the parsed hostname must be EXACTLY the mock host, over
        # https. Fail closed on anything else (empty, malformed, look-alike,
        # live host, different scheme). This is the runtime mirror of the CI
        # paper-only-guard and the reason no code path can reach production.
        parsed = urlparse(self.base_url)
        host = (parsed.hostname or "").lower()
        scheme = (parsed.scheme or "").lower()
        if host != _ALLOWED_HOST or scheme != "https":
            raise LiveEndpointError(
                f"Refusing non-mock KIS endpoint {self.base_url!r} "
                f"(host={host!r}, scheme={scheme!r}). "
                f"Only the mock endpoint ({MOCK_BASE_URL}) is allowed in this phase."
            )

    @property
    def is_mock(self) -> bool:
        # By construction (allowlist), a constructed KisConfig is always mock.
        return urlparse(self.base_url).hostname == _ALLOWED_HOST

    @property
    def has_credentials(self) -> bool:
        return bool(self.app_key) and bool(self.app_secret)


def load_from_env(env: dict[str, str] | None = None) -> KisConfig:
    """Build a KisConfig from environment variables.

    Reads KIS_APP_KEY / KIS_APP_SECRET / KIS_BASE_URL / KIS_ACCOUNT_NO /
    KIS_ACCOUNT_PROD. Until the owner completes the one-time KIS Developers
    signup, app_key/app_secret will be empty and `has_credentials` is False —
    the client then runs in offline scaffold mode (no network).
    """
    e = env if env is not None else dict(os.environ)
    return KisConfig(
        app_key=e.get("KIS_APP_KEY", ""),
        app_secret=e.get("KIS_APP_SECRET", ""),
        base_url=e.get("KIS_BASE_URL", MOCK_BASE_URL),
        account_no=e.get("KIS_ACCOUNT_NO", ""),
        account_prod=e.get("KIS_ACCOUNT_PROD", "01"),
    )


__all__ = ["KisConfig", "LiveEndpointError", "MOCK_BASE_URL", "load_from_env"]
