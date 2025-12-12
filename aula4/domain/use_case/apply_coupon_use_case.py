from aula4.domain.entities.carrinho import Carrinho
from aula4.domain.service.coupon.apply_coupon import ApplyCouponStrategy
from aula4.domain.factories.coupon_strategy_factory import (
    TypeCoupon, StrategyCouponFactory
)


class ApplyCouponUseCase:
    def execute(self, cart: Carrinho, type_coupon: TypeCoupon) -> dict:
        subtotal = cart.get_subtotal()
        strategy = StrategyCouponFactory.create(type_coupon)
        discount = ApplyCouponStrategy(strategy).apply_discount(subtotal)
        new_subtotal = subtotal - discount
        return {
            "discount_value": discount,
            "new_subtotal": new_subtotal,
            "cart_id": cart.get_carrinho_id()
        }
