from dataclasses import dataclass
import random


@dataclass
class Produto:
    nome: str
    categoria: str
    preco: float
    quantidade_estoque: int = 0
    disponivel: bool = False
    codigo: int = None

    def __post_init__(self):
        self.gerar_codigo()
        self.validar_codigo(self.codigo)

    def ativar(self):
        self.disponivel = True

    def desativar(self):
        self.disponivel = False

    def validar_codigo(self, codigo: int):
        if not isinstance(codigo, int) or codigo <= 0:
            raise ValueError('Codigo deve ser um inteiro positivo')

    def gerar_codigo(self):
        self.codigo = random.randint(1, 10000)

    def __repr__(self) -> str:
        return f'({self.codigo}, {self.nome},{self.preco})'


produto = Produto(nome='mouse', categoria='aa', preco=100)
print(produto)