from diario import Diario
from rich import inspect , print


def main():
    diario = Diario()

    diario.escrever("Meu nome é felipe")
    diario.escrever("Tenho 19 anos")
    diario.escrever("Estou estudando POO em python")

    try:
        # diario.senha = 11
        diario.ler()
    except Exception as e:
        print(f"[red]ERRO: {e}[/]")



if __name__ == "__main__":
    main()