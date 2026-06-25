from time import sleep
n1 = int(input('Digite um numero qualquer: '))
n2 = int(input('Digite outro numero: '))
numeros = [n1,n2]
print('=-=' * 50)
while True:
    op = int(input("""Digite [1] para SOMAR os valores informados
Digite [2] para MULTIPLICAR os valores informados
Digite [3] para mostrar o maior valor dos valores informados
Digite [4] para informar novos valores 
Digite [5] para SAIR do programa
Digite aqui: """))
    if op < 1 or op > 5:
        print('=-=' * 50)
        sleep(2)
        print('Digite uma opção valida!!')
        print('=-=' * 50)
        continue
    if op == 1:
        print('=-=' * 50)
        sleep(2)
        soma = n1 + n2
        print(f'A soma dos valores é de {soma}')
        print('=-=' * 50)
    elif op == 2:
        print('=-=' * 50)
        sleep(2)
        mult = n1 * n2
        print(f'A multiplicação dos valores é de {mult}')
        print('=-=' * 50)
    elif op == 3:
        print('=-=' * 50)
        sleep(2)
        maior = max(numeros)
        print(f'O maior numero digitado foi o {maior}')
        print('=-=' * 50)
    elif op == 4:
        print('=-=' * 50)
        sleep(2)
        n1 = int(input('Digite um numero qualquer: '))
        n2 = int(input('Digite outro numero: '))
        numeros = [n1, n2]
        print('=-=' * 50)
    else:
        break
