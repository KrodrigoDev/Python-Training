import webbrowser
import requests

# r4 = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
#
# # verificando o contéudo da resposta e outros detalhes
#
# # mostrando a url da requisição
#
# print(r4.url)
#
# # esse contéudo é o mesmo, a única coisa que vai mudar é o formato
#
# print(r4.text)
# print(r4.json())
#
# # pasagem de parâmentro dentro da url
#
# detalhe = {'limit': 5}
# r3 = requests.get(
#     'https://dados.al.gov.br/catalogo/api/3/action/datastore_search?resource_id=8a46bec0-256d-4265-a49b-6c08e2441d70',
#     params=detalhe)
#
# # Status da requisição (maneira divertida)
#
# if r3:
#     webbrowser.open(f'https://http.cat/status/200')
# else:
#     webbrowser.open(f'https://http.cat/status/{r3.status_code}')

# Redirecionando requisições com http para o https
# r5 = requests.get('http://github.com', allow_redirects=True)

# Definindo o tempo de espera pra realizar a conexão
# r5 = requests.get('http://github.com', allow_redirects=True)

##############################################################################
############################## TESTES ######################################

url = 'http://localhost:3001/alunos'

corpo = {
    "nome": "Nome",
    "sobrenome": "Sobrenome",
    "email": "email@email.com",
    "idade": "50",
    "peso": "80.04",
    "altura": "1.90"
}

response = requests.post(url, json=corpo)

if 200 <= response.status_code <= 299:
    # sucesso
    print(f'Reason: {response.reason}')
    print(f'Status da requisição: {response.status_code}')
else:
    print(f'Reason: {response.reason}')
    print(f'Status da requisição: {response.status_code}')
