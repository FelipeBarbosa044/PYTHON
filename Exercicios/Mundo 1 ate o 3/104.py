def leiaint(n = ''):
    global nu
    nu = input(f'{n}')
    if nu.isnumeric() == True:
        nu = int(nu)
    else:
        while nu.isnumeric() == False:
            print('ERRO,Digite um numero valido!!')
            nu = input(f'{n}')


n = leiaint('Digite um numero: ')
print(f'Você digitou o numero: {nu}')

