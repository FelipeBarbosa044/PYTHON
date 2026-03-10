from time import sleep
from rich import print
from rich.traceback import install

install()

class Livro:
    def __init__(self,titulo="NULO",paginas = 0):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_Atual = 1
        print(f":open_book: [blue]Você acabou de abrir o livro '[red]{self.titulo}[/]' que tem [green]{self.paginas} páginas no total. Você agora está na [yellow]{self.pagina_Atual}[/]")

    def avancar_paginas(self,avançar = 0):
        contador = 1
        while contador < avançar + 1 and self.pagina_Atual < self.paginas:
            contador += 1
            self.pagina_Atual += 1
            print(f"Pág{self.pagina_Atual} :arrow_forward: ",end='')
            sleep(0.5)
        print(f"[blue]Você avançou {contador - 1} páginas e agora está na [yellow]página {self.pagina_Atual}[/]")
        if self.pagina_Atual == self.paginas:
            print(f":closed_book: [red]Você chegou no final do livro '{self.titulo}'[/]")




l1 = Livro("10 coisas que aprendi",20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(100)
