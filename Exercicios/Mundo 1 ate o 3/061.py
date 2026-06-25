p1 = int(input('Digite o 1 termo dessa progressão aritmética: '))
razao = int(input('Digite a razão dessa progressão aritmética: '))
x = 0
novo = p1
print('Esses sãos os 10 primeiros termos dessa progressão aritmética: '.center(120,'='))
while x < 10:
    print(f'{novo} ',end='')
    if x == 0:
        atual = p1 + razao
        novo = atual + 0
    else:
        novo = novo + razao
    x += 1


