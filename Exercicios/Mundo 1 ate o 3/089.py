print('BOLETIM ESCOLAR'.center(115,'-'))
p =''
boletim = []
temp = []
while p != '0':
    n = str(input('Digite o seu nome: ')).title()
    temp.append(n)
    n1 = float(input(f'{n} Digite a sua 1 nota: '))
    temp.append(n1)
    n2 = float(input(f'{n} Digite a sua 2 nota: '))
    temp.append(n2)
    media = (n1 + n2) / 2
    temp.append(media)
    boletim.append(temp[:])
    temp.clear()
    p = input('''[@0a..] Digite qualquer coisa para VERIFICAR MAIS BOLETINS
[0] Para MOSTRAR OS BOLETINS
Digite aqui: ''')
print('=-='*55)
print('POS:',end='')
print('NOMES:'.center(10),end='')
print('MEDIA:'.center(15),end='')
print()
print('-'*25)
for p,v in enumerate(boletim):
    print(f'{p}',end='' )
    print(f'{v[0]}'.center(12),end='')
    print(f'{v[3]}'.center(20),end='')
    print()
print('-'*25)
p = ''
while p != 999:
    p = int(input('Mostrar notas de qual aluno(999 para parar): '))
    if p < 0 or p > len(boletim) - 1:
        print(f'Digite um valor valido de (0 a {len(boletim) - 1})')
        continue
    print(f'{boletim[p][0]} Suas notas são: {boletim[p][1]} e {boletim[p][2]}')

