class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def get_saldo(self):
        return self.__saldo
    def get_limite(self):
        return self.__limite
    
    
    def set_limite(self, limite):
        self.__limite = limite
    
    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor    

    def transferir(self, destino, valor):
        if(self.__saldo >= valor):
            self.saca(valor)
            destino.deposita(valor)
        else:
            print("\nEssa conta não tem o valor suficiente para transferir\n")
    