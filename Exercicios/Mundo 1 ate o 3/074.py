from random import randint
numeros = (
    randint(1,10),
    randint(1,10),
    randint(1,10),
    randint(1,10),
    randint(1,10),
)
print(f'Os numeros sorteados foram os : {numeros}')
print(f'O MAIOR valor digitado foi o: {max(numeros)}')
print(f'O MENOR valor digitado foi o: {min(numeros)}')
