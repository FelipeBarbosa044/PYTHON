from random import  randint

lista = []
def sortear():
    for s in range(0,5):
        n = randint(0,10)
        lista.append(n)
    print('Os valores sorteados foram os: ')
    print('-'*22)
    for n in lista:
        print(f'{n} ',end='')
    print()
    print('-' * 22)





def somapar():
    somap = 0
    for p in lista:
        if p % 2 == 0:
            somap += p
    print(f'A soma dos numeros pares é de {somap}')




sortear()

somapar()

