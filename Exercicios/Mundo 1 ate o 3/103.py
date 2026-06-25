def ficha(nomex = 'Desconhecido',gols = 0):
    dic = {'Nome': nomex,'Gols': gols}
while True:
    nome = str(input('Digite o seu nome: ')).strip().title()
    if nome == '':
        nome = 'Desconhecido'
        break
    else:
        break

while True:
    gols = input(f'{nome} Quantos gols você fez: ')
    if gols.isnumeric() == True:
        break
    else:
        gols = 0
        break
jogador = ficha(nome,gols)
print(f'O jogador {jogador["Nome"]} fez {jogador["Gols"]} gols no campeonato')

