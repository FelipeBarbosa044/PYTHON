class Avaliacao:

    def __init__(self,nome,disciplina,nota = 0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota #Atributo Protected (#)

    #Criando atributos Validavel
    @property
    def nota(self):##Getter
        return self._nota

    @nota.setter
    def nota(self,nota): # Método Setter
        if 0 <= nota <= 10:
            self._nota = nota
        else:
            print("Nota inválida!")

    @nota.deleter
    def nota(self):
        pass




