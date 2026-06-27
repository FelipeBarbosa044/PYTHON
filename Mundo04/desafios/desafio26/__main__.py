from funcionario import *

def main():
    f1 = Horista("Felipe", 12,200)
    f1.calcular_salario()
    f1.analisar_salario()

    f2 = Mensalista("Guanabara",9500)
    f2.calcular_salario()
    f2.analisar_salario()

if __name__ == "__main__":
    main()