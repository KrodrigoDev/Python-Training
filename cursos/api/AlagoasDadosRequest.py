import webbrowser

import numpy as np
import requests
import json
import pandas as pd

url_base = 'https://dados.al.gov.br/catalogo/api/3/action/datastore_search?resource_id='
u = ''

def obter_dados_da_url(id_url):

    # Faz a requisição à API
    resposta = requests.get(url_base + id_url)

    if resposta.status_code == 200:

        # Decodifica os bytes para uma string
        dados_str = resposta.content.decode('utf-8')

        # Converte a string JSON para um dicionário usando o módulo json padrão
        dados_dict = json.loads(dados_str)

        # Extrai a chave 'result.records' que contém os dados que desejamos
        records = dados_dict.get('result', {}).get('records', [])

        # Normaliza os dados para lidar com estruturas aninhadas
        df = pd.json_normalize(records)

        return df

    else:
        webbrowser.open(f'https://http.cat/status/{resposta.status_code}')
        return None


def classificacao(dados):

    # Transformando os dados da coluna 'valor' no tipo int (NaN em caso de erro)
    dados['valor'] = pd.to_numeric(dados['valor'], errors='coerce')

    # Apagando as linhas que possuem valores NaN na coluna 'valor' e criando um novo DataFrame
    novo_conjunto = dados.dropna(subset=['valor']).reset_index(drop=True).copy()

    # Lista de colunas indesejadas (primeiro momento)
    colunas_indesejadas = ['_id', 'co_uf', 'no_uf', 'ano', 'variavel', 'co_mun', 'no_mun']

    # Exclusão de todas as colunas indesejadas
    novo_conjunto = novo_conjunto.drop(colunas_indesejadas, axis=1, errors='ignore')

    # Lista de colunas restantes
    colunas_restantes = []
    for coluna in novo_conjunto.columns:
        if coluna != 'valor':
            colunas_restantes.append(coluna)

    # agrupamento dos dados desejados com base nas colunas restantes e seus respectivos valores (max e min)
    agg = ['min', 'max']
    aux = novo_conjunto.groupby(by=colunas_restantes, as_index=False).agg(agg)

    aux.columns = colunas_restantes + agg

    aux['min'] = 0

    for row in aux.itertuples(index=False):

        bins = np.ceil(np.linspace(row[2], row[3], 5))

        labels = ['0']
        index = ['A', 'B', 'C', 'D', 'E']

        for _ in range(len(bins) - 1):
            if _ == 0:
                labels.append(f'Até {int(bins[_ + 1])}')
            elif _ == len(bins) - 2:
                labels.append(f'Maior que {bins[_] + 0.1}')
            else:
                labels.append(f'De {bins[_] + 0.1} a {int(bins[_ + 1])}')

        for _ in range(len(labels)):
            labels[_] = index[_] + '. ' + labels[_]

        for _ in range(len(bins) - 1):
            dados.loc[dados[(dados[colunas_restantes[0]] == row[0]) &
                            (dados[colunas_restantes[1]] == row[1]) &
                            (dados.valor > bins[_]) &
                            (dados.valor <= bins[_ + 1])].index, 'classificacao'] = labels[_ + 1]

        dados.loc[dados[(dados.valor == 0)].index, 'classificacao'] = labels[0]

    return dados


data = classificacao(obter_dados_da_url('8a46bec0-256d-4265-a49b-6c08e2441d70'))

print(data)