from src.domain.services.coupon.coupon_strategy import CouponStrategy


class CouponStrategy:
    def __init__(self, strategy: CouponStrategy):
        """Inicializa a estratégia de aplicação de cupom."""
        self._strategy = strategy

    def update_strategy(self, new_strategy: CouponStrategy):
        self._strategy = new_strategy

    def apply_discount(self, value: float):
        return self._strategy.apply_discount(value)