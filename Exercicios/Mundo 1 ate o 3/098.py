from time import sleep


def contador(i,f,d):
    print(f'Vou contar do {i} até o {f} , em {d} em {d} :')
    print('=-=' * 50)
    if d == 0:
        print('O PORGRAMA NÃO FUNCIONA SE O NUMERO DE PULAR AS CASAS FOR 0,TENTE NOVAMENTE!!')
        return
    if f > 0 and d > 0:
        f = f+1
    else:
        f = f-1
    for c in range(i,f,d):
        print(f'{c} ' ,end='')
        sleep(0.5)
    print()
    print('-=-'* 50)


contador(1,10,1)
contador(10,0,-2)
print('Agora é sua vez de personalizar o contador:')
i = int(input('INICIO : '))
f = int(input('FIM: '))
d = int(input('PULANDO: '))
contador(i,f,d)


