n = int(input('Digite um numero qualquer: (999 para parar): '))
qt = soma = 0

while n != 999:
    qt+= 1
    soma += n
    n = int(input('Digite um numero qualquer: (999 para parar): '))
print(f'No final você digitou {qt} numeros, e a soma deles é de {soma}')


