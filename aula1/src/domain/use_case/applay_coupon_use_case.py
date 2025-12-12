from src.domain.entities.carrinho import Carrinho
from src.domain.service.coupon.coupon_strategy_factory import TypeCoupon, StrategyCouponFactory
from src.domain.service.coupon.apply_coupon import ApplyCouponStrategy


class ApplayCouponUseCase:
    
    def execute(self, carrinho: Carrinho, type_coupon: TypeCoupon) -> dict:
        """Aplica um cupom de desconto ao carrinho e retorna o valor descontado e o novo subtotal."""
        subtotal = carrinho.get_subtotal()
        strategy = StrategyCouponFactory.create(type_coupon)
        discount = ApplyCouponStrategy(strategy).apply_discount(subtotal)
        new_subtotal = subtotal - discount
        return {
            "discounted_value": discount,
            "new_subtotal": new_subtotal,
            "cart_id": carrinho.get_id()
        }