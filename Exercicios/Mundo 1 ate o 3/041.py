from time import sleep
a = 3
while True:
    ano = input('Digite o ano que você nasceu, jovem nadador: ')
    qt = len(ano)
    if qt == 4 and ano.isnumeric():
        anox = int(ano)
        break
    else:
        print('Digite um ano valido!!!,Digite novamente!')
        for c in range(0,3):
            print(a)
            sleep(1)
            a = a- 1
idade = 2025 - anox
if idade <= 9:
    print('CATEGORIA: MIRIM')
elif idade > 9 and idade <= 14:
    print('CATEGORIA: INFANTIL')
elif idade > 14 and idade <= 19:
    print('CATEGORIA: JUNIOR')
elif idade > 19 and idade <= 25:
    print('CATEGORIA: SÊNIOR')
else:
    print('CATEGORIA: MASTER')