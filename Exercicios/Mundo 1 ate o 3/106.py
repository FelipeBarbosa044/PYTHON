def cor(texto = '',cor = "branco",fund = ''):
    cores = {
    "branco": "\033[;m",
    "vermelho": "\033[31m",
    "verde": "\033[32m",
    "amarelo": "\033[33m",
    "azul": "\033[34m",
    "rosa": "\033[35m",
    "ciano": "\033[36m",
    "cinza": "\033[37m",
    "reset": "\033[m"
    }
    fundo = {
    "vermelho": "41m",
    "verde": "42m",
    "amarelo": "43m",
    "azul": "44m",
    "rosa": "45m",
    "ciano": "46m",
    "cinza": "47m",
    }


    if fund != '':
        cores = {
            "branco": "\033[;",
            "vermelho": "\033[31;",
            "verde": "\033[32;",
            "amarelo": "\033[33;",
            "azul": "\033[34;",
            "rosa": "\033[35;",
            "ciano": "\033[36;",
            "cinza": "\033[37;",
            "reset": "\033[m"
        }
        corn = f"{cores[cor]+fundo[fund]}"
        print(f'{corn}{texto}{cores["reset"]}')
        return

    print(f'{cores[cor]}{texto}{cores["reset"]}')

from time import sleep
a =''
while a != 'fim':
    cor('=-='*20,"rosa")
    a = input(f'{"\033[33m"}Função ou biblioteca: {"\033[m"}').lower()
    if a == 'fim':
        break
    cor('~~~~'*20,"rosa")
    cor(f'Acessando os conceitos de {a}',"branco",fund="azul")
    sleep(2)
    cor('=-='*20,"rosa")
    print(f'{"\033[;46m"}{help(a)}{"\033[m"}')
cor('OBRIGADO VOLTE SEMPRE',"branco","vermelho")