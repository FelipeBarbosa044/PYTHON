qt = 0
n = int(input('Digite um numero aleatorio: '))
for c in range (1,999):
    if n % c == 0:
        qt += 1
if qt == 2:
    print('O numero que você digitou é PRIMO')
else:
    print('O numero que você digitou NÃO é PRIMO')