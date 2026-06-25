meno = 0
maio = 0

for c in range(1, 8):
    while True:
        nasci = input('Digite o ano que você nasceu: ')
        if nasci.isnumeric() and len(nasci) == 4:
            nascix = int(nasci)
            break
        else:
            print('Digite um ano válido (apenas números com 4 dígitos)!')

    if nascix >= 2007:
        meno += 1
    else:
        maio += 1

print(f'Existem {meno} pessoas que são menores de idade, e {maio} pessoas maiores de idade.')
