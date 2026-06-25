palavras = (
    'aprender','Programar','linguagem','python','curso'
    ,'gratis','estudar','praticar','trabalhar','mercado','programador','futuro')
a = e = i = o = u = 0
for c in palavras:
    print(f'\nNa palavra {c.title()} temos : ',end='')
    if 'a' in c.lower():
        a = c.count('a')
        for aa in range(0,a):
            print('a ',end='')

    if 'e' in c.lower():
        e = c.count('e')
        for ee in range(0,e):
            print('e ',end='')

    if 'i' in c.lower():
        i = c.count('i')
        for ii in range(0,i):
            print('i ',end='')

    if 'o' in c.lower():
        o = c.count('o')
        for oo in range(0,o):
            print('o ',end='')

    if 'u' in c.lower():
        u = c.count('u')
        for uu in range(0, u):
            print('u ', end='')








