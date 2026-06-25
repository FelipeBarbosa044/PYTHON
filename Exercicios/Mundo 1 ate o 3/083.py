lista = []
expressao = str(input('Digite uma expressão: '))
lista.append(expressao)
parenesq = lista[0].count('(')
parendir = lista[0].count(')')
total = parendir + parenesq
a = b = 0
if total > 0:
    if parendir == parenesq:
        for p,v in enumerate(lista[0]):
            if v == '(':
                if v != ')':
                   a += 1
                   continue
        if a > 2:
           b = total
        else:
           b-= 1
if b == total:
    print('EXPRESSÃO VALIDA!!')
else:
    print('EXPRESSÃO INVALIDA!!')







