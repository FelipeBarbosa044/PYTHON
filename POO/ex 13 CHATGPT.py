class Pagamento:
    def pagar(self):
        from pacote.cores import cor
        cor('Processando pagamento',"verde")


class Pix(Pagamento):
    def pagar(self):
        from pacote.cores import cor
        cor('Pagamento via pix feito com sucesso! ✅',"verde")




class Cartao_De_Credito(Pagamento):
    def pagar(self):
        from pacote.cores import cor
        cor('Pagamento via cartão de crédito aprovado 💳',"verde")



class Boleto(Pagamento):
    def pagar(self):
        from pacote.cores import cor
        cor('Pagamento via boleto registrado 🗒️',"verde")


pagamentos = [Pix(),Cartao_De_Credito(),Boleto()]

for c in pagamentos:
    c.pagar()
