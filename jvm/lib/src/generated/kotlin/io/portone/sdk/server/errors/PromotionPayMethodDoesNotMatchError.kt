package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PayInstantlyError
import io.portone.sdk.server.errors.PayWithBillingKeyError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제수단이 프로모션에 지정된 것과 일치하지 않는 경우 */
@Serializable
@SerialName("PROMOTION_PAY_METHOD_DOES_NOT_MATCH")
@ConsistentCopyVisibility
public data class PromotionPayMethodDoesNotMatchError internal constructor(
  override val message: String? = null,
): PayInstantlyError,
  PayWithBillingKeyError
