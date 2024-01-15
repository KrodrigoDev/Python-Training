import requests
import json
import pandas as pd


def fetch_data_from_url1():
    url = 'https://dados.al.gov.br/catalogo/api/3/action/datastore_search?resource_id=fa306cbb-a609-4515-93f0-7045c6176661'
    return fetch_data_from_url(url)


def fetch_data_from_url2():
    url = 'https://dados.al.gov.br/catalogo/api/3/action/datastore_search?resource_id=b103d90a-8d37-4a3e-88d4-4651b50c6bbf'
    return fetch_data_from_url(url)


def fetch_data_from_url(url):
    # Faz a requisição à API
    requisicao = requests.get(url)

    if requisicao.status_code == 200:
        # Decodifica os bytes para uma string
        dados_str = requisicao.content.decode('utf-8')

        # Converte a string JSON para um dicionário usando o módulo json padrão
        dados_dict = json.loads(dados_str)

        # Extrai a chave 'result.records' que contém os dados que desejamos
        records = dados_dict.get('result', {}).get('records', [])

        # Normaliza os dados para lidar com estruturas aninhadas
        df = pd.json_normalize(records)

        return df
    else:
        print(f'Erro na requisição para {url}. Código de status: {requisicao.status_code}')
        return None


# Chame a função para a primeira URL
df1 = fetch_data_from_url1()

# Chame a função para a segunda URL
df2 = fetch_data_from_url2()
