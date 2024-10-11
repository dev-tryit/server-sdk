package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.ChannelNotFoundError
import java.lang.Exception


/** 요청된 채널이 존재하지 않는 경우 */
public class ChannelNotFoundException(
  cause: ChannelNotFoundError
) : Exception(cause.message) {
}
