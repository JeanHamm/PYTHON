class ExtratorUrl:
    def __init__(self, url):
        self.url = self.sanitizacao_da_url(url)
        self.validacao_da_url()


    def sanitizacao_da_url(self, url):
        return url.strip()
 
    def validacao_da_url(self):
    #validação da URL
        if(self.url == ""):
            raise ValueError("A URL está vazia")
        
    def get_url_base(self):
        #Separa a base de parâmetros
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros
    
    def get_valor_parametro(self, parametro_busca):
        #Busca o valor de um parâmetro
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        #Apartir do indice do valor vai ver se tem um &, caso tenha retorna a posição, caso não retorna -1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if(indice_e_comercial == -1):
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor: indice_e_comercial]
        return valor
    
extrator_url = ExtratorUrl('https:bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real')
valor_quantidade = extrator_url.get_valor_parametro('quantidade')
print(valor_quantidade)