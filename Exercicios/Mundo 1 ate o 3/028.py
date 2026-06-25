import random
lim  =  '\033[m '
ver = '\033[;31m'
verd = '\033[;32m'
amare = '\033[;33m'
azul = '\033[;34m'
ros = '\033[;35m'
cian = '\033[;36m'
cinz = '\033[;37m'
inverso = '\033[;7m'

print('Tente acertar o numero da cpu')
cpu = random.randint(0,5)
while True:
    player = int(input(f'{inverso}Digite um numero aleatorio de 0 a 5: {lim}'))
    if player == cpu:
        print(f'{verd}PARABENS VOCÊ ACERTOU O MEU NUMERO!!{lim}')
        break
    else:
        print(f'{ver}Você errou tente novamente!{lim}')