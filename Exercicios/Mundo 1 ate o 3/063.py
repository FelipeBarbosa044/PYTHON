print('SEQUENICA FIBONACCI'.center(100,'-'))
termo = int(input('Digite quantos termos você quer que eu mostre: '))
termo = termo - 3
x =  0
novo = ant = 1
print('0 1 1 ',end='')
fribonacci = [0,1,1]
while x != termo:
    novo = ant + novo
    print(f'{novo} ',end='')
    fribonacci.append(novo)
    x+= 1
    total = len(fribonacci) - 2
    ant = fribonacci[total]



