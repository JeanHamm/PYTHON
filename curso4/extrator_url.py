import re

class ExtratorUrl:
    def __init__(self, url):
        self.url = self.sanitizacao_da_url(url)
        self.validacao_da_url()


    def sanitizacao_da_url(self, url):
        if(type(url) == str):
            return url.strip()
        else:
            return""
 
    def validacao_da_url(self):
    #validação da URL
        if (not self.url):
            raise ValueError("A URL está vazia")
        
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError("A url não é  valida")  



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
    
    def __len__(self):
        return len(self.url)
    
    def __str__(self):
        return self.url + "\n\n" + "Paramentros: " + self.get_url_parametros() + '\n' + "URL Base: " + self.get_url_base()
    
    def __eq__(self, other):
        return self.url == other.url