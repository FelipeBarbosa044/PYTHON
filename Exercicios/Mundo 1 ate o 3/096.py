def area(l,c):
    a = l * c
    print('-*-'*45)
    print(f'a area é de {round(a,2)}M, tendo a largura de {l}M e comprimento de {c}m')
    print('-*-' * 45)
l = float(input('Digite a largura desse terreno: '))
c = float(input('Digite o comprimento desse terreno: '))
area(l,c)