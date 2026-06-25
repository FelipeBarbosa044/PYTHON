from time import sleep
homens = maior =  miniempoderadas =0
p = ''
s = 'm'
while p != '0':
    print('=-=' *45)
    sleep(2)
    while True:
        print('[M] Para MASCULINO\n[F] Para FEMININO')
        s = input('Digite o seu sexo: ').upper()
        if s in 'MF' and s != 'MF':
            break
        if s not in 'MF':
            print('Digite uma opção valida!')
            print('=-=' * 45)
            sleep(2)
    print('=-=' * 45)
    sleep(1)
    idade = int(input('Digite a sua idade: '))

    if idade > 18:
        maior += 1
    if s == 'M':
        homens += 1
    if s == 'F' and idade < 20:
        miniempoderadas += 1

    p = input('[@3-p] Para continuar digite qualquer coisa\n[0] Para encerrar digite 0\nDigite aqui: ')
    print('=-=' * 45)
    sleep(2)

print(f'Contém {maior} pessoas maiores de idade\nForam cadastrados {homens} homens\nE contem {miniempoderadas} mulheres com menos de 20 anos')

