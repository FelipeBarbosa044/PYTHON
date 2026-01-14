#Declaração de classe
class Gafanhoto:
    def __init__(self): #Metodo construtor
        #atributos de instância
        self.nome = ""
        self.idade = 0

        #Métodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f"Olá {self.nome} seu pequeno gafanhoto de {self.idade} anos de idade"

#Declaração de objetos
g1 = Gafanhoto()
g1.nome = "Felipe"
g1.idade = 19
g1.aniversario()
print(g1.mensagem())


g2 = Gafanhoto()
g2.nome = "Tyago"
g2.idade = 23
print(g2.mensagem())