def validacao_da_url(url):
    #validação da URL
    if(url == ""):
        raise ValueError("A URL está vazia")
def sanitizacao_da_url(url):
    #Sanitização da URL
    url = url.strip()
    return url
def busca_valor(valor_de_busca, url_parametros):
    #Busca o valor de um parâmetro
    parametro_busca = valor_de_busca
    indice_parametro = url_parametros.find(parametro_busca)
    indice_valor = indice_parametro + len(parametro_busca) + 1
    #Apartir do indice do valor vai ver se tem um &, caso tenha retorna a posição, caso não retorna -1
    indice_e_comercial = url_parametros.find('&', indice_valor)
    if(indice_e_comercial == -1):
        valor = url_parametros[indice_valor:]
    else:
        valor = url_parametros[indice_valor: indice_e_comercial]
    return valor

#url = 'https:bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real'
url = ""
url = sanitizacao_da_url(url)
validacao_da_url(url)

#Separa a base de parâmetros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao + 1]
url_parametros = url[indice_interrogacao:]
print(url_parametros)



valor = busca_valor('quantidade', url_parametros)

print(valor)