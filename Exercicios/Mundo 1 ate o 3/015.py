km = (float(input('Digite quantos km você percorreu com esse carro: ')))
dias = int(input('E quantos dias você utilizou o carro depois que o alugou: '))
diass = 60 * dias
kmm = km * 0.15
print(f'Você vai ter que pagar {round(diass + kmm,3)}R$ por esse carro')