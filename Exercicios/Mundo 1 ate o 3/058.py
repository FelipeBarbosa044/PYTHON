from random import randint
print('Tente advinhar o numero da cpu'.center(100,'-'))
player = 11
qt = 0
cpu = randint(0,10)
while True:
    player = int(input('Digite um numero de 0 a 10 : '))
    qt += 1
    if player < 0 or player > 10:
        qt -= 1
        print('DIGITE UM NUMERO DE O A 10')
        continue
    if player == cpu:
        break
print(f'Você precisou de {qt} tentativas para acertar o meu numero,o numero era o {cpu}')

