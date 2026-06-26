from abc import ABC, abstractmethod


class BebidaQuente(ABC):
    """
        Classe abstrata que define o fluxo de preparo de uma bebida.

        Utiliza o padrão Template Method, onde o método `preparar()`
        controla a sequência de execução e as subclasses implementam
        as etapas específicas de mistura e serviço.
    """
    def preparar(self):
        print("--- Iniciando o Preparo ---")
        self.ferver_agua()

    def ferver_agua(self):
        print("1. Fervendo água a 100 graus Celsius.")
        self.misturar()

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass



###############

class Cafe(BebidaQuente):
    """
       Representa o preparo de um café.

       Implementa as etapas de mistura e serviço específicas
       para a preparação de café.
    """
    def misturar(self):
        print("2. Passando água pressurizada pelo pó do café moido.")
        self.servir()

    def servir(self):
        print("3. Servindo em xícara pequena.")
        print("--- Bebida Pronta ---")

###############

class Cha(BebidaQuente):
    """
      Representa o preparo de um chá.

      Implementa as etapas de infusão do sachê na água
      e o serviço da bebida.
    """
    def misturar(self):
        print("2. Mergulhando o sachê de ervas na água.")
        self.servir()

    def servir(self):
        print("3. Servindo na canelca de porcelana com limão.")
        print("--- Bebida Pronta ---")

#############
class Leite(BebidaQuente):
    """
           Representa o preparo de leite vaporizado para bebidas.

           Implementa as etapas de vaporização do leite
           e o serviço na caneca.
    """
    def misturar(self):
        print("2. Passando vapor pressurizado pelo bico de leite")
        self.servir()

    def servir(self):
        print("3. Servindo na caneca grande, já com café.")
        print("--- Bebida Pronta ---")
