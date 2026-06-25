while True:
    r1 = float(input('Digite quantos cm tem essa reta: '))
    r2 = float(input('Digite quantos cm tem essa reta: '))
    r3 = float(input('Digite quantos cm tem essa reta: '))
    if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2 :
        break
    else:
        print('Você não pode formar um triangulo com essas retas,TENTE NOVAMENTE.')
        print("--" * 30)

if r1 == r2 and r1 == r3 and r3 == r2:
    print('Você formou um triângulo EQUILÁTERO')
elif r1 == r2 or r1 == r3 or r2 == r3:
    print('Você formou  um triângulo ISÓCELES')
else:
    print('Você formou um triângulo ESCALENO')
