from bases import data_frame_curso, pd

# Remover coluna não nomeada
del data_frame_curso["Unnamed: 0"]

# Explorar Dados ÓLEO DIESEL
# print(data_frame_curso['PRODUTO'].unique())

# Explorar Dados PERNAMBUCO
# print(data_frame_curso['ESTADO'].unique())

# Filtros por Estado e Produto
# est_prb = data_frame_curso.query('ESTADO == "PERNAMBUCO"')
# prb_diesel = est_prb.query('PRODUTO == "ÓLEO DIESEL"')
# prb_diesel_ano_0510 = prb_diesel.query('2005 <= ANO <= 2010')
#
# print(f'Tamanho DataFrame original: {data_frame_curso.shape[0]}')
# print(f'Tamanho da primeira busca: {est_prb.shape[0]}')
# print(f'Tamanho da segunda busca: {prb_diesel.shape[0]}')
# print(f'Tamanho da terceira busca: {prb_diesel_ano_0510.shape[0]}')

# Iteração sobre as primeiras 100 linhas
# for index, linha in data_frame_curso.head(100).iterrows():
#     print(f'Index: {index}º Estado: {linha["ESTADO"]}')

# Limpeza de Dados
# copia = data_frame_curso.copy()

# Conversão de datas
# copia['DATA INICIAL'] = pd.to_datetime(copia['DATA INICIAL'])
# copia['DATA FINAL'] = pd.to_datetime(copia['DATA FINAL'])

# Conversão de colunas numéricas
# colunas_sujas = ['MARGEM MÉDIA REVENDA', 'PREÇO MÉDIO DISTRIBUIÇÃO', 'DESVIO PADRÃO DISTRIBUIÇÃO',
#                  'PREÇO MÍNIMO DISTRIBUIÇÃO', 'PREÇO MÁXIMO DISTRIBUIÇÃO', 'COEF DE VARIAÇÃO DISTRIBUIÇÃO']
#
# for coluna in colunas_sujas:
#     copia[f'{coluna}'] = pd.to_numeric(copia[f'{coluna}'], errors='coerce')

# Preenchimento de valores nulos
# copia.fillna(0, inplace=True)

# print(copia.info())

# Remover linhas com valores nulos
# copia.dropna(inplace=True)

# print(copia.info())

# Exploração estatística do DataFrame
# print(copia.describe())

# Leitura de CSV
data = pd.read_csv('./49705000_por_semestre.csv')

# Filtros por Ano
# filtro = data.query('2015 <= Ano < 2023')
# print(filtro.describe())

# Contagem de valores únicos em 'Ano'
# print(data['Ano'].value_counts().unique())

# Outros exemplos
# data['PREÇO MÉDIO DISTRIBUIÇÃO'] = pd.to_numeric(data['PREÇO MÉDIO DISTRIBUIÇÃO'], errors='coerce')
# data.dropna(inplace=True)
# print(data.info())

# Exploração de valores por Estado
# print(data['ESTADO'].value_counts())
# print(f'Valor máximo: {data['ESTADO'].value_counts().max()}')

# Transformação de uma série em DataFrame
# serie = data['ESTADO'].value_counts()
# print(type(serie))
#
# teste = serie.to_frame()
# teste.rename(columns={'count': 'FREQUÊNCIA'}, inplace=True)
#
# print(teste)

# Agrupamento por Ano e Semestre
# serie = data.groupby(['Ano', 'Semestre'])['Vazão (m³/s)'].sum()
#
# print(serie)


# Percorrendo o data frame de maneira eficiente

df = pd.DataFrame({
    'A': [1, 10, 100],
    'B': [2, 20, 200],
    'C': [3, 30, 300]
}, index=['linha 1', 'linha 2', 'linha 3'])


def somatorio_linha(linha):
    return linha.sum()


# criação de coluna com a soma das linhas
# df['SOMA(A B C)'] = df.apply(somatorio_linha, axis=1)

# criando uma nova linha com os valores das colunas
# df.loc['linha 4'] = df.apply(somatorio_linha, axis=0)

# print(df)

df['Media (A, B, C)'] = df.loc[['linha 1', 'linha 2', 'linha 3']].apply(lambda series: series.mean(), axis=1)

df['A * 2'] = df['A'].apply(lambda i : i * 2)

print(df['A * 2'])