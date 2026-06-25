class Pessoa:
    def __init__(self,nome):
        self.nome = nome


    def falar(self):
        print(f'{self.nome},esta falando...')


class Funcionario(Pessoa):
    def __init__(self,nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self.nome},esta em reunião...')


    def trabalhar(self):
        print(f'{self.nome} esta trabalhando...')

class Administrador(Funcionario):
    def __init__(self,nome):
        super().__init__(nome)



    def trabalhar(self):
        print(F'{self.nome} esta gerenciando o sistema...')




l = Administrador('felipao')
l.falar()
l.trabalhar()
