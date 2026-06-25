total = 0
for c in range(1,7):
    n = int(input('Digite um numero aleatorio: '))
    if n % 2 == 0:
        total += n
print(f'A soma dos numeros pares é de {total}')
