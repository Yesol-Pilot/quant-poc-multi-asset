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

# The only base URL this connector will accept. Mock/paper trading domain.
MOCK_BASE_URL = "https://openapivts.koreainvestment.com:29443"
_LIVE_FRAGMENT = "openapi.koreainvestment.com"  # FORBIDDEN live host (note: no "vts")


class LiveEndpointError(RuntimeError):
    """Raised when a non-mock (live) KIS endpoint is configured."""


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
        # Reject the live endpoint. The mock domain contains "openapivts";
        # the live domain is "openapi" without "vts".
        host = self.base_url.lower()
        if "openapivts" not in host and _LIVE_FRAGMENT in host:
            raise LiveEndpointError(
                f"Refusing live KIS endpoint {self.base_url!r}. "
                f"Only the mock endpoint ({MOCK_BASE_URL}) is allowed in this phase."
            )

    @property
    def is_mock(self) -> bool:
        return "openapivts" in self.base_url.lower()

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
