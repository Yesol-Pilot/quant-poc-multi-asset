"""@qpm/core — Shared utilities for quant-poc-multi-asset.

Cross-language layer (Python + TypeScript via shared schemas).
Reference: docs/design/01-architecture-spec.md
"""

from core.types import (
    AlphaSignal,
    AssetClass,
    KillSwitchLayer,
    KillSwitchTrigger,
    MarketBar,
    OrderIntent,
    OrderType,
    Side,
)

__version__ = "0.1.0"
__all__ = [
    "AlphaSignal",
    "AssetClass",
    "KillSwitchLayer",
    "KillSwitchTrigger",
    "MarketBar",
    "OrderIntent",
    "OrderType",
    "Side",
]
