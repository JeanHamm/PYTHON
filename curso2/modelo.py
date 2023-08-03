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
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} L'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min -  {self._likes} L'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas -  {self._likes} L'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)
    

    
vingadores = Filme("vingadores guerra infinita", 2021, 160)
star_wars = Filme('star wars o retorno do jedi', 1968, 320)
doctor_who = Serie("Doctor Who", 1960, 2)
the_office  = Serie('the office', 2008, 10)

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
doctor_who.dar_likes()
doctor_who.dar_likes() 
the_office.dar_likes() 
the_office.dar_likes() 
star_wars.dar_likes() 
star_wars.dar_likes() 


filmes_e_series = [vingadores, doctor_who, star_wars, the_office]

playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')
for programa in playlist_fim_de_semana:
    print(programa)

