lim  =  '\033[m '
ver = '\033[;31m'
verd = '\033[;32m'
amare = '\033[;33m'
azul = '\033[;34m'
ros = '\033[;35m'
cian = '\033[;36m'
cinz = '\033[;37m'
inverso = '\033[;7m'

vel = float(input(f'{ver}Digite quantos km você dirige com o seu carro: {lim}'))
if vel > 80:
    multa = (vel - 80) * 7
if vel > 80:
    print(f'{ver}MULTADO,você passou do limite!!,você vai pagar{lim} {ros}{multa}R${lim} {ver}de multa{lim}')
else:
    print(f'{verd}Você esta na lei DEUS ABENÇOE!{lim}')