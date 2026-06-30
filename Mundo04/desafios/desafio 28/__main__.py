from termostato import Termostato
from rich import inspect

def main():
    t = Termostato()
    t.temperatura = 19
    inspect(t,private=True)
    print(f"A temperatura atual é {t.ftemperatura}")


if __name__ == "__main__":
    main()