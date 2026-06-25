dic = {}
nome = []
idade = []
sexo = []
mulheres = []
acima = []
p = ''
total = soma = 0
while p != 'N':
    n = str(input('Digite o seu nome: ').title())
    nome.append(n)
    id = int(input(f'{n} Digite a sua idade: '))
    idade.append(id)
    while True:
        sex = input(f'{n} Digite o seu sexo\n[F] para feminino\n[M] para masculino\nDigite aqui:  ').upper().strip()[0]
        if sex not in 'MF':
            print('Digite um SEXO VALIDO!!')
            continue
        else:
            break
    sexo.append(sex)
    total += 1
    soma += id
    p = input('''[S] Para continuar
[N] Para PARAR
Digite aqui: ''').upper().strip()[0]
dic['nomes'] = nome
dic['idades'] = idade
dic['sexos'] = sexo
print(f'Foram {total} pessoas cadastradas')
media = soma/total
print('As mulheres cadastradas foram a...')
for p,v in enumerate(sexo):
    if v == 'F':
        mulheres.append(p)
if len(mulheres) > 0:
    for m in mulheres:
        print(f' {nome[m]}|',end = '')
print('')
for p,v in enumerate(idade):
    if v > media:
        acima.append(p)
print('Aqui estão os dados das pessoas que tem idade acima da média: ')
if len(acima) > 0:
    for a in acima:
        print(f'Nome:{nome[a]} |Sexo: {sexo[a]} |Idade: {idade[a]}')











