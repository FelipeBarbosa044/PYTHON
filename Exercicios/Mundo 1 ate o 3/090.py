aluno = {}
aluno['nome'] = input('Digite o seu nome: ').title().strip()
aluno['media'] = float(input('Digite a sua média: '))
if aluno['media'] >= 7:
    aluno['situaçao'] = 'REPROVADO'
elif  5 <= aluno['media'] < 7:
    aluno['situaçao'] = 'RECUPERAÇÃO'
else:
    aluno['situaçao'] = 'APROVADO'
print('=-='*50)
for k,v in aluno.items():
    print(f'{k} é igual a {v}')



