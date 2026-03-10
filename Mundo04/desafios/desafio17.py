from rich import print
from rich.panel import Panel


class Produto:
    """"
    Representa um produto com nome e preço.

    Esta classe é usada para armazenar informações básicas de um produto
    e exibir uma etiqueta visual utilizando a biblioteca Rich.

    Atributos:
        nome (str): Nome do produto.
        preço (float): Preço do produto.

    Métodos:
        etiqueta():
            Exibe uma etiqueta visual do produto utilizando um Panel
            da biblioteca Rich.
    """
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = "R$" + preco

    def etiqueta(self):
        traços = "-" * 46
        etiqueta = Panel(f"{self.nome.center(46)}\n{traços}\n{self.preco.center(46,".")}" ,title="Produto",width=50)
        print(etiqueta)

p1 = Produto('IPhone 17 Pro Max',"25,000.85")
p1.etiqueta()

p2 = Produto("Nootbook Gamer", "8,000.00")
p2.etiqueta()
