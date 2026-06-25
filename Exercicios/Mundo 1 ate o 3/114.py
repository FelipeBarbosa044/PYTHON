from urllib import request
from pacote.cores import cor

try:
    resposta = request.urlopen('http://pudim.com.br')
except:
    cor('Site indisponivel no momento!',"vermelho")
else:
    cor('Site disponivel!!',"verde")

