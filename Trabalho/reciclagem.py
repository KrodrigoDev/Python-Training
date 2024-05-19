import numpy as np
import pandas as pd


def ler_dados(ano):
    if ano == 2021:
        caminho = '../Trabalho/arquivos/Planilha_Indicadores_RS_2021.xls'
    elif ano == 2022:
        caminho = '../Trabalho/arquivos/Planilha_Indicadores_RS_2022.xlsx'

    # Dados do indicador
    rs = pd.read_excel(caminho, skiprows=6)

    # Dados do IBGE (ano de 2022)
    pop = pd.read_csv('../Trabalho/arquivos/tabela4709.csv', sep=';', skiprows=1)

    return rs, pop


def ajustes_rs(rs, ano):
    # Filtrando apenas os dados relevantes
    colunas_desejadas = ['Código do município', 'Município', 'UF',
                         'Taxa de recuperação de recicláveis em relação à quantidade de RDO e RPU',
                         'Nome do orgão responsável pela gestão', 'Sigla'
                         ]

    if ano == 2022:
        colunas_desejadas.insert(-1, 'Sigla do orgão responsável pela gestão')
        colunas_desejadas.remove('Sigla')

    rs = rs[colunas_desejadas].copy()

    # Renomeando a coluna
    rs.rename(columns={'Taxa de recuperação de recicláveis em relação à quantidade de RDO e RPU': 'Taxa do RDO e RPU'},
              inplace=True)

    # Verifica se o valor na coluna é NaN
    rs['Preenchimento'] = rs['Taxa do RDO e RPU'].apply(
        lambda linha: 'Não preencheu' if pd.isna(linha) else 'Preencheu'
    )

    # Removendo o índice 0 que contém apenas '-'
    rs.drop(index=0, inplace=True)

    # Ordenar pelos valores da coluna 'UF'
    rs.sort_values('UF', inplace=True)

    return rs


def ajustes_pop(pop):
    pop = pop.copy()

    pop.rename(columns={'Unnamed: 3': 'População'}, inplace=True)
    pop.dropna(inplace=True)

    pop['UF'] = pop['Município'].apply(lambda linha: linha[-3:-1])
    pop['Município'] = pop['Município'].apply(lambda linha: linha[:len(linha) - 4].strip())

    pop = pop[['Município', 'UF', 'População']]
    return pop


def mesclagem(pop, rs):
    merged_data = pd.merge(pop, rs, how='inner', on=['UF', 'Município'])
    return merged_data


def calc(dados, pop_bruto):
    dados = dados.query('Preenchimento == "Preencheu"').reset_index()

    # Convertendo a taxa para porcentagem
    dados['Taxa do RDO e RPU'] = dados['Taxa do RDO e RPU'] / 100

    # Calculando a proporção
    dados['Proporção'] = dados['População'] * dados['Taxa do RDO e RPU']

    # Calculando a soma da proporção por UF
    soma_proporcao = dados.groupby('UF')['Proporção'].sum().reset_index()

    # Calculando a soma da população por UF
    soma_pop = pop_bruto.groupby('UF')['População'].sum().reset_index()

    # Mesclando os DataFrames com base na coluna 'UF'
    df_final = pd.merge(soma_proporcao, soma_pop, on='UF')

    # Calculando a proporção final
    df_final['Taxa'] = df_final['Proporção'] / df_final['População']

    df_final = ponderar(df_final)
    return df_final


def ponderar(base):
    base['Taxa'] = pd.to_numeric(base['Taxa'], errors='coerce')

    base['Normalização'] = np.round(
        100 * (base['Taxa'] - base['Taxa'].min()) / (base['Taxa'].max() - base['Taxa'].min()), 2)

    base = base.sort_values('Normalização', ascending=False).reset_index(drop=True)
    base['posição'] = base.index + 1

    return base


# Requisitando os dados
ano = 2021
residuos_solidos, pop_residente = ler_dados(ano)

# Aplicando ajustes
residuos_solidos = ajustes_rs(residuos_solidos, ano)
pop_residente = ajustes_pop(pop_residente)

# Mesclar os dados
dados_mesclados = mesclagem(pop_residente, residuos_solidos)

# Realizar os cálculos
dados_finais = calc(dados_mesclados, pop_residente)

# Salvar os dados mesclados em um arquivo CSV
dados_mesclados.to_csv(f'mesclagem_{ano}.csv', index=False)
dados_finais.to_csv(f'dados_finais_{ano}.csv', index=False)

import matplotlib.pyplot as plt

# Contagem de preenchimentos por UF
contagem_preenchimento_uf = dados_mesclados.groupby(['UF', 'Preenchimento']).size().unstack(fill_value=0)

# Ordenar o DataFrame pela posição
contagem_preenchimento_uf = contagem_preenchimento_uf.reindex(dados_finais.sort_values('posição')['UF'])

# Plotagem do gráfico de barras
plt.figure(figsize=(14, 8))  # Ajuste o tamanho da figura conforme necessário
largura_barra = 0.4  # Defina a largura das barras

# Definindo a posição das barras no eixo x
posicoes = np.arange(len(contagem_preenchimento_uf.index))

# Plotagem das barras para dados preenchidos
plt.bar(posicoes - largura_barra / 2, contagem_preenchimento_uf['Preencheu'], width=largura_barra, color='green',
        label='Preenchido')

# Plotagem das barras para dados não preenchidos
plt.bar(posicoes + largura_barra / 2, contagem_preenchimento_uf['Não preencheu'], width=largura_barra, color='red',
        label='Não Preenchido')

# Adicionando o número da posição no eixo y
for i, v in enumerate(contagem_preenchimento_uf['Preencheu']):
    plt.text(i - largura_barra / 2, v + 0.7, f'{v}', color='green', ha='center')

for i, v in enumerate(contagem_preenchimento_uf['Não preencheu']):
    plt.text(i + largura_barra / 2, v + 0.7, f'{v}', color='red', ha='center')

plt.title(f'Preenchimento dos dados sobre resíduos sólidos em {ano}')

plt.xlabel('UF')
plt.ylabel('Quantidade de Municípios')
plt.xticks(posicoes, contagem_preenchimento_uf.index)  # Definindo os rótulos do eixo x
plt.legend(title='Preenchimento')
plt.tight_layout(pad=3)  # Ajusta o layout para evitar sobreposições
plt.show()

