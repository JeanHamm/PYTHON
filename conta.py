class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    @property
    def titular(self):
        return self.__titular
    #Get __saldo
    @property
    def saldo(self):
        return self.__saldo
    
    #limites get and set
    @property
    def limite(self):
        return self.__limite
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"
    
    @staticmethod
    def codigo_dos_bancos():
        return {"BB":"001", "Caixa":"013", "Stone":"197"}
    
    
    def deposita(self, valor):
        self.__saldo += valor

    
    #Sacar o dinheiro
    def saca(self, valor):
        if(self.__pode_sacar(valor) == True):
            self.__saldo -= valor
        else:
           print("Você não tem saldo suficiente")
    
    def __pode_sacar(self, valor):
        if(valor <= self.__saldo):
            return True

    
    
    
    
    
    
    
    
    
    def transferir(self, destino, valor):
        if(valor <= self.__limite):
            self.saca(valor)
        else:
            print('Não deu certo, valor insuficiente')
        destino.deposita(valor)