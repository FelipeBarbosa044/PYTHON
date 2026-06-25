temp = [[],[]]
for c in range(1,8):
    n = int(input(f'Digite o {c} numero: '))
    if n % 2 == 0:
        temp[0].append(n)
    else:
        temp[1].append(n)
print('Os numeros pares digitados foram os:')
print('=-='*50)
temp[0].sort()
print(temp[0])
print('=-='*50)
print('E os numeros imapres digitados foram os: ')
print('=-='*50)
temp[1].sort()
print(temp[1])
print('=-='*50)






