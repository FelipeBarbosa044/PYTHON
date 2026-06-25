frase = input('Digite uma frase: ')
lim  =  '\033[m '
ver = '\033[;31m'
verd = '\033[;32m'
amare = '\033[;33m'
azul = '\033[;34m'
ros = '\033[;35m'
cian = '\033[;36m'
cinz = '\033[;37m'

#SE CONTEM NUMEROS:
n = frase.isnumeric()
####################
#Se só contém letras :
l = frase.isalpha()
#####################
#Se é alfabetico e numerico:
alnum= frase.isalnum()
#Se só contem espaço:
space = frase.isspace()
#####################
#Se só contem numeros inteiros decimais:
nu = frase.isnumeric()
######################
#Se só letras maiusculas:
maiu = frase.isupper()
#####################
#Se so contem digitos minusculos:
minu = frase.islower()
######################
#Verifica se começa com a letra maiuscula:
tit=frase.istitle()
#####################
#Tipo primitivo:
a= type(frase)
print(f'{'\033[7;0;40m'}O tipo primitivo da frase e´ {a}{lim}')
print(f'{cian}A frase só tem numeros {n}{lim}\n{verd}A frase contém letras {l}{lim}\n{ver}A frase só tem espaço {space}{lim}\n{azul}A frase so tem numeros {nu}{lim}\n{ros}A frase e´toda maiuscula {maiu}{lim}\n{ver}A frase e toda minuscula {minu}{lim}\n{cinz}A frase começa com a Letra maiscula {tit}{lim}')
print(f'{amare}É alfabetico e numerico = {alnum}{lim}')
