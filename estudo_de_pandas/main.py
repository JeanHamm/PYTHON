import pandas as pd 

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
url2 = 'https://vscode.dev/github/JeanHamm/PYTHON/blob/main/estudo_de_pandas/Encantabilidade_%20CSAT%20_Tabela%20-%20Sheet1.csv'
dados = pd.read_csv(url, sep=';')
dados2 = pd.read_csv(url2, sep=',' )

print(dados2.head(5))



