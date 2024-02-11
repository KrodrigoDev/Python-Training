import pandas as pd

# Carregando a base de dados (um pouco modificada)
data_frame_original = pd.read_csv('../arquivos/vazoes_C_49705000.csv')

# Limpando o campo de data e criando colunas relacionadas
data_frame_original['Data'] = pd.to_datetime(data_frame_original['Data'], format='%d/%m/%Y')

# Criando as colunas 'Ano' e 'Semestre'
data_frame_original['Ano'] = data_frame_original['Data'].dt.year
data_frame_original['Semestre'] = (data_frame_original['Data'].dt.month - 1) // 6 + 1

# Selecionando as colunas de vazão para calcular a média
colunas_vazao = [f'Vazao{i:02d}' for i in range(1, 32)]
data_frame_original['Vazão (m³/s)'] = data_frame_original[colunas_vazao].mean(axis=1)

# Calculando a média das vazões para cada semestre de cada ano
media_vazoes_por_semestre = data_frame_original.groupby(['Ano', 'Semestre']).mean()['Vazão (m³/s)'].reset_index()

# Adicionando a coluna 'Datas' ao DataFrame
media_vazoes_por_semestre['Datas'] = pd.to_datetime(
    media_vazoes_por_semestre['Ano'].astype(str) + '-' +
    ((media_vazoes_por_semestre['Semestre'] - 1) * 6 + 1).astype(str) + '-01'
)

# Criando a coluna 'Estação'
media_vazoes_por_semestre['Estação'] = data_frame_original['EstacaoCodigo']

# Criando as colunas 'Dia' e 'Mês'
media_vazoes_por_semestre['Dia'] = media_vazoes_por_semestre['Datas'].dt.day
media_vazoes_por_semestre['Mês'] = media_vazoes_por_semestre['Datas'].dt.month

# Adicionando as colunas 'Data Inicial' e 'Data Final' por semestre
media_vazoes_por_semestre['Data Inicial'] = media_vazoes_por_semestre['Datas']
media_vazoes_por_semestre['Data Final'] = media_vazoes_por_semestre['Datas'] + pd.DateOffset(months=6, days=-1)

# Arredondando a coluna 'Vazão (m³/s)' para duas casas decimais
media_vazoes_por_semestre['Vazão (m³/s)'] = media_vazoes_por_semestre['Vazão (m³/s)'].round(2)

# Reordenando as colunas conforme a especificação
colunas_esperadas = ['Estação', 'Ano', 'Semestre', 'Data Inicial', 'Data Final', 'Vazão (m³/s)']
media_vazoes_por_semestre = media_vazoes_por_semestre[colunas_esperadas]

# Salvando o novo DataFrame em um arquivo CSV
nome_arquivo = f'{media_vazoes_por_semestre.loc[0, "Estação"]}_por_semestre.csv'
media_vazoes_por_semestre.to_csv(nome_arquivo, index=False)
