from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class SumOfPartsExceedsTotalAmountError:
    """면세 금액 등 하위 항목들의 합이 전체 결제 금액을 초과한 경우
    """
    type: Literal["SUM_OF_PARTS_EXCEEDS_TOTAL_AMOUNT"] = field(repr=False)
    message: Optional[str]


def _serialize_sum_of_parts_exceeds_total_amount_error(obj: SumOfPartsExceedsTotalAmountError) -> Any:
    entity = {}
    entity["type"] = "SUM_OF_PARTS_EXCEEDS_TOTAL_AMOUNT"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_sum_of_parts_exceeds_total_amount_error(obj: Any) -> SumOfPartsExceedsTotalAmountError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "SUM_OF_PARTS_EXCEEDS_TOTAL_AMOUNT":
        raise ValueError(f"{repr(type)} is not 'SUM_OF_PARTS_EXCEEDS_TOTAL_AMOUNT'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return SumOfPartsExceedsTotalAmountError(type, message)
