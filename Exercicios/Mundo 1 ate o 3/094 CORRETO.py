dic = {}
pessoa = []
sexos = []
total = soma = 0
p = ''
while p != 'N':
    n = str(input('Digite o seu nome: ')).title()
    dic['nome'] = n
    ida = int(input(f'{n} Digite a sua idade: '))
    dic['idade'] = ida
    soma += ida
    while True:
        sex = input(f'{n} Digite o seu sexo\n[F] para feminino\n[M] para masculino\nDigite aqui:  ').upper().strip()[0]
        if sex not in 'MF':
            print('Digite um SEXO VALIDO!!')
            continue
        else:
            sexos.append(sex)
            dic['sexo'] = sex
            break
    pessoa.append(dic.copy())
    total += 1
    while True:
        p = input('''[S] Para continuar
[N] Para PARAR
Digite aqui: ''').upper().strip()[0]
        if p not in 'SN':
            print('Digite [S] Para CONTINUAR ou [N] Para ENCERRAR')
        else:
            break
print('_=_'*50)
print(f'No total foram {total} pessoas cadastradas')
print('_=_'*50)
print(f'A média das pessoas é de {round(soma/total),1} anos')
print('_=_'*50)
print('As mulheres cadastradas foram as: ')
if len(sexos) > 0:
    for p,v in enumerate(sexos):
        if v == 'F':
            print(f' {pessoa[p]["nome"]}|',end='')
else:
    print('Não foi cadastrada nenhuma mulher')
print()
print('_=_'*50)
print('Os dados das pessoas acima da média de idade são essas: ')
for p,v in enumerate(pessoa):
    if pessoa[p]["idade"] > soma/total:
        print(v)
print('_=_'*50)









