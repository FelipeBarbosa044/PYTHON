#listanum = []
#for c in range(1,6):
    #n = int(input(f'Digite o {c} valor: '))
    #listanum.append(n)

#for p,v in enumerate(listanum):
    #if v % 2 == 0:
        #print(f'O valor {v} está na posição {p+1}')
from time import sleep
lista = []
l = i = q = 0
print(len(lista))

for c in range(1,8):
    n = int(input(f'Digite o {c} valor: '))
    lista.append(n)
print('Os valores PARES digitados foram os: ')
print('-=-'* 50)
sleep(3)
for p,v in enumerate(lista,start=1):
    q+= 1
    if v % 2 == 0:
        l+= 1
        print(f'{v} da posição {p}')
    if q == len(lista) and l < 1:
        print('Não foi digitado nenhum valor que seja PAR!!')
print('Os valores IMPARES digitados foram os: ')
print('-=-'* 50)
sleep(3)
q = 0
for p,v in enumerate(lista,start=1):
    q+= 1
    if v % 2 != 0:
        i+= 1
        print(f'{v} da posição {p}')
    if q == len(lista) and i < 1:
        print('Não foi digitado nenhum valor que seja IMPAR!!')






