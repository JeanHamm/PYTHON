from modelo import Filme, Serie

filme1 = Filme("vingadores guerra infinita", 2021, 160)
serie1 = Serie("Doctor Who", 1960, 2)


print(f'\nNome é {filme1.nome} do ano de {filme1.ano} e tem {filme1.duracao} min, atingiu a marca de {filme1.likes} likes\n')

print(f'Nome é {serie1.nome} do ano de {serie1.ano} e tem {serie1.temporadas} temporadas, atingiu a marca de {serie1.likes} likes\n')