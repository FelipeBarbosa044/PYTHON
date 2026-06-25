peso = float(input('Digite seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura * altura)
imcx = round(imc,1)
if imcx < 18.5:
    print(f'Seu imc é de {imcx}')
    print('ABAIXO DO PESO,VAI MALHAR OU GANHAR GORDURA, AGORA!')
elif imcx >= 18.5 and imcx < 25:
    print(f'Seu imc é de {imcx}')
    print('PESO IDEAL,PARABENS!')
elif imcx >= 25 and imcx < 30:
    print(f'Seu imc é de {imcx}')
    print('SOBREPESO,SE CUIDA HEIN!')
elif imcx >= 30 and imcx < 40:
    print(f'Seu imc é de {imcx}')
    print('OBESIDADE , VAI PERDER PESO AGORA!!')
else:
    print(f'Seu imc é de {imcx}')
    print('OBESIDADE MORBIDA, VAI CORRER,FAZER DIETA E  TREINAR AGORRAAAAAAA!')