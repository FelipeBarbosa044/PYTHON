from abc import ABC,abstractmethod

class Personagem(ABC):
    def __init__(self,nome):
        self.nome = nome

    @abstractmethod
    def atacar(self):
        pass



class Arqueiro(Personagem):
    def __init__(self,nome):
        super().__init__(nome)


    def atacar(self):
        print(f'{self.nome} o arqueiro esta atirando')


class Cavalheiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome)

    def atacar(self):
        print(f'{self.nome} o cavalheiro esta atacando')


cav = Cavalheiro('felipe')
arq = Arqueiro('kratos')
cav.atacar()
arq.atacar()
p = Personagem('p')
p.atacar()
