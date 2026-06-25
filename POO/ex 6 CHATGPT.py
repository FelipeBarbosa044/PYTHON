class Pessoa:
    def __init__(self,nome):
        self.nome = nome


    def falar(self):
        print(f'{self.nome},esta falando...')



class Aluno(Pessoa):
    def __init__(self,nome,sala):
        super().__init__(nome)
        self.sala = sala


    def turma(self):
        print(f'{self.nome} esta na turma: {self.sala}')



a = Aluno('felipao','2adjd')
a.turma()