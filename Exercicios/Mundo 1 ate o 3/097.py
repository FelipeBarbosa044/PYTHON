from random import randint
lista = ['Olá,Mundo!','Vagner love','Taligado mano dé','OF THE KING THE POWER TE MAND THE BESTY','Oi']


def mensagem(msg):
    for p,v in enumerate(msg):
        total = len(v) + 3
        met = total/2
        print('-' * total)
        print(f' {v}')
        print('-' * total)

mensagem(lista)

