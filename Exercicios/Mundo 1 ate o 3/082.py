lista =  []
par = []
impar = []
x = 0
p = ''
while p != '0':
    x += 1
    n = int(input(f'Digite o {x} valor: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    p = input('[@#15ps] Digite qualquer coisa para continuar\n[0] Digite 0 para ENCERRAR\nDigite aqui: ').strip()

print(f'A lista com todos os valores é essa: {lista}')
print(f'A lista dos numeros pares é:  {par}')
print(f'A lista dos numeros impares é: {impar}')