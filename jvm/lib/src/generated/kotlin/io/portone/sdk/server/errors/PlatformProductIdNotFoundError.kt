package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CreatePlatformOrderCancelTransferError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_PRODUCT_ID_NOT_FOUND")
@ConsistentCopyVisibility
public data class PlatformProductIdNotFoundError internal constructor(
  val id: String,
  override val message: String? = null,
): CreatePlatformOrderCancelTransferError
