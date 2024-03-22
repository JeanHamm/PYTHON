import random

class Pessoa:
   def __init__(self, nome, cpf, rg, nascimento):
      self.nome = nome
      self.cpf = cpf
      self.rg = rg
      self.nascimento = nascimento

class Conta(Pessoa):
   def __init__(self, nome, cpf, rg, nascimento):
      super().__init__(nome, cpf, rg, nascimento)
      self.numero_conta = random.randrange(1000, 2000)
      self.agencia = 1
      self.banco = 'HammBank'
      self.saldo = 0
      self.limite = random.randrange(9000, 10000)

      def __str__(self):
        return f'-------- DADOS DO CLIENTE --------\n\nNome: {self.nome}\nData de nascimento: {self.nascimento}\nCPF: {self.cpf}\nRG: {self.rg}\nConta: {self.numero_conta}\nAgencia; 000{self.agencia}\nBanco: {self.banco}\n\nSALDO: {self.saldo}\nLIMITE: {self.limite}\n'
      
      def saca(self, valor):
        if self.saldo >= valor:
          self.saldo -= valor
        else:
          print('Você não tem saldo suficiente')

      def deposita(self, valor):
        self.saldo += valor

class ContaCorrente(Conta):
    def __init__(self, nome, cpf, rg, nascimento):
      super().__init__(nome, cpf, rg, nascimento,)
      self.codigo_da_conta = 1
    
    def __str__(self):
        return f'-------- DADOS DO CLIENTE --------\n\nNome: {self.nome}\nData de nascimento: {self.nascimento}\nCPF: {self.cpf}\nRG: {self.rg}\nConta: {self.numero_conta} - {self.codigo_da_conta}\nAgencia: 000{self.agencia}\nBanco: {self.banco}\n\nSALDO:{self.saldo}\nLIMITE: {self.limite}\n'

    def saca(self, valor):
      if self.saldo >= valor:
          self.saldo -= valor
      else:
          print('Você não tem saldo suficiente')

    def deposita(self, valor):
        self.saldo += valor


class ContaSalario(Conta):
    def __init__(self, nome, cpf, rg, nascimento):
      super().__init__(nome, cpf, rg, nascimento,)
      self.codigo_da_conta = 2
    
    def __str__(self):
        return f'-------- DADOS DO CLIENTE --------\n\nNome: {self.nome}\nData de nascimento: {self.nascimento}\nCPF: {self.cpf}\nRG: {self.rg}\nConta: {self.numero_conta} - {self.codigo_da_conta}\nAgencia: 000{self.agencia}\nBanco: {self.banco}\n\nSALDO:{self.saldo}\nLIMITE: {self.limite}\n'
    
    def saca(self, valor):
      if self.saldo >= valor:
        self.saldo -= valor
      else:
          print('Você não tem saldo suficiente')

    def deposita(self, valor):
      self.saldo += valor


steffany = ContaCorrente("steffanny miranda krul","04505740919","130931588","16/04/2001")
jean = ContaSalario("jean michel hamm","04505740919","130931588","16/04/2001")

steffany.deposita(100)
jean.deposita(350)

print(steffany)
steffany.saca(50)

print(steffany)

print(jean)
jean.saca(350)
print(jean)
