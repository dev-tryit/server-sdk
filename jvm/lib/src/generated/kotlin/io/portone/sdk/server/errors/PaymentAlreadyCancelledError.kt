package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CancelPaymentError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제가 이미 취소된 경우 */
@Serializable
@SerialName("PAYMENT_ALREADY_CANCELLED")
@ConsistentCopyVisibility
public data class PaymentAlreadyCancelledError internal constructor(
  override val message: String? = null,
): CancelPaymentError
