from retangulo import  Retangulo
from rich import inspect , print

def main():
    r = Retangulo()
    try:
        r.altura = -33
        r.base = -12

        # r.medidas = (-9,3)
        print(r.medidas)
    except Exception as e:
        print(f"[red]ERRO: {e}")

    inspect(r, private=True)

if __name__ == '__main__':
    main()