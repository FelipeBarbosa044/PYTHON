from abc import ABC, abstractmethod
from rich.table import Table
from rich import  print
from rich.traceback import install

install()



class Transporte(ABC):
    """
       Classe abstrata que representa um meio de transporte para entregas.

       Armazena a distância da entrega e o valor do frete, além de fornecer
       um método para exibir uma tabela comparando os fretes de diferentes
       tipos de transporte.

       Attributes:
           distancia (float): Distância da entrega em quilômetros.
           frete (float): Valor do frete calculado.
    """
    def __init__(self,distancia=0,frete=0):
        self.distancia = distancia
        self.frete = frete

    def tabela_de_fretes(self,distancia):
        moto = Moto(distancia)
        caminhao = Caminhao(distancia)
        drone = Drone(distancia)

        tabela = Table(title="Tabela de Fretes",width=60)
        tabela.add_column("Distância")
        tabela.add_column("Tipo")
        tabela.add_column("Frete")
        tabela.add_row(f"{distancia}KM","Moto",moto.calcular_frete())
        tabela.add_row(f"{distancia}KM", "Caminhão", caminhao.calcular_frete())
        tabela.add_row(f"{distancia}KM", "Drone", drone.calcular_frete())

        print(tabela)

    @abstractmethod
    def calcular_frete(self) -> str:
        pass



####################

class Moto(Transporte):
    """
       Representa uma entrega realizada por moto.

       O frete é calculado multiplicando a distância pelo fator fixo da moto.

       Attributes:
           fator (float): Valor utilizado para calcular o frete por quilômetro.
    """
    #Atributos de classe
    fator : float =  0.50

    def __init__(self,distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        self.frete = self.distancia * Moto.fator
        return  f"R${self.frete:.2f}"


####################

class Caminhao(Transporte):
    """
        Representa uma entrega realizada por caminhão.

        O caminhão somente realiza entregas com distância mínima de 50 km.
        Caso a distância seja válida, o frete é calculado utilizando seu
        fator por quilômetro.

        Attributes:
            fator (float): Valor utilizado para calcular o frete por quilômetro.
    """
    # Atributos de classe
    fator: float = 1.20

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if(self.distancia < 50):
            return "Raio minímo de 50 km"
        else:
            self.frete = self.distancia * Caminhao.fator
            return f"R${self.frete:.2f}"

####################

class Drone(Transporte):
    """
      Representa uma entrega realizada por drone.

      O drone somente realiza entregas com distância máxima de 10 km.
      Caso a distância esteja dentro do limite, o frete é calculado
      utilizando seu fator por quilômetro.

      Attributes:
          fator (float): Valor utilizado para calcular o frete por quilômetro.
    """
    # Atributos de classe
    fator: float = 9.50

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if (self.distancia > 10):
            return "Raio máximo de 10 km"
        else:
            self.frete = self.distancia * Drone.fator
            return f"R${self.frete:.2f}"
