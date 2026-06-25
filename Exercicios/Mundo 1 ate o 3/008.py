lim  =  '\033[m '
ver = '\033[;31m'
verd = '\033[;32m'
amare = '\033[;33m'
azul = '\033[;34m'
ros = '\033[;35m'
cian = '\033[;36m'
cinz = '\033[;37m'
inverso = '\033[;7m'

mt = float(input(f'Digite um numero em {cian}métros: {lim}'))
cm = mt * 100
mm = mt * 1000
print(f'O valor convertido de {cian}metros{lim} para {verd}centimetro{lim} é igual a : {amare}{cm}{lim}{verd}cm{lim}\nE o valor convertido de {cian}métros{lim} a {ver}milimetros{lim} é {amare}{mm}{lim}{ver}milimetros{lim}')