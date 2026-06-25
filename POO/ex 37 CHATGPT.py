from abc import ABC,abstractmethod

from pacote.matematica import leiaint
from pacote.cores import cor


class Funcionario(ABC):
    def __init__(self,nome,cargo):
        self.nome = nome.title().strip()
        self.cargo = cargo.lower()
        self.salarios = {"junior": 1200,"estagiario": 1500,"medium": 3000,"senior": 5000}

    @abstractmethod
    def CalcularSalario(self):
        pass

    @abstractmethod
    def status(self):
        pass




class Desenvolvedor(Funcionario):
    def __init__(self,nome,cargo):
        super().__init__(nome,cargo)




    def CalcularSalario(self):
        if self.cargo in self.salarios:
            for v,c in self.salarios.items():
                if v == self.cargo:
                    return  f'Salario: {c}'
        else:
            print('CARGO INVALIDO!!')

    def status(self):
        return f'NOME: {self.nome}  CARGO: {self.cargo}  PROFISSÃO: DESENVOLVEDOR {self.CalcularSalario()}'


class Desginer(Funcionario):
    def __init__(self,nome,cargo):
        super().__init__(nome,cargo)




    def CalcularSalario(self):
        if self.cargo in self.salarios:
            for v,c in self.salarios.items():
                if v == self.cargo:
                    return f'Salario: {c}'
        else:
            print('CARGO INVALIDO!!')

    def status(self):
        return f'NOME: {self.nome}  CARGO: {self.cargo}  PROFISSÃO: DESGINER  {self.CalcularSalario()}'

class Departamento:
    def cadastrar(self):
        from pacote.string import leianome
        from pacote.matematica import leiaint
        from pacote.cores import cor
        funcionarios = []
        op = ''
        ob = ''
        while op != 'N':
            profissao = leiaint('[1] Para Desenvolvedor\n[2] Para Desginer\nDigite aqui: ')
            if profissao > 2 or profissao < 1:
                cor('Digite uma opção valida!!,', "vermelho")
                continue
            if profissao == 1:
                ob = 'd'
            else:
                ob = 'D'
            nome = leianome('Digite o seu nome: ')
            cargo = leiaint("""[1] PARA JUNIOR
[2] PARA ESTAGIARIO
[3] PARA MEDIUM
[4] PARA SENIOR
DIGITE AQUI: """)
            if cargo > 4 or cargo < 1:
                cor('Digite uma oção valida!!',"vermelho")
                continue
            if cargo == 1:
                cargo = 'junior'
            if cargo == 2:
                cargo = 'estagiario'
            if cargo == 3:
                cargo = 'medium'
            if cargo == 4:
                cargo = 'senior'
            if ob == 'D':
                obj = Desginer(nome,cargo)
            else:
                obj = Desenvolvedor(nome,cargo)

            funcionarios.append(obj.status())
            op = str(input('Digite qualquer coisa para continuar\n[N] Para Ver os funcionarios \nDigite aqui: '.upper()))
            if op == 'N' or op == 'n':
                print(funcionarios)
                break





func = Departamento()
func.cadastrar()











