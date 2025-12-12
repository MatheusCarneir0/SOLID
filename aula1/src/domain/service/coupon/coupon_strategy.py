from abc import ABC, abstractmethod


class CouponStrategy(ABC):
    """Estratégia abstrata para aplicação de cupom de desconto."""
    @abstractmethod
    def apply_discount(self, value: float):
        pass 


class BlackFridayCoupon(CouponStrategy):
    """Implementação concreta da estratégia de cupom de Black Friday."""
    def apply_discount(self, value: float):
        if value < 300:
            raise ValueError("Valor mínimo para aplicar cupom Black Friday é 300.")
        return value * 0.2
    

class NatalCoupon(CouponStrategy):
    """Implementação concreta da estratégia de cupom de Natal."""
    def apply_discount(self, value: float):
        if value < 800:
            raise ValueError("Valor mínimo para aplicar cupom de Natal é 800.")
        return value * 0.3
    
    "teste"