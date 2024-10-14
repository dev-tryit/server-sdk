from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformNotEnabledError:
    """플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
    """
    type: Literal["PLATFORM_NOT_ENABLED"] = field(repr=False)
    message: Optional[str]


def _serialize_platform_not_enabled_error(obj: PlatformNotEnabledError) -> Any:
    entity = {}
    entity["type"] = obj.type
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_not_enabled_error(obj: Any) -> PlatformNotEnabledError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_NOT_ENABLED":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_NOT_ENABLED'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformNotEnabledError(type, message)