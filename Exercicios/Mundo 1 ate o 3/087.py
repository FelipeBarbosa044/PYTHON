matriz0 = []
matriz1 = []
matriz2 = []
matrizoficial =[]
l2 = []
par = soma = total = maior =0
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
        soma += n
    total+= 1
    coluna += 1
    if total > 3 and total <= 6:
        l2.append(n)
        maior = max(l2)
    if coluna == 3:
        coluna = 0
        linha+= 1
print('=-='*50)
for p,v in enumerate(matrizoficial):
    print(f'{[v]} ',end='')
    if p == 2 or p == 5 or p == 8:
        print()
print('=-='*50)
for p,v in enumerate(matrizoficial):
    if v % 2 == 0:
        par += v
print(f'A soma de todos os PARES é de : {par}')
print('=-='*50)
print(f'A soma de todos os valores da coluna 3 --> {matriz2} e´de:')
print(f'{soma}')
print('=-='*50)
print(f'O maior valor da 2 linha --> {l2} é o :')
print(maior)
print('=-='*50)



