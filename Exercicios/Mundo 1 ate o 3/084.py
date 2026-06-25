cadastro = []
p = ''
pesos = []
pesado = []
leve = []
total = to = 0
while p != '0':
    n = input('Digite o seu nome: ').title()
    cadastro.append(n)
    peso = float(input(f'{n} Digite o seu peso: '))
    pesos.append(peso)
    total += 1
    p = input('''[@#rR56] Digite qualquer coisa para continuar
[0] Digite 0 para continuar:
Digite aqui: ''').strip()
for c in range (len(pesos)):
    if pesos[c] == max(pesos):
        pesado.append(c)
    if pesos[c] == min(pesos):
        leve.append(c)
print(f'Foram {total} pessoas digitadas.')
print('=-='*50)
print('As pessoa(s) mais pesadas são a(s):')
print('=-='*50)
for i,v in enumerate(pesado):
    print(f'{cadastro[v]} de {pesos[v]} kg')
print('=-='*50)
print('E a pessoa(s) mais leve são a(s: )')
print('=-='*50)
for i,v in enumerate(leve):
    print(f'{cadastro[v]} de {pesos[v]} kg')
print('=-='*50)