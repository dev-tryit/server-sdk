import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PlatformArchivedDiscountSharePolicyError } from "#generated/platform/PlatformArchivedDiscountSharePolicyError"
import type { PlatformDiscountSharePolicyNotFoundError } from "#generated/platform/PlatformDiscountSharePolicyNotFoundError"
import type { PlatformDiscountSharePolicyScheduleAlreadyExistsError } from "#generated/platform/PlatformDiscountSharePolicyScheduleAlreadyExistsError"
import type { PlatformNotEnabledError } from "#generated/platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type ScheduleDiscountSharePolicyError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformArchivedDiscountSharePolicyError
	| PlatformDiscountSharePolicyNotFoundError
	| PlatformDiscountSharePolicyScheduleAlreadyExistsError
	| PlatformNotEnabledError
	| UnauthorizedError
