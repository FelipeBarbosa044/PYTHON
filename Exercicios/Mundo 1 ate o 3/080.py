from time import sleep

lista = []
insert = p = a = s = atual = media = n = i = imex = imax =  0
ime  = 123746578463
ima = -4545455454
for c in range(1,6):
    n = int(input(f'Digite o {c} valor: '))
    if c == 1:
        lista.insert(0,n)
        a = p = n
        insert+= 1
        s += n
        print('Adicionando na lista...')
        sleep(2)
        continue
    elif c == 2:
        if n < a:
            print('Adicionando na 1 posicão...')
            sleep(2)
            a = n
            s+= n
            insert += 1
            lista.insert(0,n)
            continue
        if n > a:
            print('Adicionando na ultima posição...')
            sleep(2)
            p = n
            s += n
            insert += 1
            lista.insert(6, n)
            continue
        else:
            print('Adicionando na mesma posição...')
            sleep(2)
            s += n
            insert += 1
            i = n
            total = len(lista)
            lista.insert(total-1, n)
            continue
    media = s / insert
    if n > media:
        if n > media:
            if n < ima:
                print('Adicionando nas ultimas posições...<<MEDIA>>')
                sleep(2)
                s += n
                insert += 1
                lista.insert(lista.index(ima) - imax, n)
                continue
            if n >= p:
                print('Adicionando na ultima posição...')
                sleep(2)
                p = n
                s += n
                insert += 1
                lista.insert(6, n)
                continue
            else:
                print('Adicionando no meio...>MEDIA')
                sleep(2)
                s += n
                insert += 1
                lista.insert(lista.index(p), n)
                continue
        if n < p:
            print('Adicionando no meio...>>MEDIA')
            sleep(2)
            s += n
            ima = n
            imax += 1
            insert += 1
            lista.insert(lista.index(p)-1, n)
            continue
    if n < media:
        if n > ime:
            print('Adicionando nas primeiras posições...<<MEDIA>>')
            sleep(2)
            s += n
            insert += 1
            lista.insert(lista.index(ime) + imex, n)
            ime = n
            continue
        if n <= a:
            if n == a:
                print('Adicionando nas primeiras posições...')
                sleep(2)
                s += n
                insert += 1
                lista.insert(lista.index(a), n)
                continue
            else:
                print('Adicionando nas ultimas posições...<MEDIA')
                sleep(2)
                s += n
                a = n
                insert += 1
                lista.insert(0, n)
                continue
        if n > a:
            print('Adicionando nas primeiras posições...<<MEDIA')
            sleep(2)
            s += n
            ime = n
            imex += 1
            insert += 1
            lista.insert(lista.index(a)+ 1, n)
            continue
    else:
         print('Adicionando no meio...MEIO')
         sleep(2)
         s += n
         insert += 1
         total = len(lista)
         meio = insert//2
         lista.insert(meio,n)
         continue
print(lista)
