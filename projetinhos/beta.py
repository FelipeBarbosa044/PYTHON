import random

sorteio = random.randint(0,6)


class Fernandinho():
    def __init__(self,nome):
        self.nome = nome

    def ébetinha(self):
        if sorteio < 3:
            return print(f"Sim o {self.nome} é betinha")
        else:
            return print(f"Não, o {self.nome} NÃO é betinha")


nome = Fernandinho("Kaique")
nome.ébetinha()





