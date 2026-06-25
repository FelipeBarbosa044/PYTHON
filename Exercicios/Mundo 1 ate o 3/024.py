lim  =  '\033[m '
ver = '\033[;31m'
verd = '\033[;32m'
amare = '\033[;33m'
azul = '\033[;34m'
ros = '\033[;35m'
cian = '\033[;36m'
cinz = '\033[;37m'
inverso = '\033[;7m'

cidade = input('Digite o nome de sua cidade: ').lower()
cidadex = cidade.split()
if cidadex[0] == 'santo':
    print(f'{cian}Essa cidade começa com{lim} {amare} "SANTO"{lim} {cian} em seu primeiro nome{lim} ')
else:
    print(f'{ros}Essa cidade {ver}NÃO{lim}{ros} começa com{lim}{amare} "SANTO"{lim}{ros} em seu primeiro nome ')