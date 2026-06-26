from poligono import *

def main():
    quadrado = Quadrado(12)
    circulo = Circulo(20)


    print("Perimetro do Quadrado: " , quadrado.perimetro())
    print("Areá do Quadrado: ", quadrado.area())

    print()

    print("Perimetro do Circulo: ", circulo.perimetro())
    print("Areá do Circulo: ", circulo.area())




if __name__ == "__main__":
    main()