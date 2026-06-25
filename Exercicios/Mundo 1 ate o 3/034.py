lim  =  '\033[m '
ver = '\033[;31m'
verd = '\033[;32m'
amare = '\033[;33m'
azul = '\033[;34m'
ros = '\033[;35m'
cian = '\033[;36m'
cinz = '\033[;37m'
inverso = '\033[;7m'

sal = float(input('Digite o valor de seu salario jovem: '))
if sal > 1250:
    au1 = sal + (sal * 10/100)
    print(f'{azul}Você recebeu um aumento de{lim}{cian}10%{lim}{azul},e agora recebe:{lim}{verd}{au1}R${lim}')
elif sal <= 1250:
    au = sal + (sal * 15/100)
    print(f'{azul}Você recebeu um aumento de{lim}{cian}15%{lim},{azul}e agora recebe:{lim}{verd}{au}R${lim}')
