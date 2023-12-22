import pandas as pd

# Supondo que 'Data' e 'Media' são nomes das colunas
dataFrameAna = pd.read_csv('../arquivos/vazoes_C_49705000.csv')

# Convertendo 'Data' para o tipo datetime
dataFrameAna['Data'] = pd.to_datetime(dataFrameAna['Data'], format='%d/%m/%Y')

# Criando uma nova coluna para armazenar o ano
dataFrameAna['Ano'] = dataFrameAna['Data'].dt.year

# Calculando a média para cada ano
media_por_ano = dataFrameAna.groupby('Ano')['Media'].mean().reset_index()

# Salvar a coluna 'Ano' e 'Media' em um novo arquivo CSV
media_por_ano.to_csv('media_por_ano.csv', index=False)

print(media_por_ano)
