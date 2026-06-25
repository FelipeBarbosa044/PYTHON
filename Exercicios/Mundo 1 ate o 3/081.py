from time import sleep

lista = []
p = ''
x = t = i5 = 0
while p != '0':
    x += 1
    n = int(input(f'Digite o {x} valor: '))
    t+= 1
    lista.append(n)
    if 5 in lista:
        i5 += 1
    p = input('[@#15ps] Digite qualquer coisa para continuar\n[0] Digite 0 para ENCERRAR\nDigite aqui: ')
desc = sorted(lista,reverse= True)
print(f'Contém {t} numeros na lista')
print(f'A lista em ordem decrescente é: {desc}')
if i5 > 0:
    print(f'O numero 5 se encontra na lista!!\nE contém {i5} 5 na lista')
else:
    print('Não contém o numero 5 na lista')






