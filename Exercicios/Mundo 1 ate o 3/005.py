lim  =  '\033[m '
ver = '\033[;31m'
verd = '\033[;32m'
amare = '\033[;33m'
azul = '\033[;34m'
ros = '\033[;35m'
cian = '\033[;36m'
cinz = '\033[;37m'
inverso = '\033[;7m'


n = float(input(f'{inverso}Digite um numero qualquer: {lim}'))


print(f'O Sucessor desse numero é o {cian}{n+1}{lim} e o antecessor é o {ver}{n-1}')