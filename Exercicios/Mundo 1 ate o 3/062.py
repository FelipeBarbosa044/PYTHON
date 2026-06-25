p1 = int(input('Digite o 1 termo dessa progressão aritmética: '))
razao = int(input('Digite a razão dessa progressão aritmética: '))
x =  w = total = 0
novo = p1
p = 10
print('Esses sãos os 10 primeiros termos dessa progressão aritmética: '.center(120,'='))

while True:
    print(f'{novo} ',end='')
    if x == 0 and w == 0:
        atual = p1 + razao
        novo = atual + 0
    else:
        novo = novo + razao
    x += 1
    if x == p:
        x = 0
        w += 1
        p = int(input('\nCaso queira mostrar mais termos , digite quantos termos você quer mostrar: '))
        total += p
        if p == 0:
            break
        continue
print(f'Progressão aritmética finalizada com {10 + total} termos no total')

