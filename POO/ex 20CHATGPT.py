class Personagem:
    def __init__(self,nome):
        self.nome = nome

    def info(self):
        print(f'O nome do personagem é {self.nome}')


class Mago(Personagem):



    def atacar(self):
        print('Ataque magico')


class Guerreiro(Personagem):


    def atacar(self):
        print('Ataque fisico')


class Paladino(Mago,Guerreiro):



    def atacar(self):
        super().atacar()
        Guerreiro.atacar(self)



m = Paladino('Resfera')

m.info()
m.atacar()