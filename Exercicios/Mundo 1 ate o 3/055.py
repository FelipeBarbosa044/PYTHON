lista = []
for c in range(1,6):
    peso = float(input('Digite o seu peso: '))
    lista.append(peso)
menor = min(lista)
maior = max(lista)
print(f'O MAIOR peso digitado foi de {maior}kg e o MENOR peso foi de {menor}kg')