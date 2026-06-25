dic = {'nome': str(input('Jogador Digite o seu nome: ').title()),'partidas':int(input('Digite quantas partidas jogou: '))
    }
goles = []
for c in range(1,dic['partidas']+1):
    gol = int(input(f'Quantos gols na partida {c}?: '))
    goles.append(gol)
dic['gols'] = goles[:]
t = sum(goles)
dic['Total'] = t
print('=-='* 50)
print(dic)
print('=-='* 50)
for k,v in dic.items():
    print(f'{k} é de {v}')
print('=-='*50)
print(f'O {dic['nome']} jogou {dic['partidas']} partidas')
x = 1
for c in dic['gols']:
    print(f'==> Na partida{x}, ele fez {c} gols')
    x+= 1
print(f'Foi um total de {t} gols')

