class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome
        self.__ano = ano
        self.__duracao = duracao

    def get_nome(self):
        return self.__nome
    def get_ano(self):
        return self.__ano
    def get_duracao(self):
        return self.__duracao

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome  = nome
        self.__ano = ano
        self.__temporadas = temporadas 

    def get_nome(self):
        return self.__nome
    def get_ano(self):
        return self.__ano
    def get_temporadas(self):
        return self.__temporadas