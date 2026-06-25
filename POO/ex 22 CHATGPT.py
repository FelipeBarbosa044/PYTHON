from abc import ABC,abstractmethod

class Personagem(ABC):
    def __init__(self,nome,poder):
        self.nome = nome
        self.poder = poder

    @abstractmethod
    def atacar(self):
        pass



class Arqueiro(Personagem):
    def __init__(self,nome,poder):
        super().__init__(nome,poder)



    def atacar(self):
        print(f'{self.nome} o arqueiro esta atirando uma flecha de {self.poder}')


class Cavalheiro(Personagem):
    def __init__(self, nome,poder):
        super().__init__(nome,poder)

    def atacar(self):
        print(f'{self.nome} o cavalheiro esta atacando com uma espada de {self.poder}')


class Mago(Personagem):
    def __init__(self, nome,poder):
        super().__init__(nome,poder)

    def atacar(self):
        print(f'{self.nome} lança uma bola de {self.poder}!')


personagens = [Arqueiro('VICGI','Veneno'),Cavalheiro('Petheus','Pedra'),Mago('Felmin','Dano')]


for c in personagens:
    c.atacar()


