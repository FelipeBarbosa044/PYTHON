total = 0
velho = 0
velhote = ''
qt = 0

for c in range(1,5):
    nome = input('Digite o seu nome: ').title()
    idade = int(input(f'Digite a sua idade {nome}: '))
    while True:
        sexo = input(f'M (masculino)/F (feminino) Digite uma dessas letras para sabermos o seu sexo {nome}: ').upper()
        if sexo not in 'MF':
            print('Digite uma opção de sexo valida!')
        else:
            break
    total += idade
    if sexo == 'M':
        if idade > velho:
            velho = idade
            velhote = nome
    elif sexo == 'F':
        if idade < 20:
            qt += 1

media = total / 4

print(f'A média do grupo é de {media:.1f} anos\nO homem mais velho é o {velhote} com {velho} anos\nE contém {qt} mulheres com menos de 20 anos')
