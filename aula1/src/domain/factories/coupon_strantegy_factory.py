import Enum, auto
from src.domain.service.coupon_strategy import CouponStrategy, BlackFridayCoupon, NatalCoupon

class TypeCoupon(Enum):
    """Tipos de cupom disponíveis."""
    BLACK_FRIDAY = auto()
    NEW_YEAR = auto()


class StrategyCouponFactory:
    """Fábrica de estratégias de cupons."""
    _strategy_map = {
        TypeCoupon.BLACK_FRIDAY: (BlackFridayCoupon()),
        TypeCoupon.NEW_YEAR: (NatalCoupon())
    }

    @classmethod
    def create(cls, type_coupon: TypeCoupon) -> CouponStrategy:
        try:
            return cls._strategy_map[type_coupon]
        except KeyError:
            raise ValueError(f"Tipo de cupom desconhecido: {type_coupon}")
        


        