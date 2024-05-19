import requests as rs


try:
    request = rs.get('https://pudim.com.br/')
except rs.exceptions.ConnectionError:
    print('Ocorreu um erro na conexão com o site.')
except rs.exceptions.InvalidSchema:
    print('A URI está incompleta')
else:
    if request.status_code == 200:
        print('Consegui acessar o site Pudim com sucesso!')
