lista = []
p = ''
while p != '0':
    n = int(input('Digite um valor: '))
    if n in lista:
        print('Esse valor ja foi digitado,TENTE NOVAMENTE!')
        continue
    else:
        lista.append(n)
    p = input('''[@!#r02] - Digite qualquer coisa para continuar
[0] - Para ENCERRAR
Digite aqui: ''').lower()
org = sorted(lista)
print(f'Os numeros digiados em ordem crescente ficou assim:\n{org}')






