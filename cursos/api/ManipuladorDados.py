import webbrowser
import numpy as np
import requests
import json
import pandas as pd

url_base = 'https://dados.al.gov.br/catalogo/api/3/action/datastore_search?resource_id='


def obter_dados_da_url(id_url):
    resposta = requests.get(url_base + id_url)
    print(resposta.url)
    if resposta.status_code == 200:
        dados_dict = resposta.json()
        records = dados_dict.get('result', {}).get('records', [])
        return pd.json_normalize(records)
    else:
        webbrowser.open(f'https://http.cat/status/{resposta.status_code}')
        return None


def criar_labels(bins):
    index = np.array(['A', 'B', 'C', 'D', 'E'])
    labels = ['0'] + [f'{index[i]}. ' + (f'Até {int(bins[i + 1])}' if i == 0
                                          else f'Maior que {bins[i] + 0.1}' if i == len(bins) - 2
                                          else f'De {bins[i] + 0.1} a {int(bins[i + 1])}') for i in range(len(bins) - 1)]
    return labels


def aplicar_labels(dados, colunas_restantes, linha, bins, labels):
    for i, label in enumerate(labels[1:], start=1):
        condition = (dados[colunas_restantes[0]] == linha[0]) & \
                    (dados[colunas_restantes[1]] == linha[1]) & \
                    (dados.valor > bins[i - 1]) & \
                    (dados.valor <= bins[i])
        dados.loc[condition, 'classificacao'] = label

    dados.loc[dados[(dados.valor == 0)].index, 'classificacao'] = labels[0]


def classificacao(dados):
    dados['valor'] = pd.to_numeric(dados['valor'], errors='coerce')
    dados.dropna(subset=['valor'], inplace=True)

    colunas_indesejadas = ['_id', 'co_uf', 'no_uf', 'ano', 'variavel', 'co_mun', 'no_mun']
    colunas_restantes = [col for col in dados.columns if col not in colunas_indesejadas + ['valor']]

    agg = ['min', 'max']
    aux = dados.groupby(by=colunas_restantes, as_index=False)['valor'].agg(agg)
    aux['min'] = 0

    for linha in aux.itertuples(index=False):
        bins = np.ceil(np.linspace(linha[2], linha[3], 5))
        labels = criar_labels(bins)
        aplicar_labels(dados, colunas_restantes, linha, bins, labels)

    return dados


data = classificacao(obter_dados_da_url('8a46bec0-256d-4265-a49b-6c08e2441d70&limit=873935'))
