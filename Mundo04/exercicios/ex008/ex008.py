class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    """

    def __init__(self, id , nome ,saldo = 0):
        self.id = id #publico (+)
        self._titular = nome #protegido (#)
        self.__saldo = saldo #privado (-)
        print(f"Conta {self.id} criada com sucesso. Saldo atual de R${self.__saldo:,.2f}")

    def __str__(self):
        #return f"A conta {self.id} de {self.titular} tem R${self.__saldo:.2f} de saldo"
        return f"Estado atual da conta: {self.__dict__}"

    def depositar(self,valor = 0):
        valor = abs(valor)
        self.__saldo += valor
        print(f"Depósito de R${valor:,.2f} autorizado na conta {self.id}")


    def sacar(self,valor = 0):
        valor = abs(valor)
        if valor > self.__saldo:
            print(f"Saque NEGADO de R${valor:,.2f} na conta {self.id} SALDO INSUFICIENTE")
        else:
            self.__saldo -= valor
            print(f"Saque de R${valor:,.2f} autorizado na conta {self.id}")


