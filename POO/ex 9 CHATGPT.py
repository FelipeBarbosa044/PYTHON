class Instrumento:
    def tocar(self):
        print('Esse instrumento faz esse barulho!!...🎶🎶')


class Violao(Instrumento):
    def tocar(self):
        print('🎻🎻🎶')


class Piano(Instrumento):
    def tocar(self):
        print('🎹🎹🎶')


instru = Instrumento()
piano = Piano()
violao = Violao()

violao.tocar()
piano.tocar()
instru.tocar()