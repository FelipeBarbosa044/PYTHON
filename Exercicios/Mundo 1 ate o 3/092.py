from datetime import datetime
dic = {'Nome': input('Digite o seu nome: ').title().strip()}
while True:
    nasc = input('Digite o ano de seu nascimento: ')
    if  len(nasc) < 4 or  len(nasc) > 4:
        print('Digite um ano valido!!(de 4 digitos!!)')
        continue
    else:
        nasc = int(nasc)
        dic['nasceu no ano'] = nasc
        break
dic['CTPS'] = int(input('Digite a sua carteira de trabalho(0 se não tem): '))
idade = datetime.now().year -  dic['nasceu no ano']
dic['Idade é'] = idade
if dic['CTPS'] != 0:
    while True:
         cont = input(f'{dic["Nome"]} Digite o ano em que você foi contratado(a): ')
         if len(cont) < 4 or len(cont) > 4:
            print('Digite um ano valido!!(de 4 digitos!!)')
            continue
         else:
            cont = int(cont)
            dic['Contratado(a) no ano'] = cont
            break
    dic['SALARIO'] = float(input('Digite o seu salario: $$$'))
    apos = dic['Contratado(a) no ano'] - dic['nasceu no ano'] + 35
    dic['Vai se aposentar na idade'] = apos
print('=-='* 55)
for k,v in dic.items():
    print(f'{k} de {v}')
