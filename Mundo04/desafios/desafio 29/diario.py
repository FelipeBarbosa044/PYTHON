from rich import print


class Diario:
    def __init__(self, senha="12345678"):
        self.__segredos = []
        self.__senha = senha

    @property
    def senha(self):
        return self.__senha

    def escrever(self, mensagem=None):
        if mensagem == None:
            print("[red]Escreva algo no diário[/]")
        else:
            self.__segredos.append(mensagem)

    def ler(self, senha=None):
        if senha == None:
            senha = "12345678"

        if senha != self.__senha:
            print(f"[red]Senha inválida, você não pode tentar ler meu diário!")
        else:
            print(f"[green]Diário LIBERADO!")
            for verso in self.__segredos:
                print(f"- {verso}")

    @senha.setter
    def senha(self, novasenha):
        if novasenha == None:
            raise ValueError(f"Digite uma senha")

        novasenha = str(novasenha).strip()

        if novasenha == self.__senha:
            raise ValueError(f"A senha não pode ser a mesma que a anterior")

        self.__senha = novasenha
        print(f"[green]Senha alterada[/], sua nova senha é [yellow]{novasenha}")
