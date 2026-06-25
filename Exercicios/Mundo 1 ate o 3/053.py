frase = str(input('Digite uma frase: ')).lower()
frasejunta = frase.replace(' ','')
if frasejunta[::-1] == frasejunta:
    print('Essa frase é um polindromo')
else:
    print('Essa frase NÃO é um polindromo')