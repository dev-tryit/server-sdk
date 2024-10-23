package io.portone.sdk.server.b2b.taxinvoice

import kotlinx.serialization.Serializable

/** 세금계산서 식별자 유형 */
@Serializable
public enum class B2bTaxInvoiceKeyType {
  /** 공급자용 문서 번호 */
  SUPPLIER,
  /** 공급받는자용 문서 번호 */
  RECIPIENT,
  /** 세금계산서 아이디 */
  TAX_INVOICE_ID,
}
