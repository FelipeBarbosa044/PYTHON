#maneira alternativa:
#rs = float(input('Digite quantos reais você tem na carteira: '))
#dolar = 3.27
#q = 0
#while True:
#    if dolar < rs:
#        q += 1
#        rs = rs - dolar
#    else:
#        break
#print(f'Com esse dinheiro na carteira você consegue comprar : {q} Dolares')


#### maneira correta e mais pratica:

rs = float(input('Digite quantos reais você tem na carteira: '))
con = rs / 3.27
print(f'Com esse dinheiro na carteira você consegue comprar : {round(con,2)} Dolares')


