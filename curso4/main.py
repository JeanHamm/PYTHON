from extrator_url import ExtratorUrl

extrator_url = ExtratorUrl('https:bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real')

valor_quantidade = extrator_url.get_valor_parametro('quantidade')

print(valor_quantidade)
