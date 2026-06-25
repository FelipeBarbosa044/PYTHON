class Dancarino:
    def __init__(self,nome):
        self.nome = nome


    def dancar(self):
        print(f'{self.nome} esta dançando💃')


class Cantor:
    def __init__(self,nome):
        self.nome = nome


    def cantar(self):
        print(f'{self.nome} esta cantando🎤')


class Artista(Cantor,Dancarino):
    def __init__(self,nome):
        super().__init__(nome)


    def arte(self):
        super().dancar()
        super().cantar()


artista = Artista('felipao')
artista.arte()

