from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformSettlementCycleMethodDaily:
    """매일 정산
    """
    type: Literal["DAILY"] = field(repr=False)


def _serialize_platform_settlement_cycle_method_daily(obj: PlatformSettlementCycleMethodDaily) -> Any:
    entity = {}
    entity["type"] = "DAILY"
    return entity


def _deserialize_platform_settlement_cycle_method_daily(obj: Any) -> PlatformSettlementCycleMethodDaily:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "DAILY":
        raise ValueError(f"{repr(type)} is not 'DAILY'")
    return PlatformSettlementCycleMethodDaily(type)
