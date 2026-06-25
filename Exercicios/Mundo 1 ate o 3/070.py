from time import sleep
total = p1 = b = 0
p = barato = ''
produtos = []
precos = []

print('LOJINHA DO BARBOSINHA'.center(134,'-'))
while p != '0':
    produto = input('Digite o nome do produto: ')
    produtos.append(produto)
    preco = input(f'Digite o valor do {produto}: ')
    precox = float(preco)
    precos.append(precox)

    total += precox

    if precox > 1000:
        p1 += 1

    b = precos.index(min(precos))
    barato = produtos[b]

    print('-=-'*45)
    sleep(2)
    print('[0@#R.] Digite qualquer coisa para continuar\n[0] Digite 0 para ENCERRAR')
    p = input('Digite aqui: ')
    print('-=-' * 45)
    sleep(2)
print(f'O total das compra(s) é de {total}R$\nContém {p1} produtos acima de 1000R$\nE o produto mais barato é o {barato} custando {min(precos)}R$')


