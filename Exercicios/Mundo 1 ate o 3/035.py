r1 = float(input('Digite quantos cm tem essa reta: '))
r2 = float(input('Digite quantos cm tem essa reta: '))
r3 = float(input('Digite quantos cm tem essa reta: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2 :
    a = 'ok'
else:
    a = 'no'
if a == 'ok':
    print('Com essas retas você pode formar um triangulo')
else:
    print('Você não pode formar um triangulo com essas retas')
