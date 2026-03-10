from rich import print
from rich.panel import Panel
from rich.traceback import install

install()

class Gamer:
    def __init__(self,nome,nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = []
        self.games = ''

    def add_favoritos(self,game):
        self.favoritos.append(game)
        self.favoritos.sort()


    def ficha(self):

        games =  "\n".join(f":video_game: [blue]{game}[/]" for game in self.favoritos) #Usando JOIN



        dados = Panel(f"Nome real: [black on blue]{self.nome}[/]\nJogos favoritos:\n{games} " ,title=f"Jogador <{self.nick}>")
        print(dados)

j1 = Gamer("Felipe","Nesferaz")
j1.add_favoritos("God of war")
j1.add_favoritos("The last of us")
j1.add_favoritos("Uncharted")
j1.add_favoritos("Minecraft")
j1.ficha()

j2 = Gamer("Glivia Souza","peach_raivosa")
j2.add_favoritos("Mario Bros")
j2.add_favoritos("Call of Duty")
j2.ficha()
