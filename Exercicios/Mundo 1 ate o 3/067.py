from time import sleep
print('Digite um numero que eu mostro a TABUADA'.center(100,'-'))
n = s = 1
while True:
    n = int(input('Digite aqui o numero/Para parar digite um numero negativo: '))
    if n == 0:
        print('Digite um numero valido!')
        continue
    elif n < 0:
        break
    print('...loading')
    sleep(2)
    print('-=-' * 45)
    for c in range(n,n * 11,n):
        print(f'{n} X {s} = {c}')
        s+= 1
    print("-=-" * 45)



