class ErrorNegocio(Exception):
    pass


class ProdutoSemEstoqueError(ErrorNegocio):
    def __init__(self, produto, estoque_disponivel):
        super().__init__(
            f"Produto '{produto}' sem estoque"
        )

class CNPJInvalidError(ValueError):
    def __init__(self, cnpj):
        super().__init__(
           f"CNPJ: {cnpj} está correto"
        )