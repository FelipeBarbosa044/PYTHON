valor = float(input('Digite o valor da casa: '))
sal = float(input('Digite o valor de seu salario: '))
anos = int(input('Digite em quantos anos você vai pagar a casa no total: '))
sal30 = sal * 30/100
prestacao = valor /  (anos * 12)
if prestacao > sal30:
    print('EMPRESTIMO NEGADO!!!!,A prestação mensal execedeu mais de 30 % de seu salario')
else:
    print('EMPRESTIMO CONCEDIDO!!')

