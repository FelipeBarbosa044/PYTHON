n = int(input('Digite um numero qualquer: '))
x = n
z = 0
cal = n
print(f'A FATORIAL DO {n} é : '.center(100,'-'))
while x > 1:
    if x == n:
       total = n
       x -= 1
       print(f'{n} ',end ='')
    if z >= 1:
        x -= 1
    cal = total
    total = cal * x
    print (f'X {x} ',end='')
    z+= 1
print(f'= {total}',end='')
