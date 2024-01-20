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

class ContaCorrente(Conta):
    def __init__(self, nome, cpf, rg, nascimento):
      super().__init__(nome, cpf, rg, nascimento,)
      self.codigo_da_conta = 1
    
    def __str__(self):
        return f'-------- DADOS DO CLIENTE --------\n\nNome: {self.nome}\nData de nascimento: {self.nascimento}\nCPF: {self.cpf}\nRG: {self.rg}\nConta: {self.numero_conta} - {self.codigo_da_conta}\nAgencia: 000{self.agencia}\nBanco: {self.banco}\n\nSALDO:{self.saldo}\nLIMITE: {self.limite}\n'


class ContaSalario(Conta):
    def __init__(self, nome, cpf, rg, nascimento):
      super().__init__(nome, cpf, rg, nascimento,)
      self.codigo_da_conta = 2
    
    def __str__(self):
        return f'-------- DADOS DO CLIENTE --------\n\nNome: {self.nome}\nData de nascimento: {self.nascimento}\nCPF: {self.cpf}\nRG: {self.rg}\nConta: {self.numero_conta} - {self.codigo_da_conta}\nAgencia: 000{self.agencia}\nBanco: {self.banco}\n\nSALDO:{self.saldo}\nLIMITE: {self.limite}\n'

conta1 = ContaCorrente('Jean Michel Hamm', 13283434999, 133791809, 27122002)
conta2 = ContaSalario('Emerson Jair Hamm', 31245142423, 3281631283, 16063213)


print(conta1)
print(conta2)

