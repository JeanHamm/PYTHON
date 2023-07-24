class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    def formatada(self):
        print("{}/{}/{}".format(self.dia, self.mes, self.ano))

class Nome:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def nome_brasileiro(self):
        print(self.nome, self.sobrenome)

    def nome_americano(self):
        print(self.sobrenome, self.nome)

