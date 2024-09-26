import type { IdentityVerificationFailure } from "#generated/identityVerification/IdentityVerificationFailure"
import type { IdentityVerificationRequestedCustomer } from "#generated/identityVerification/IdentityVerificationRequestedCustomer"
import type { SelectedChannel } from "#generated/common/SelectedChannel"

/** 실패한 본인인증 내역 */
export type FailedIdentityVerification = {
	/** 본인인증 상태 */
	status: "FAILED"
	/** 본인인증 내역 아이디 */
	id: string
	/** 사용된 본인인증 채널 */
	channel?: SelectedChannel
	/** 요청 시 고객 정보 */
	requestedCustomer: IdentityVerificationRequestedCustomer
	/** 사용자 지정 데이터 */
	customData?: string
	/**
	 * 본인인증 요청 시점
	 * (RFC 3339 date-time)
	 */
	requestedAt: string
	/**
	 * 업데이트 시점
	 * (RFC 3339 date-time)
	 */
	updatedAt: string
	/**
	 * 상태 업데이트 시점
	 * (RFC 3339 date-time)
	 */
	statusChangedAt: string
	/** 본인인증 실패 정보 */
	failure: IdentityVerificationFailure
}