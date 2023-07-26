from modelo import Filme, Serie

filme1 = Filme("Vingadores guerra infinita", 2021, 160)
serie1 = Serie("Doctor Who", 1960, 2)

print('O filme {} do ano de {} e tem {} minutos'. format(filme1.get_nome(), filme1.get_ano(), filme1.get_duracao()))
print('A serie {} do ano de {} e tem {} minutos'. format(serie1.get_nome(), serie1.get_ano(), serie1.get_temporadas()))
