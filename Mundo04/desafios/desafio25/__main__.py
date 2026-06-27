from transporte import *
from rich import print

def main():
    moto = Moto(20)
    caminhao = Caminhao(80)
    drone = Drone(8)

    print(f"Frete de {type(moto).__name__} em {moto.distancia}KM = [green]{moto.calcular_frete()}[/]")

    print(f"Frete de {type(caminhao).__name__} em {caminhao.distancia}KM = [green]{caminhao.calcular_frete()}[/]")

    print(f"Frete de {type(drone).__name__} em {drone.distancia}KM = [green]{drone.calcular_frete()}[/]")

    moto.tabela_de_fretes(100)

if __name__ == "__main__":
    main()