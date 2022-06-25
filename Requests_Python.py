# necessário instalar a biblioteca requests
# pip install requests

import requests

# sempre que verificado que tenha firewall, coloque os headers
cabecalho = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
             "Cookie": "cf_clearance=MZWoGtnYq6.ahoRSTWAWTYJ3M4dID83g810ysebRO2A-1656127444-0-250"}

# usando a função GET
# resposta = requests.get("http://bancocn.com", headers=cabecalho)  # fazendo a requisição

# dados para acesso do cliente
dados = {"user": "admin", "password": "senhafoda"}  # usuário e senha
# nessa parte do requests, não é preciso fazer o encoding dos dados

# usando a função POST
resposta = requests.post("http://bancocn.com/admin/index.php", headers=cabecalho, data=dados)

# lendo o HTML da resposta
html = resposta.text
print(html)

#
# User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
#
# Cookie: cf_clearance=MZWoGtnYq6.ahoRSTWAWTYJ3M4dID83g810ysebRO2A-1656127444-0-250; PHPSESSID=hado7li853319r4cfv4cgr3t81
