n = int(input('Digite qual o valor que você quer sacar: '))
i100 = i50 = i20 = i10 = i1 = 0
while True:
    if n >= 100:
        n = n - 100
        i100 += 1
    elif n >= 50:
        n = n - 50
        i50 += 1
    elif n >= 20:
        n = n - 20
        i20 += 1
    elif n >= 10:
        n = n - 10
        i10 += 1
    elif n >= 1:
        n = n - 1
        i1 += 1
    else:
        break
print('Você vai receber: ')
if i100 > 0:
    print(f'{i100} células de 100R$')
if i50 > 0:
    print(f'{i50} cédulas de 50R$')
if i20 > 0:
    print(f'{i20} cédulas de 20R$')
if i10 > 0:
    print(f'{i10} cédulas de 10R$')
if i1 > 0:
    print(f'{i1} cédulas de 1R$')

