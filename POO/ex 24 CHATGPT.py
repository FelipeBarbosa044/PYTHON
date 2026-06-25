from abc import ABC,abstractmethod

class Personagem(ABC):
    def __init__(self,nome,poder,vida = 150):
        self.nome = nome
        self.poder = poder
        self._vida = vida


    def get_vida(self):
        return self._vida

    @abstractmethod
    def atacar(self):
        pass

    @abstractmethod
    def ataque_especial(self):
        pass



class Arqueiro(Personagem):
    def __init__(self,nome,poder,vida = 150):
        super().__init__(nome,poder,vida)


    def atacar(self):
        print(f'{self.nome} o arqueiro esta atirando uma flecha de {self.poder}')


    def ataque_especial(self, personagem):
        from pacote.cores import cor
        if isinstance(personagem, Personagem) == False:
            cor('ERRO, esse personagem não existe!!!', "vermelho")
        else:
            from random import randint
            especial = randint(30, 50)
            print(f'{self.nome} o ARQUEIRO usou o seu especial\nE retirou {eval(f'-{especial}')} da vida do {personagem.nome}  ')
            print('-'*70)
            personagem._vida -= especial


class Cavalheiro(Personagem):
    def __init__(self, nome,poder,vida=150):
        super().__init__(nome,poder,vida)

    def atacar(self):
        print(f'{self.nome} o cavalheiro esta atacando com uma espada de {self.poder}')

    def ataque_especial(self, personagem):
        from pacote.cores import cor
        if isinstance(personagem, Personagem) == False:
            cor('ERRO, esse personagem não existe!!!', "vermelho")
        else:
            from random import randint
            especial = randint(30, 50)
            print(f'{self.nome} o CAVALEIRO usou o seu especial\nE retirou {eval(f'-{especial}')} da vida do {personagem.nome}  ')
            print('-'*70)
            personagem._vida -= especial


class Mago(Personagem):
    def __init__(self, nome,poder,vida=150):
        super().__init__(nome,poder,vida)


    def atacar(self):
        print(f'{self.nome} lança uma bola de {self.poder}!')

    def ataque_especial(self, personagem):
        from pacote.cores import cor
        if isinstance(personagem, Personagem) == False:
            cor('ERRO, esse personagem não existe!!!', "vermelho")
        else:
            from random import randint
            especial = randint(30, 50)
            print(f'{self.nome} o MAGO  usou o seu especial\nE retirou {eval(f'-{especial}')} da vida do {personagem.nome}  ')
            print('-'*70)
            personagem._vida -= especial


def status(personagem):
    from pacote.cores import cor
    if isinstance(personagem, Personagem) == False:
        cor('ERRO, esse personagem não existe!!!', "vermelho")
    else:
        print(f'Nome: {personagem.nome}      Vida: {personagem.get_vida()}')
        print('-' * 70)




felipe = Mago('Felipe','fedor')
joao = Arqueiro('joazin',"agua")
silvio = Cavalheiro('Silvio', 'diamante')
status(joao)
status(felipe)
status(silvio)

felipe.ataque_especial(joao)
joao.ataque_especial(silvio)
silvio.ataque_especial(felipe)

status(joao)
status(felipe)
status(silvio)


