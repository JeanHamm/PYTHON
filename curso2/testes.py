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

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

class Documentario(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

vingadores = Filme("vingadores guerra infinita", 2021, 160)
star_wars = Filme('star wars o retorno do jedi', 1968, 320)
doctor_who = Serie("Doctor Who", 1960, 2)
the_office  = Serie('the office', 2008, 10)

filmes_e_series = [vingadores, doctor_who, star_wars, the_office]

for programa in filmes_e_series:
    detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
    print(f'{programa.nome} - {detalhes} - {programa.likes}')