url = "https://www.bytebank.com.br/cambio"

import re

padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrao_url.match(url)

if not match:
    raise ValueError("A url não é  valida")

print("A url é valida")

