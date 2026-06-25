import math
catadc= float(input('Digite quantos cm tem o cateto adcajente: '))
catopo= float(input('Digite quantos cm tem o cateto oposto: '))
hip = (catadc * catadc) + (catopo * catopo)
print(f'A hipotenusa arredondada é : {math.trunc(math.sqrt(hip))}')