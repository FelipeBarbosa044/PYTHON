lim  =  '\033[m '
ver = '\033[;31m'
verd = '\033[;32m'
amare = '\033[;33m'
azul = '\033[;34m'
ros = '\033[;35m'
cian = '\033[;36m'
cinz = '\033[;37m'
inverso = '\033[;7m'

n = int(input('Digite um numero qualquer: '))
x = 0
s = 1
print(f'A tabuada do {n} é :')
print (f'{amare}--{lim}' * 26)
while x != 10:
    print(f'{amare}{n}{lim} X {azul}{s}{lim}= {amare}{n * s}{lim}')
    s+= 1
    x+= 1
print (f'{amare}--{lim}' * 26)