s = 'SS'
while True:
    s = input('Digite o seu sexo F(Feminino)/M(Masculino): ').upper()
    if s in 'MF' and s != 'fm':
        break
    else:
        print('Digite uma opção valida!!  (M/F)')





