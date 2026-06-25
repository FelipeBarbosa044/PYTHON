from time import sleep
a = 3
while True:
    ano = input('Digite o ano que você nasceu: ')
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
if idade < 18:
    tempo = 18 - idade
    print(f'Você ainda vai se alistar,falta {tempo} anos para isso,você vai se alistar em {2025 + tempo}')
elif idade == 18:
    print(f'Ja chegou a hora de se alistar!! você ja pode se alistar esse ano')
else:
    tempo = idade - 18
    print(f'Ja passou a hora de se alistar,VAI SE ALISTAR AGORA,VOCÊ ESTA ATRASADO POR {tempo} ANO(S)!\nERA PARA VOCê TER SE ALISTADO EM {2025 - tempo}')



