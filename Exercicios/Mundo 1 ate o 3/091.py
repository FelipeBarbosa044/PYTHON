from random import randint
from time import sleep
from operator import itemgetter

sorteio = {'Jogador1': randint(1,6),'Jogador2':randint(1,6),'Jogador3':randint(1,6),
           'Jogador4': randint(1,6)
           }
x = 1
for k,v in sorteio.items():
    print(f'{k} caiu no dado o numero : {v}')
    sleep(1)
sorteioord = dict(sorted(sorteio.items(),key=itemgetter(1), reverse=True))
print('RANKING🏆'.center(115,'-'))
for k,v in sorteioord.items():
    print(f'{x} lugar: ficou o {k} com o valor {v} ')
    sleep(1)
    x+= 1









