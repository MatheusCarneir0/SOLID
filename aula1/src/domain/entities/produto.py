class Produto:
    def __init__(self, sku, preco, descricao, qtd_estoque):
        self._sku = sku
        self._preco = preco
        self._descricao = descricao
        self._qtd_estoque = qtd_estoque

    def get_preco(self):
        return self._preco

    def get_estoque(self):
        if self._qtd_estoque < 0:
            result = True
        else:
            result = False
        return result

    def get_product(self):
        return {
            "sku": self._sku,
            "preco": self._preco,
            "descricao": self._descricao,
            "quantidade": self._qtd_estoque
        }

