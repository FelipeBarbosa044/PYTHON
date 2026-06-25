import sys
lim  =  '\033[m '
ver = '\033[;31m'
verd = '\033[;32m'
amare = '\033[;33m'
azul = '\033[;34m'
ros = '\033[;35m'
cian = '\033[;36m'
cinz = '\033[;37m'
inverso = '\033[;7m'

while True:
    ano = (input('Digite o seu ano atual: '))
    qt = len(ano)
    if qt > 4 or qt < 4 or ano.isnumeric() == False:
        print(f'{ver}Digite um ano valido{lim}')
    else:
        break
digitos = ano[2]+ano[3]
ano = int(ano)
digitos = int(digitos)
if digitos == 00:
    if ano % 400 == 00:
        print(f'{amare}Esse ano é bissexto{lim}')
        sys.exit()
    else:
        print(f'{ros}Esse ano{lim}{ver}NÃO{lim}{ros}é bissexto{lim}')
        sys.exit()


if digitos % 4 == 0 :
    print(f'{amare}Esse ano é bissexto{lim}')
else:
    print(f'{ros}Esse ano{lim}{ver}NÃO{lim}{ros}é bissexto{lim}')
