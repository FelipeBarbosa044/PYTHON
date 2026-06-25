from datetime import datetime
atual = datetime.now().year
def voto(nasc):
    idade = atual - nasc
    if idade >= 18:
        op = 'OBRIGATORIO'
    if idade > 65:
        op = 'OPCIONAL'
    else:
        op = 'NEGADO'
    return idade,op



while True:
    ano = input('Digite o seu ano de nascimento: ').strip()
    if len(ano) < 4 or len(ano) > 4:
        print('Digite um ano valido(DE 4 DIGITOS!!)')
        continue
    else:
        ano=int(ano)
        break
print(f'Você tem {voto(ano)[0]} anos seu voto é : {voto(ano)[1]}')


