produtos = ('Cadeira',120,'Boné',53,'Calça jeans',100,'Skate',215,'Bike',250,'Tênis',300)
print('PRODUTOS E VALORES :'.center(114,'-'))
print('PRODUTOS:',end='')
print('VALORES:'.center(85),end='')
print('')
x = 0
for c in produtos:
    if x % 2 == 0:
        print(c,end='')
        total = len(c)
    if x % 2 != 0:
        cx = 50 - total
        print('.'.center(cx,'.',),end='')
        print(f'{c}R$'.center(0))
    x += 1

