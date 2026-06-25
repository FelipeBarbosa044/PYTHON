from time import sleep

from pacote.cores import cor
from pacote.matematica import leiaint



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
            sleep(4)
        if op == 2:
            print('-' * 70)
            cor('OPÇÃO 2'.center(70), "ciano")
            print('-' * 70)
            sleep(4)
        if op == 3:
            print('-' * 70)
            cor('SAINDO DO SISTEMA...'.center(70), "vermelho")
            print('-' * 70)
            sleep(4)
            break




dados()
