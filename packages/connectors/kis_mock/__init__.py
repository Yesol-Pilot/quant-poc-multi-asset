"""KIS (Korea Investment & Securities) OpenAPI connector — mock/paper only.

Usage (once owner injects KIS_APP_KEY + KIS_APP_SECRET):

    from connectors.kis_mock import KisMockClient, load_from_env

    async with KisMockClient(load_from_env()) as kis:
        bar = await kis.quote_to_bar("005930")  # Samsung Electronics

Until then, network methods raise OfflineMode and the rest of the stack can
still import + unit-test against fixtures.
"""

from connectors.kis_mock.client import KisApiError, KisMockClient, OfflineMode
from connectors.kis_mock.config import (
    MOCK_BASE_URL,
    KisConfig,
    LiveEndpointError,
    load_from_env,
)
from connectors.kis_mock.models import (
    OrderRequest,
    OrderResponse,
    QuoteResponse,
    TokenResponse,
)

__all__ = [
    "KisMockClient",
    "KisApiError",
    "OfflineMode",
    "KisConfig",
    "LiveEndpointError",
    "MOCK_BASE_URL",
    "load_from_env",
    "TokenResponse",
    "QuoteResponse",
    "OrderRequest",
    "OrderResponse",
]
