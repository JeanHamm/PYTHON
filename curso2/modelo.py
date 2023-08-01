class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome
    @property
    def likes(self):
        return self._likes
    def dar_likes(self):
        self._likes += 1
    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self._likes} L')

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self.duracao} min -  {self._likes} L')

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self.temporadas} temporadas -  {self._likes} L')

    
vingadores = Filme("vingadores guerra infinita", 2021, 160)
star_wars = Filme('star wars o retorno do jedi', 1968, 320)
doctor_who = Serie("Doctor Who", 1960, 2)
the_office  = Serie('the office', 2008, 10)

filmes_e_series = [vingadores, doctor_who, star_wars, the_office]

for programa in filmes_e_series:
    programa.imprime()
