import math
lim  =  '\033[m '
ver = '\033[;31m'
verd = '\033[;32m'
amare = '\033[;33m'
azul = '\033[;34m'
ros = '\033[;35m'
cian = '\033[;36m'
cinz = '\033[;37m'


ang = float(input('Digite o valor do ângulo: '))
coss = math.cos(ang)
tang = math.tan(ang)
seno = math.sin(ang)
print(f'O valor do cosseno é {azul}{round(coss,2)}{lim},do tangente é {amare}{round(tang,2)}{lim} e o seno é {ros}{round(seno,2)}{lim}')