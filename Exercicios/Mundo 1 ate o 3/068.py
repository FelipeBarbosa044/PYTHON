from random import randint
from time import sleep
win = 0
print('Jogo do PAR OU IMPAR 🕹️'.center(115,'-'))
while True:
    print('[P] Para PAR\n[I] Para IMPAR')
    op = input('Digite aqui: ').upper()
    if op not in 'PI':
        print('Digite uma opcão valida!!')
        continue
    print('-=-'*45)
    sleep(2)
    if op == 'P':
        while True:
            cpu = randint(1,10)
            n = int(input('Digite aqui o numero: '))
            soma = cpu + n
            print('-=-'*45)
            sleep(2)
            if soma % 2 == 0:
                win+= 1
                print(f'VITÓRIA!!, A cpu escolheu {cpu} e você {n} e a soma deles é de {soma} que é PAR')
                print('-=-'*45)
                sleep(2)
                continue
            else:
                print(f'DERROTA!!, A cpu escolheu {cpu} e você {n} e a soma deles é de {soma} que é IMPAR')
                print('-=-'*45)
                sleep(2)
                break
    else:
        cpu = randint(1, 10)
        n = int(input('Digite aqui o numero: '))
        soma = cpu + n
        print('-=-' * 45)
        sleep(2)
        if soma % 2 != 0:
            win += 1
            print(f'VITÓRIA!!, A cpu escolheu {cpu} e você {n} e a soma deles é de {soma} que é IMPAR')
            print('-=-' * 45)
            sleep(2)
            continue
        else:
            print(f'DERROTA!!, A cpu escolheu {cpu} e você {n} e a soma deles é de {soma} que é PAR')
            print('-=-'*45)
            sleep(2)
            break
    break
print('estatísticas: '.upper() + f'Você venceu {win} vezes')








