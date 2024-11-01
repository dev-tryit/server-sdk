from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.platform.platform_archived_discount_share_policy_error import PlatformArchivedDiscountSharePolicyError, _deserialize_platform_archived_discount_share_policy_error, _serialize_platform_archived_discount_share_policy_error
from portone_server_sdk._generated.platform.platform_discount_share_policy_not_found_error import PlatformDiscountSharePolicyNotFoundError, _deserialize_platform_discount_share_policy_not_found_error, _serialize_platform_discount_share_policy_not_found_error
from portone_server_sdk._generated.platform.platform_discount_share_policy_schedule_already_exists_error import PlatformDiscountSharePolicyScheduleAlreadyExistsError, _deserialize_platform_discount_share_policy_schedule_already_exists_error, _serialize_platform_discount_share_policy_schedule_already_exists_error
from portone_server_sdk._generated.platform.platform_not_enabled_error import PlatformNotEnabledError, _deserialize_platform_not_enabled_error, _serialize_platform_not_enabled_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

ScheduleDiscountSharePolicyError = Union[ForbiddenError, InvalidRequestError, PlatformArchivedDiscountSharePolicyError, PlatformDiscountSharePolicyNotFoundError, PlatformDiscountSharePolicyScheduleAlreadyExistsError, PlatformNotEnabledError, UnauthorizedError]


def _serialize_schedule_discount_share_policy_error(obj: ScheduleDiscountSharePolicyError) -> Any:
    if obj.type == "FORBIDDEN":
        return _serialize_forbidden_error(obj)
    if obj.type == "INVALID_REQUEST":
        return _serialize_invalid_request_error(obj)
    if obj.type == "PLATFORM_ARCHIVED_DISCOUNT_SHARE_POLICY":
        return _serialize_platform_archived_discount_share_policy_error(obj)
    if obj.type == "PLATFORM_DISCOUNT_SHARE_POLICY_NOT_FOUND":
        return _serialize_platform_discount_share_policy_not_found_error(obj)
    if obj.type == "PLATFORM_DISCOUNT_SHARE_POLICY_SCHEDULE_ALREADY_EXISTS":
        return _serialize_platform_discount_share_policy_schedule_already_exists_error(obj)
    if obj.type == "PLATFORM_NOT_ENABLED":
        return _serialize_platform_not_enabled_error(obj)
    if obj.type == "UNAUTHORIZED":
        return _serialize_unauthorized_error(obj)


def _deserialize_schedule_discount_share_policy_error(obj: Any) -> ScheduleDiscountSharePolicyError:
    try:
        return _deserialize_forbidden_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_invalid_request_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_archived_discount_share_policy_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_discount_share_policy_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_discount_share_policy_schedule_already_exists_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_not_enabled_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_unauthorized_error(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not ScheduleDiscountSharePolicyError")
