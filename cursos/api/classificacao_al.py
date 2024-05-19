# Feito por Kauã Rodrigo

import warnings
from math import ceil
import mapclassify
import locale
import pandas as pd
import requests


# Função para puxar os dados de uma fonte específica
def puxar_dados(datastore_id):
    # Construindo a URL para a solicitação dos dados
    url = f'https://dados.al.gov.br/catalogo/api/3/action/datastore_search_sql?sql=SELECT * from "{datastore_id}"'
    # Fazendo a solicitação HTTP e obtendo os dados em formato JSON
    dados = requests.get(url).json()['result']['records']
    # Convertendo os dados em um DataFrame do Pandas
    return pd.DataFrame(dados)


# Função para formatar números com separadores de milhar
def formatar_numero(numero):
    # Configurando a localização para formatar o número
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    # Formatando o número e retornando como string
    return locale.format_string("%d", numero, grouping=True)


# Função para classificar os dados de um DataFrame
def classificacao(base, coluna_valor):
    try:
        # Calculando a quebra de Jenks
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")  # Ignora os avisos
            jenks_breaks = mapclassify.NaturalBreaks(base[coluna_valor], 5)
        # Calculando os intervalos completos
        intervals = [(jenks_breaks.bins[i], jenks_breaks.bins[i + 1]) for i in range(len(jenks_breaks.bins) - 1)]
        # Aplicando a classificação aos dados
        base['classificacao'] = base.apply(lambda x: aplicar_classificacao(x[coluna_valor], intervals), axis=1)
    except IndexError:
        tam_populacao = base.shape[0]
        intervalo_valores = amplitude_intervalo(base, coluna_valor, tam_populacao)
        valor_min = min(base[coluna_valor])
        qtd_classes = 5
        intervalos = []
        for i in range(qtd_classes):
            if i == 0:
                intervalos.append([valor_min, ceil(valor_min + intervalo_valores)])
            else:
                calc_intervalo = intervalos[i - 1][1]
                intervalos.append([calc_intervalo, ceil(calc_intervalo + intervalo_valores)])
        base['classificacao'] = base.apply(lambda x: aplicar_classificacao(x[coluna_valor], intervalos), axis=1)
    return base


# Função para calcular a amplitude total de uma coluna
def amplitude_total(base, coluna):
    valor_min = min(base[coluna])
    valor_max = max(base[coluna])
    return valor_max - valor_min


# Função para calcular o intervalo de amplitude de uma coluna
def amplitude_intervalo(base, coluna_valor, tam_populacao):
    ampli_total = amplitude_total(base, coluna_valor)
    return ceil(ampli_total / tam_populacao)


# Função para aplicar a classificação em um valor baseado em intervalos
def aplicar_classificacao(valor, intervalos):
    if valor <= 0:
        return 'A. 0'
    elif valor < intervalos[0][0]:
        return f'B. Até {formatar_numero(intervalos[0][0])}'
    elif intervalos[0][0] <= valor < intervalos[0][1]:
        return f'C. De {formatar_numero(intervalos[0][0])} Até {formatar_numero(intervalos[0][1])}'
    elif intervalos[1][0] <= valor < intervalos[1][1]:
        return f'D. De {formatar_numero(intervalos[1][0])} Até {formatar_numero(intervalos[1][1])}'
    elif intervalos[2][0] <= valor < intervalos[2][1]:
        return f'E. De {formatar_numero(intervalos[2][0])} Até {formatar_numero(intervalos[2][1])}'
    elif valor >= intervalos[3][0]:
        return f'F. Acima De {formatar_numero(intervalos[3][0])}'


# Função para ajustar o DataFrame removendo colunas indesejadas
def ajustes(base):
    base['valor'] = pd.to_numeric(base['valor'], errors='coerce')
    base.dropna(inplace=True)
    colunas_indesejadas = ['variavel', 'co_mun', '_full_text', 'no_mun', '_id', 'co_uf', 'no_uf', 'classificacao',
                           'valor']
    colunas_restantes = base.drop(columns=colunas_indesejadas, errors='ignore').columns.tolist()
    colunas_restantes.sort()
    return colunas_restantes


# Função principal para classificar os DataFrames
def classificar_dfs(uri):
    df_bruto = puxar_dados(uri)
    grupos = df_bruto.groupby(ajustes(df_bruto))
    df_temp = pd.DataFrame()
    for _, dados in grupos:
        dados_classificados = classificacao(dados, 'valor')
        df_temp = pd.concat([df_temp, dados_classificados], ignore_index=True)
    return df_temp


# Requisição dos dados e classificação (adicione o nome da tabela)
energia = classificar_dfs('9b2e41fc-2a03-412a-947b-30f265d5fac7')
