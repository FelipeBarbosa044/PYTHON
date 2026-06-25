lista = []
for c in range(1,6):
    n = int(input(f'Digite o {c} valor: '))
    lista.append(n)
maio = max(lista)
m = lista.index(maio)
qtm = lista.count(maio)
meno = min(lista)
n = lista.index(meno)
qtn = lista.count(meno)
print(f'O maior numero digitado foi o {maio} na posição: ')
if qtm >= 1:
    if qtm > 1:
        for p, v in enumerate(lista):
            if v == maio:
                print(p, end=' ')
    else:
        print(m+ 1,end=' ')
print('')
print('=-='* 50)
print(f'O menor numero digitado foi o {meno} na posição: ')
if qtn >= 1:
    if qtn > 1:
        for p, v in enumerate(lista,start=1):
            if v == meno:
                print(p, end=' ')
    else:
        print(n+ 1,end=' ')






