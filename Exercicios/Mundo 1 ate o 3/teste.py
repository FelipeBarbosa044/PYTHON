from time import sleep
from pacote.matematica import avaliar, criar_aluno, leiaint
from pacote.cores import cor
from pacote.string import leianome, linha, cabecalho
produto = []

def produtos():
    global po
    po = leianome(f'{"\033[33m"}Digite um produto: {"\033[m"} ')
    produto.append(po)


def listar(produto):
    if len(produto) == 0:
        cor('AINDA NÃO HÁ NENHUM PRODUTO CADASTRADO','vermelho')
    else:
        for c in produto:
            print (c)


while True:
    while True:
        linha(50)
        cor('[1] - ',"ciano",juntar=True), cor('Cadastrar produto','azul')
        cor('[2] - ', "ciano", juntar=True), cor('Listar produtos', 'azul')
        cor('[3] - ', "ciano", juntar=True), cor('SAIR', 'vermelho')
        sleep(0.8)
        op = leiaint(f'{"\033[33m"}Escolha sua opção: {"\033[m"}')
        if op < 1 or op > 3:
            cor('Digite uma opcão valida!![do 1 ao 3]',"vermelho")
        else:
            break
    linha(50)
    if op == 1:
        produtos()
        cor('Produto cadastrado com sucesso!',"ciano")
    if op == 2:
        cor('PRODUTOS CADASTRADOS: ','amarelo')
        listar(produto)
    if op == 3:
        cor('SAINDO DO SISTEMA...',"vermelho")
        break






