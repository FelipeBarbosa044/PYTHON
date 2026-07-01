class Retangulo:
    def __init__(self,base= None,altura = None):
        self._base = base
        self._altura = altura
        self._area = None

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self,base):

        self._base = abs(base)

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        self._altura = abs(altura)

    @property
    def area(self):
        area = self._base * self._altura
        self._area = area
        return self._area

    @property
    def medidas(self):
        return f"Base : {self.base}\nAltura : {self.altura}\nÁrea {self.area}"

    @medidas.setter
    def medidas(self,medidas):
        base = medidas[0]
        altura = medidas[1]

        self._base = abs(base)
        self._altura = abs(altura)



