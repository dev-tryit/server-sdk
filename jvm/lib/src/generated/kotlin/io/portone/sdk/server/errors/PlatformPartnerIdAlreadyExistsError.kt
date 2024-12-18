package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CreatePlatformPartnerError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_PARTNER_ID_ALREADY_EXISTS")
@ConsistentCopyVisibility
public data class PlatformPartnerIdAlreadyExistsError internal constructor(
  override val message: String? = null,
): CreatePlatformPartnerError
