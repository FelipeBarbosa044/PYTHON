from random import choice
from time import sleep
cpu = ['🪨','🧻','✂️']
print ('Vamos jogar JOKENPO 🕹️')
player = 0
while player < 1 or player > 3:
    player = int(input("""Escolha :  pedra papel ou tesoura: 
[1] Para PEDRA 🪨
[2] Para PAPEL 🧻
[3] Para TESOURA ✂️
Digite aqui: """))
if player < 1 or player > 3:
    print('Digite uma opção valida,TENTE NOVAMENTE!!')


if player == 1:
    jogada = '🪨'
elif player == 2:
    jogada = '🧻'
else:
    jogada = '✂️'
jogadac = choice(cpu)

if jogadac == jogada:
    frase = "EMPATE!"

elif jogadac == '🧻':
    if jogada == '🪨':
        frase = 'Você PERDEU'
    elif jogada == '✂️':
        frase = 'Você GANHOU!!'

elif jogadac == '🪨':
    if jogada == '🧻':
        frase = 'Você GANHOU!!'
    elif jogada == '✂️':
        frase = 'Você PERDEU!!'

else:
    if jogada == '🧻':
        frase = 'Você PERDEU!!'
    elif jogada == '🪨':
        frase = 'Você GANHOU!!'
print('...LOADING')
sleep(2)
print(f'Você --> {jogada} VS {jogadac} <-- CPU')
print('...⚔️ BATALHANDO')
sleep(5)
print(f'{frase}')


