from pacote.cores import cor
def leiafloat(n):
    while True:
        try:
            nu = float(input(f'{n}'))
        except(KeyboardInterrupt):
            cor('O usuario não inseriu o valor', "vermelho")
            nu = 0
            return nu
            break
        except:
            cor('INVALIDO!!,Digite um numero real valido!!', "vermelho")

        else:
            return nu
            break


def leiaint(n = ''):
    while True:
        try:
            nu = int(input(f'{n}'))
        except(KeyboardInterrupt):
            cor('O usuario não inseriu o valor', "vermelho")
            return 0
        except:
            cor('INVALIDO!!,Digite um numero inteiro valido!!',"vermelho")
        else:
            return nu



ni = leiaint('Digite um numero inteiro: ')
nr = leiafloat('Digite um numero Real: ')
print('-'*30)

print(f'O valor INTEIRO digitado foi o: {ni}\nE o valor REAL digitado foi o {nr}')


