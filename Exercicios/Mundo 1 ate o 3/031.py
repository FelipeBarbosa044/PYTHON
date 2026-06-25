viagem = float(input("Digite a quilometragem percorrida de sua viagem: "))
if viagem <= 200:
    preco = viagem * 0.50
else:
    preco = viagem * 0.45
print(f'O preço da viagem sera de : {preco}R$')