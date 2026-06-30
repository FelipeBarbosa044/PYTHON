from ex009 import *
from rich import print, inspect

def main():
    av1 = Avaliacao("Felipe","Portugues",0)
    av1.set_nota(4)
    print(f"{av1.nome} tirou {av1.get_nota()} em {av1.disciplina}")
    # inspect(av1,private=True)

if __name__ == "__main__":
    main()