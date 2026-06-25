matriz0 = []
matriz1 = []
matriz2 = []
matrizoficial =[]
x = 0
linha = coluna = 0
print('MONTE UMA MATRIZ[3X3]'.center(115,'-'))
for c in range(1,10):
    n = float(input(f'Digite o {c} valor para [{linha}:{coluna}] : '))
    if coluna == 0:
        matriz0.append(n)
        matrizoficial.append(n)

    elif coluna == 1:
        matriz1.append(n)
        matrizoficial.append(n)

    else:
        matriz2.append(n)
        matrizoficial.append(n)
    coluna += 1
    if coluna == 3:
        coluna = 0
        linha+= 1
print('=-='*50)
for p,v in enumerate(matrizoficial):
    print(f'{[v]} ',end='')
    if p == 2 or p == 5 or p == 8:
        print()



print('=-='*50)










