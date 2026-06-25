n = int(input('Digite o numero que você que ver a tabuada: '))
s = 1
for c in range(n,n *10 + 1,n):
    print(f'{n} X {s} = {c}')
    s+= 1
