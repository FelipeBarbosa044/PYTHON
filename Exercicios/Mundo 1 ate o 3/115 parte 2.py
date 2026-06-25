from pacote.cores import cor
from time import sleep
from pacote.matematica import leiaint

try:
    open('pessoas.txt', 'r').read() == ''
except:
    with open('pessoas.txt', 'x') as arquivo:
        arquivo.write('--')
else:
    cor('pessoas.txt ',"ciano",juntar=True)
    cor('foi criado com sucesso!!')

def dados():
    while True:
        print('-' * 70)
        print('MENU PRINCIPAL'.center(70))
        print('-' * 70)
        cor('1 - ',"amarelo",juntar=True) ,cor('Ver pessoas cadastradas',"rosa")
        cor('2 - ', "amarelo", juntar=True), cor('Cadastrar nova pessoa', "rosa")
        cor('3 - ', "amarelo", juntar=True), cor('Sair do sistema', "rosa")
        print('-' * 70)
        sleep(0.5)
        op = leiaint(f'{'\033[33m'}{'Digite uma opção: '}{'\033[m'}')
        if op > 3 or op < 1:
             cor('Digite uma opção valida ',"vermelho",)
             continue
        if op == 1:
            print('-'*70)
            cor('OPÇÃO 1'.center(70),"ciano")
            print('-' * 70)
            sleep(3)
            with open('pessoas.txt', 'r') as arquivo:
                arq = arquivo.read()
                if arq == '--':
                    cor('Ainda não existe nenhuma pessoa cadastrada!!',"rosa")
                else:
                    print(arq)

        if op == 2:
            print('-' * 70)
            cor('OPÇÃO 2'.center(70), "ciano")
            print('-' * 70)
            sleep(3)
        if op == 3:
            print('-' * 70)
            cor('SAINDO DO SISTEMA...'.center(70), "vermelho")
            print('-' * 70)
            sleep(3)
            break


sleep (2)
dados()