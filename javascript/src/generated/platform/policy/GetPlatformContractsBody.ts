import type { PageInput } from "#generated/common/PageInput"
import type { PlatformContractFilterInput } from "#generated/platform/policy/PlatformContractFilterInput"

/** 계약 다건 조회를 위한 입력 정보 */
export type GetPlatformContractsBody = {
	/** 요청할 페이지 정보 */
	page?: PageInput
	/** 조회할 계약 조건 필터 */
	filter?: PlatformContractFilterInput
}