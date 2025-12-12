import uuid
from enum import Enum, auto


from src.domain.entities.produto import Produto
from typing import List


class CarrinhoStatus(Enum):
    ATIVO = auto()
    FINALIZADO = auto()
    EXPIRADO = auto()


class Carrinho:
    def __init__(self, products: List[Produto], carrinho_id: str):
        self._products = products
        self._carrinho_id = carrinho_id
        self._status = CarrinhoStatus.ATIVO

    def get_id(self):
        """Retorna o ID do carrinho, se não existir, cria um novo ID."""
        if not self._carrinho_id:
            self._carrinho_id = uuid.uuid4()
        return self._carrinho_id
    def add_novo_produto(self, produto: Produto):
        """Adiciona um novo produto ao carrinho."""
        self._products.append(produto)

    def remove_produto(self, produto: Produto):
        """Remove um produto do carrinho."""
        self._products.remove(produto)

    def switch(self, new_state: CarrinhoStatus):
        """Substitui a lista de produtos do carrinho por uma nova lista."""
        self._status = new_state
        return self._status
    
    def get_status(self, status: CarrinhoStatus):
        """Retorna o status atual do carrinho."""
        return self._status
    
    def _cal_subtotal(self):
        """Calcula o subtotal dos produtos disponíveis no carrinho."""
        prices = [produto.get_preco() for produto in self._products
                   if product.isavailable() is True]
        return sum(prices)
    
    def get_subtotal(self):
        """Retorna o subtotal dos produtos disponíveis no carrinho."""
        return self._cal_subtotal()
    
