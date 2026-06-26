from abc import ABC, abstractmethod


class Poligono(ABC):
    """
        Classe abstrata que representa um polígono.

        Esta classe serve como base para figuras geométricas que possuem
        um número definido de lados. As classes filhas devem implementar
        os métodos `perimetro()` e `area()`.

        Attributes:
            qtd_lados (int): Quantidade de lados do polígono.
    """
    def __init__(self,qtd_lados = 0):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass

#############

class Quadrado(Poligono):
    """
         Classe que representa um quadrado.

        Herda da classe Poligono e implementa os métodos para
        calcular o perímetro e a área do quadrado.

        Attributes:
            qtd_lados (int): Quantidade de lados do quadrado.
            lado (float): Comprimento de cada lado do quadrado.
    """
    def __init__(self,lado = 0):
        super().__init__(4)
        self.lado = lado

    def perimetro(self) -> float:
        perimetro = 4 * self.lado
        return perimetro


    def area(self) -> float:
        area = self.lado * self.lado
        return area

#############

class Circulo(Poligono):
    """
        Classe que representa um círculo.

        Herda da classe Poligono e implementa os métodos para
        calcular o perímetro (circunferência) e a área do círculo.

        Attributes:
            qtd_lados (int): Quantidade de lados da figura (0 para círculo).
            raio (float): Raio do círculo.
    """

    def __init__(self,raio = 0):
        super().__init__(1)
        self.raio = raio

    def perimetro(self) -> str:
        perimetro = 2 * 3.14 * self.raio
        return f"{perimetro:.2f}"

    def area(self) -> str:
        area = 3.14 * (self.raio * self.raio)
        return f"{area:.2f}"


