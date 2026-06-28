from abc import ABC, abstractmethod
from rich import print
from random import randrange, randint


class Personagem(ABC):
    """
       Classe abstrata que representa um personagem de um jogo.

       Atributos:
           nome (str): Nome do personagem.
           vida (int): Quantidade de pontos de vida do personagem.

       Métodos:
           atacar(alvo, forca): Realiza um ataque contra outro personagem.
           receber_dano(dano): Reduz a vida do personagem conforme o dano recebido.
           curar(): Método abstrato responsável por recuperar vida.
    """

    golpes = ["Bola de Fogo","Voadora Invertida","Foice Letal","Soco Biônico","Exercito de porcos","Magia Negra"]
    def __init__(self,nome,vida):
        self.nome = nome
        self.vida = vida

    def atacar(self,alvo,forca=0):
        dano = randint(0,forca)
        golpe = randrange(len(Personagem.golpes))
        print(f"[green]{self.nome}[/] atacou [red]{alvo.nome}[/]([cyan]{self.vida}[/]) com [blue]{Personagem.golpes[golpe]}[/] de força {forca}")

        alvo.receber_dano(dano)

    def receber_dano(self,dano):
        self.vida -= dano
        print(f"[blue]{self.nome}[/] recebeu [red bold]dano de[/] [red]{dano}[/]!")

    def status_jogo(self):
        print(f"O nome do personagem é [blue]{self.nome}[/], ele é um [red]{self.__class__.__name__}[/],contém [green]{self.vida} pontos de vida[/] e seus golpes são [cyan]{Personagem.golpes}[/]")

    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):
    """
       Classe que representa um guerreiro.

       Herda da classe Personagem e implementa o método de cura
       utilizando ataduras para recuperar pontos de vida.
    """
    def __init__(self,nome = None,vida = 0):
        super().__init__(nome,vida)

    def curar(self):
        cura = randint(0, 1000)
        self.vida += cura
        print(f"{self.nome} enrolou uma atadura nos ferimentos e [green]recuperou {cura} pontos[/] de vida.")


class Mago(Personagem):
    """
       Classe que representa um mago.

       Herda da classe Personagem e implementa o método de cura
       utilizando magia para recuperar pontos de vida.
    """
    def __init__(self,nome = None,vida = 0):
        super().__init__(nome,vida)

    def curar(self):
        cura = randint(0, 1000)
        self.vida += cura
        print(f"{self.nome} fez uma magia de cura e [green]recuperou {cura} pontos[/] de vida.")


