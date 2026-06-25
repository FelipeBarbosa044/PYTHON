termo = int(input('Digite o 1 termo dessa progressão aritmética: '))
razao = int(input('Digite a razão dessa progressão aritmética: '))
ate = 0
for c in range(termo,999999999,razao):
    print(c,end = '')
    ate += 1
    if ate < 10:
        print(' - ', end='')
    if ate == 10:
        break

