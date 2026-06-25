from random import sample
from time import sleep
n = int(input('Digite quantos numeros de jogadas você quer que eu sorteie: '))
cpu = 0
sorteio = []
print(f'Os {n} bilhetes foram sorteados: '.center(115,'-'))
for c in range(1,n+1):
    cpu = sample(range(1,60),6)
    cpu.sort()
    print(f'Jogo {c}: {cpu}')
    sleep(1)






