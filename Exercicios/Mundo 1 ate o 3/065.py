numeros = []
qt = total = 0
n = 1
p = ''
while p != '0':
    for c in range(1,2):
        n = int(input('Digite um numero qualuqer: '))
        qt += 1
        numeros.append(n)
        total+= n
    p = (input('Se quiser parar digite [0],caso queira continuar digite qualquer coisa: ')).upper()
    if p!= '0':
        continue
media = total/qt
print(f'Você digitou {qt} valores e a média desses valores é de {media}\nO maior numero digitado foi o {max(numeros)}\nE o menor digitado foi o {min(numeros)}')



