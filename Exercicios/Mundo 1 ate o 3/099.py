from time import sleep


def maior(*num):
    print('ANALISANDO...')
    if len(num) < 1:
        print('Digite algum numero porfavor!!Tente NOVAMENTE!!')
        return
    sleep(2)
    print('=-='* 30)
    print(f'Os numeros digitados foram os: ')
    for n in num:
        print(f'{n} ',end='')
        sleep(0.3)
    print()
    print(f'Foi digitado no total {len(num)} numeros')
    print(f'E o maior numero digitado foi o {max(num)}')
    print('=-=' * 30)
maior(5,2,7,5,9,4,10,3)
maior(6)
maior()
