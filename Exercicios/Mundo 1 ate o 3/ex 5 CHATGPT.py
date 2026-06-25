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


l = Funcionario('felipao')
l.falar()
l.trabalhar()
