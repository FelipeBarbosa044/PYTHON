from time import sleep
br = ('palmeiras','flamengo','fluminense','bragantino','ceara','corinthians','cruzeiro','vasco da gama','juventude','são paulo','mirassol','internacional','bahia','fortaleza','botafogo','vitoria','atletico -mg','santos','grêmio','sport')


print('BRASILEIRÃO 2025 :'.center(125,'%'))
s = 0
print('-=-'*50)
sleep(2)
for c in enumerate(br,start=1):
    print(c)
print('-=-'*50)
print('Os 5 primeiros colocados do brasileirão 2025 é:')
sleep(2)
for a5 in enumerate(br,start=1,):
    print(a5,end='')
    s += 1
    if s == 5:
        s = 0
        break

print(''*50)
print('-=-' * 50)
print('A zona de REBAIXAMENTO esta preenchida com esses times:')
sleep(2)
for reb in enumerate(br[16:20],start=17):
    print(reb,end='')

print('' * 50)
print('-=-'*50)
print('O brasileirão em ordem alfabética fica assim: ')
sleep(2)
print('-=-'*50)
alfab = sorted(br)
print(alfab)
print('-=-'*50)
print('-=-'*50)
sleep(2)
print(f'Atualmente o SANTOS se encontra na posição: {br.index('santos')+1}')
