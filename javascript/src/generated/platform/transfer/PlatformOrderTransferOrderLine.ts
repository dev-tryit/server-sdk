import type { PlatformOrderSettlementAmount } from "#generated/platform/PlatformOrderSettlementAmount"
import type { PlatformOrderTransferAdditionalFee } from "#generated/platform/transfer/PlatformOrderTransferAdditionalFee"
import type { PlatformOrderTransferDiscount } from "#generated/platform/transfer/PlatformOrderTransferDiscount"
import type { PlatformOrderTransferProduct } from "#generated/platform/transfer/PlatformOrderTransferProduct"

/** 주문 항목 */
export type PlatformOrderTransferOrderLine = {
	/** 상품 */
	product: PlatformOrderTransferProduct
	/**
	 * 상품 수량
	 * (int32)
	 */
	quantity: number
	/** 상품 할인 정보 */
	discounts: PlatformOrderTransferDiscount[]
	/** 상품 추가 수수료 정보 */
	additionalFees: PlatformOrderTransferAdditionalFee[]
	/** 상품 정산 금액 정보 */
	amount: PlatformOrderSettlementAmount
}