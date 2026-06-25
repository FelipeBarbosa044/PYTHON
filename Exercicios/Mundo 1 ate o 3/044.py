print('Seja bem vindo ao produtosworld, boas compras!!'.center(100))
produto = float(input('Digite o valor do produto: '))
forma = 0
qt = 0
while forma < 1 or forma > 4:
    forma = int(input("""Digite sua forma de pagamento: 
     Se for DINHEIRO/CHEQUE Digite [1]
     Se for a VISTA NO CARTÃO Digite [2]
     Se for EM 2X NO CARTÃO Digite [3]
     Se for EM 3X OU MAIS NO CARTÃO Digite [4]
     Digite aqui: """))
    if forma < 1 or forma > 4:
        print('Digite uma opção valida,TENTE NOVAMENTE')
if forma == 1:
    des = produto - (produto * 10/100)
    print(f'Você recebeu um desconto de 10%, PARABENS , agora você vai pagar por apenas {round(des,2)}R$')
elif forma == 2:
    des = produto - (produto * 5 / 100)
    print(f'Você recebeu um desconto de 5%, PARABENS , agora você vai pagar por apenas {round(des,2)}R$')
elif forma == 3:
    print(f'Pague {produto}R$')
else:
    while qt < 3:
         qt = int(input('Em quantas vezes você deseja pagar: '))
         if qt < 3:
             print('Lembrando que não é possivel pagar por menos de 3x na parcela nessa opção')
    juros = (produto * (20/100))
    jurox = juros / qt
    print(f'Você recebeu 20% de juros,assim você vai pagar {round(produto / qt + jurox,2)}R$ por mês, e  no total você vai pagar {round(juros + produto,2)}R$ em {qt}x no cartão')


