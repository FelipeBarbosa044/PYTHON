from pacote.cores import cor
class Jogador:
    def __init__(self,vida,mana):
        self._vida = 100
        self._mana = 50
        self.trocar_vida = vida
        self.trocar_mana = mana


    @property
    def trocar_vida(self):
        vidax = self._vida - 25
        while True:
            if vidax <= 0:
                vidax += 10
            else:
                break
        return f'VIDA:    {vidax}/{self._vida}'




    @trocar_vida.setter
    def trocar_vida(self,vida):
        from pacote.cores import cor
        if vida > 100 or vida <= 0:
            cor('A vida deve te entre 0 a 100 de life',"vermelho")
        else:
            self._vida = vida

    @property
    def trocar_mana(self):
        manax = self._mana - 20
        while True:
            if manax <= 0:
                manax+= 5
            else:
                break
        return f'MANA:    {manax}/{self._mana}'

    @trocar_mana.setter
    def trocar_mana(self, mana):
        from pacote.cores import cor
        if mana > 50 or mana <= 0:
            cor('A vida deve te entre 0 a 100 de life', "vermelho")
        else:
            self._mana = mana




g = Jogador(25,5)
print(g.trocar_vida)
print(g.trocar_mana)
print('-'*70)
g.trocar_vida = 100
g.trocar_mana = 50
print(g.trocar_vida)
print(g.trocar_mana)
