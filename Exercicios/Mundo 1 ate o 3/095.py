from time import sleep
dic = {}
dados = []
goles = []
p = ''
while p != 'N':
    dic['nome'] = str(input('Jogador Digite o seu nome: ').title())
    dic['partidas'] = int(input(f'{dic["nome"]} Digite quantas partidas jogou: '))
    for c in range(1,dic['partidas']+1):
        gol = int(input(f'Quantos gols na partida {c}?: '))
        goles.append(gol)
    dic['gols'] = goles[:]
    t = sum(goles)
    dic['total'] = t
    goles.clear()
    dados.append(dic.copy())
    while True:
        p = input('''[S] Para continuar
[N] Para PARAR
Digite aqui: ''').upper().strip()[0]
        if p not in 'SN':
            print('Digite [S] Para CONTINUAR ou [N] Para ENCERRAR')
        else:
            break
print('=-='* 50)
print('=-='* 50)
sleep(1)
print('POS:',end='')
print('NOME:'.center(10),end='')
print('GOLS:'.center(15),end='')
print('TOTAL:'.center(18),end='')
print()
p = ''
print('-'.center(50,'-'))
for p,v in enumerate(dados):
    print(f'{p} |',end='')
    print(f'{v["nome"]}'.center(8),end='')
    print(f'{v["gols"]}'.center(15),end ='')
    print(f'{v["total"]}'.center(20),end = '')
    print()
print('-'.center(50,'-'))
while p != 999:
    p = int(input(f'Digite qual jogador você quer que mostre mais estatísticas,digite a POS dele de [0 a {len(dados)}-1]\n[999] Para PARAR\nDigite aqui: '))
    if p < 0 or p > len(dados)-1:
        if p != 999:
            print('DIGITE UMA POSIÇÃO VALIDA!!')
            continue
    else:
        print(f'O jogador {dados[p]["nome"]} Teve esses dados:')
        print('_=_'*45)
        for p,v in enumerate(dados[p]['gols']):
            print(f'Na partida {p+1} ele fez {v} gol(s)')
            sleep(2)
        print('_=_' * 45)
print('_=_' * 45)
print('VOLTE SEMPRE')