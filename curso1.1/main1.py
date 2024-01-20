class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._like = 0

    def __str__(self):
        f'-------------- {self._nome} --------------\nAno: {self.ano}\n Likes: {self._like}\n'
    pass

    @property
    def dar_like(self):
        self._like += 1
    pass


class Filme(Programa):
    def __init__(self, nome, duracao, ano):
        #Ele herna o inicializado de Programa
        super().__init__(nome, ano)
        self.duracao = duracao
        pass


    def __str__(self):
       return f'-------------- {self._nome} --------------\nAno: {self.ano}\nDuração {self.duracao} \nLikes: {self._like}\n'
    pass  


class Serie(Programa):
    def __init__(self, nome, temporadas, ano):
        #Ele herna o inicializado de Programa
        super().__init__(nome, ano)
        self.temporadas = temporadas
        pass

    def __str__(self):
       return f'-------------- {self._nome} --------------\nAno: {self.ano}\nTemporadas {self.temporadas} \nLikes: {self._like}\n'
    pass   

#Estamos herdando a classe lista, fazendo nossa Playlist poder usar metodos e inicializadores da classe List
class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self.programa = programas
        pass

    def __getitem__(self, item):
        return self.programa[item]
    


filme = Filme('Avenger', 230, 2020)
for i in range(300):
    filme.dar_like
filme2 = Filme('Spider Man', 230, 2020)
for i in range(150):    
    filme2.dar_like
filme3 = Filme('Hulk', 230, 2020)
for i in range(50):    
    filme3.dar_like
serie = Serie('doctor who', 12, 1970)
for i in range(1000):    
    serie.dar_like
serie2 = Serie('Arrow', 12, 1970)
for i in range(10):    
    serie2.dar_like


lista_de_filmes = [filme, serie, filme2, filme3, serie2]
playlist_fim_de_semana = Playlist('fim de semana', lista_de_filmes)

for programa in playlist_fim_de_semana:
 
    print(programa)





