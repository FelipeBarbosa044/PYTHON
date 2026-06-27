from abc import ABC, abstractmethod
from rich.panel import Panel
from rich import print

class Funcionario(ABC):
    """
       Classe abstrata que representa um funcionário.

       Armazena informações básicas do funcionário, como nome, salário bruto
       e salário líquido. Também fornece um método para analisar o salário em
       relação ao salário mínimo e define um método abstrato para o cálculo
       do salário, que deve ser implementado pelas subclasses.

       Attributes:
           salario_minimo (float): Valor do salário mínimo utilizado na análise.
           inss (float): Percentual de desconto do INSS.
           nome (str): Nome do funcionário.
           salario_bruto (float): Salário antes dos descontos.
           salario (float): Salário líquido após o desconto do INSS.
    """
    #Atributos de Classe
    salario_minimo = 1612
    inss = 0.075

    def __init__(self,nome,salario_bruto = 0,salario = 0):
        self.nome = nome
        self.salario_bruto = salario_bruto
        self.salario = salario

    def analisar_salario(self):
        salarios_minimos = self.salario / Funcionario.salario_minimo

        conteudo = f"O salário de [blue]{self.nome}[/] ([purple]{self.__class__.__name__}[/]) é de [green]R${self.salario:.2f}[/] e corresponde a [yellow]{salarios_minimos:.1f} salários minímos[/]."

        painel = Panel(conteudo,title="Análise de Salário",width=50)
        print(painel)

    @abstractmethod
    def calcular_salario(self):
        pass


class Horista(Funcionario):
    """
        Representa um funcionário horista.

        O salário é calculado multiplicando o valor da hora pela quantidade
        de horas trabalhadas. Após esse cálculo, é aplicado o desconto do INSS
        para obter o salário líquido.

        Attributes:
            valor_hora (float): Valor recebido por hora trabalhada.
            horas_trabalhadas (float): Quantidade de horas trabalhadas.
    """
    def __init__(self,nome,valor_hora,horas_trabalhadas):
        super().__init__(nome,0,0)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas

    def calcular_salario(self):
        self.salario_bruto = self.valor_hora * self.horas_trabalhadas
        inss = self.salario_bruto * Funcionario.inss
        self.salario = self.salario_bruto - inss



class Mensalista(Funcionario):
    """
      Representa um funcionário mensalista.

      O salário bruto é informado diretamente e o salário líquido é obtido
      aplicando o desconto do INSS sobre esse valor.
    """
    def __init__(self, nome, salario_bruto):
        super().__init__(nome,salario_bruto)


    def calcular_salario(self):
        inss = self.salario_bruto * Funcionario.inss
        self.salario = self.salario_bruto - inss