from uuid import uuid4
from typing import List, Optional
from enum import Enum, auto

from aula4.domain.entities.produto import Produto

class CarrinhoStatus(Enum):
    ATIVO = auto()
    FINALIZADO = auto()
    EXPIRADO = auto()


class Carrinho:
    def __init__(self, produtos: List[Produto], carrinho_id: Optional[uuid4] = None):
        self._produtos = produtos
        self._carrinho_id = carrinho_id
        self._status = CarrinhoStatus.ATIVO

    def get_carrinho_id(self):
        if self._carrinho_id is None:
            self._carrinho_id = uuid4()
        return self._carrinho_id

    def add_novo_produto(self, produto: Produto):
        self._produtos.append(produto)

    def remove_produto(self, produto: Produto):
        self._produtos.remove(produto)

    def _cal_subtotal(self):
        prices = [
            produto.get_preco() for produto in self._produtos if produto.is_disponivel()
        ]
        total = sum(prices)
        self._subtotal = total
        return total

    def get_subtotal(self):
        self._cal_subtotal()
        return self._subtotal

    def get_status(self):
        return self._status

    def switch(self, novo_status):
        self._status = novo_status
        return self._status


