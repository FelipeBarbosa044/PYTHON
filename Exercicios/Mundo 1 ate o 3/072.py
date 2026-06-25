numeros = ('Zero','um','Dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte')
print('|Digite um numero de 0 a 20 , que eu direi a forma escrita dele|'.center(115,'-'))
while True:
    n = int(input('Digite aqui: '))
    if n < 0 or n > 20:
        print('Digite um numero de 0 A 20 !')
    else:
        break
print(numeros[n].title())


