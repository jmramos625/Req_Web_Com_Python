from urllib import request
from urllib import parse  # usado para encodar os dados e tranformar em bits para enviar na requisição

# cabeçalhos para inserção no site
cabecalho = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
             "Cookie": "cf_clearance=MZWoGtnYq6.ahoRSTWAWTYJ3M4dID83g810ysebRO2A-1656127444-0-250; PHPSESSID=hado7li853319r4cfv4cgr3t81"}

# objeto que faz nossa requisição de fato:
# req = request.Request("http://bancocn.com", headers=cabecalho)  # passamos o domínio e cabeçalho

# dados para acesso do cliente
dados = {"user": "admin", "password": "senhafoda"}  # usuário e senha
dados = parse.urlencode(dados).encode()  # convertendo os dados

# fazendo requisição com POST e enviando dados
req = request.Request("http://bancocn.com/admin/index.php", headers=cabecalho, data=dados)


resposta = request.urlopen(req)  # esse é um objeto resposta em HTTP
# como tem um firewall antes de alguns sites, e ele vai verificar que não é um navegador, ele vai bloquear a conexão

# para pegar o HTML da página, temos que ler o mesmo
html = resposta.read()
print(html)


# para que o firewall permita, precisamos definir alguma coisas forçada, como o User-Agent e os Cookies
# User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
# Cookie: cf_clearance=MZWoGtnYq6.ahoRSTWAWTYJ3M4dID83g810ysebRO2A-1656127444-0-250; PHPSESSID=hado7li853319r4cfv4cgr3t81
