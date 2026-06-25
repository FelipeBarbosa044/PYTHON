n = int(input('Digite um numero qualquer: '))
p = 999
bin = bin(n)
hex = hex(n)
oct = oct(n)

while p > 3:
    p = int(input('''Digite [1] para converter em BINARIO
Digite [2] para converter em OCTAL
Digite [3] para converter em HEXADECIMAL
Digite [0] para sair do programa
Digite aqui: '''))
    if p == 1:
        print(f'O numero convertido em BINARIO é {bin[2:]}')
    elif p == 2:
        print(f'O numero convertido em OCTAL é {oct[2:]}')
    elif p == 3:
        print(f'O numero convertido em HEXADECIMAL é {hex[2:]}')
    elif p == 0:
        break


