package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.GetB2bAccountHolderError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 정지 계좌인 경우 */
@Serializable
@SerialName("B2B_SUSPENDED_ACCOUNT")
public data class B2bSuspendedAccountError(
  val message: String? = null,
): GetB2bAccountHolderError