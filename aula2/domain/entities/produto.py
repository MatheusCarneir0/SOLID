class Produto:
    def __init__(self, sku, nome, preco, quantidade):
        self._sku = sku
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade

    def get_sku(self):
        return self._sku

    def get_preco(self):
        return self._preco

    def is_disponivel(self):
        result = True if self._quantidade > 0 else False
        return result

