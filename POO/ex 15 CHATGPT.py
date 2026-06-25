class Pai1:
    def falar(self):
        print('Pai1 falou')


class Pai2:
    def falar(self):
        print('Pai2 falou')


class Filho(Pai1,Pai2):
    pass





f = Filho()

f.falar()