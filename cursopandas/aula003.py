import pandas as pd

# data frames
base = pd.read_csv('../arquivos/BASE.csv')
estacao = pd.read_csv('../arquivos/vazoes_C_49705000.csv')

# Remova espaços extras do nome da coluna 'Código' e configure como índice
base.set_index('Código', inplace=True)

# Realizando formatação na data
estacao['Data'] = pd.to_datetime(estacao['Data'], format='%d/%m/%Y')
estacao['ano'] = estacao['Data'].dt.year

# criação e atribuição das colunas de interesse
new_data = pd.DataFrame()

# Calculando a média com base no valor máximo de cada mês
media_vazoes_por_ano = estacao.groupby('ano')['Maxima'].mean().reset_index()

# Puxando as informações da estação atual
estacao_atual = base.loc[49705000]

# Adiciona as datas correspondentes à média
new_data['Ano'] = media_vazoes_por_ano['ano']
new_data['Média de Vazão Anual'] = round(media_vazoes_por_ano['Maxima'], 4)
new_data['Nome Estação'] = estacao_atual['Nome Estação']
new_data['Altitude (m)'] = estacao_atual['Altitude (m)']
new_data['Longitude'] = estacao_atual['Longitude']
new_data['Latitude'] = estacao_atual['Latitude']

# Ordena o DataFrame pelo ano em ordem decrescente
new_data.sort_values(by='Ano', ascending=False, inplace=True)

# Salvando o DataFrame em um arquivo CSV com nome personalizado
nome_arquivo = f'vazao_{estacao_atual["Nome Estação"].replace(" ", "_")}.csv'
new_data.to_csv(nome_arquivo, index=False)
