class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.valor = 0
    def deposita(self, valor):
        self.valor =+ valor

    def __str__(self):
        return f"Codigo {self.codigo} Valor: R${self.valor}"
def deposita_todas_as_contas(valor, contas):
        for conta in contas:
            conta.deposita(valor)


contas = []

for i in range(10):
    conta_do_jean = ContaCorrente(i)
    contas.append(conta_do_jean)

deposita_todas_as_contas(100, contas)

for conta in contas:
    print(conta)

