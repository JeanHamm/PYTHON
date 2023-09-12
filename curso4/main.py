from extrator_url import ExtratorUrl

url = 'bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar'

extrator_url = ExtratorUrl(url)
extrator_url_2 = ExtratorUrl(url)

print("O tamnho da url é :", len(extrator_url))
print(extrator_url)

valor_quantidade = extrator_url.get_valor_parametro('quantidade')

print(valor_quantidade)
