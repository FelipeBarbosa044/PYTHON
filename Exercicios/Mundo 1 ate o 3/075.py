from time import sleep
x = 0
tupla = (
        int(input('Digite um valor aleatorio: ')),
        int(input('Digite um valor aleatorio: ')),
        int(input('Digite um valor aleatorio: ')),
        int(input('Digite um valor aleatorio: ')),
    )
v9 = tupla.count(9)
if 3 in tupla:
    v3 = tupla.index(3,0)
    print(f'A primeira vez que o numero 3 foi digitado foi na posição : {v3 + 1}')
print(f'Você digitou os valores:  {tupla}')
print(f'O numero 9 foi digitado {v9} vezes ')
print('Os numeros pares digitados foram os: ')
print('loading...')
sleep(2)
print('-=-'*50)
for c in tupla:
    if c % 2 == 0:
        x+= 1
        print(c , ' ',end ='')
if x == 0:
    print('Você não digitou nenhum numero par')
print('')
print('-=-'*50)


