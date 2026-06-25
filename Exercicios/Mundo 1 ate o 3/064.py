n = 59092039
soma = qt = 0
while n != 999:
    n = int(input('Digite um numero aleatorio,(Digite 999 para parar) : '))
    qt += 1
    soma += n
    if n == 999:
        soma = soma - 999
        qt -= 1
print(f'O total de numeros digitado foi de: {qt} vezes e a soma de todos os numeros é de : {soma} ')