# In[0]: Importação das bibliotecas
import locale

import pandas as pd
from unidecode import unidecode

# In[1]: Definindo o modelo e planilha-chave
modelo = pd.read_excel(
    r'C:\Users\Kauã Rodrigo\Documents\Scripts-Python\Curso em vídeo\Idea\CursoEmVideo\cursoapi\social.xlsx')
chave = pd.read_excel(
    r'C:\Users\Kauã Rodrigo\Documents\Scripts-Python\Curso em vídeo\Idea\CursoEmVideo\cursoapi\planilha_chave.xlsx')

reg_mun = chave.dropna(subset='co_mun')[['co_reg_plan', 'no_reg_plan', 'co_mun', 'no_mun']].astype(
    {'co_reg_plan': 'int64', 'no_reg_plan': 'string', 'co_mun': 'int64', 'no_mun': 'string'})
reg_mun['co_mun2'] = reg_mun['co_mun'].astype('string').apply(lambda x: int(x[:6]))

reg_mun['aux'] = reg_mun['no_mun'].apply(lambda x: unidecode(x.upper()))
reg_mun['aux'] = reg_mun['aux'].replace({"'": ' '}, regex=True)
reg_mun = reg_mun.astype({'aux': 'string'})

ufs = chave[['co_uf', 'no_uf']].dropna().drop_duplicates().reset_index(drop=True)
reg_geo = chave[['co_reg_geo', 'no_reg_geo']].dropna().drop_duplicates().reset_index(drop=True)

rge_ufs = chave.dropna(subset='co_uf')[['co_reg_geo', 'no_reg_geo', 'co_uf', 'no_uf']].astype(
    {'co_reg_geo': 'int64', 'no_reg_geo': 'string', 'co_uf': 'int64', 'no_uf': 'string'}).drop_duplicates()

rge_ufs['aux'] = rge_ufs['no_uf'].apply(lambda x: unidecode(x.upper()))
rge_ufs = rge_ufs.astype({'aux': 'string'})

# In[2]: Agrupamento dos dados
variavel = 'Assistência Social'

# Caminho único do arquivo CSV
file_path = '../cursoapi/visdata3-download-28-01-2024 171608.csv'

# Lista para armazenar os DataFrames
lista = []

print("Caminho do arquivo CSV:")
print(file_path)

# Leitura do arquivo CSV
df = pd.read_csv(file_path, encoding='latin-1', sep=',')

print("\nDados originais:")
print(df)

if 'UF' in list(df.columns):
    del df['UF']

# Ajuste para dividir a coluna 'Referência' corretamente
df['mes'] = df['Referência'].str.split('/', expand=True)[0]
df['ano'] = df['Referência'].str.split('/', expand=True)[1]

# Remoção da coluna 'Referência'
del df['Referência']

print("\nDados após ajuste:")
print(df)

# Empilhamento do DataFrame
aux = df.set_index(['Código', 'Unidade Territorial', 'mes', 'ano']).stack().reset_index()

aux.columns = ['co', 'no', 'mes', 'ano', 'social_subcategoria', 'valor']

print("\nDataFrame após empilhamento:")
print(aux)

lista.append(aux)

dados = pd.concat(lista, ignore_index=True)

dados['social_subcategoria'] = dados['social_subcategoria'].str.split(r' \(', expand=True)[0]

dados = dados.replace({'Valor repassado às famílias PBF': 'Valor Total Repassado do Bolsa Família',
                       'Famílias PBF': 'Famílias beneficiárias',
                       'Valor do Benefício médio': 'Benefício médio recebido pelas famílias do Bolsa Família'})

dados = dados.replace({',': '.'}, regex=True).astype({'valor': 'float'})

# Correção para garantir que o 'mes' seja um número
dados['mes'] = dados['mes'].apply(lambda x: int(x) if x.isdigit() else 0)

# Se 'mes' for um intervalo, como '010203', use o primeiro mês
dados['mes'] = dados['mes'] % 100

corte = dados[
    dados['social_subcategoria'].isin(['Famílias beneficiárias', 'Pessoas beneficiárias'])].copy().sort_values(
    by=['ano', 'mes']).reset_index(drop=True)
corte = corte.drop_duplicates(subset=['co', 'no', 'social_subcategoria', 'ano'], keep='last')
corte = corte[['co', 'no', 'ano', 'social_subcategoria', 'valor', 'mes']]

soma = dados[
    ~dados['social_subcategoria'].isin(['Famílias beneficiárias', 'Pessoas beneficiárias'])].copy().sort_values(
    by=['ano', 'mes']).reset_index(drop=True)
soma = soma.groupby(by=['co', 'no', 'social_subcategoria', 'ano'], as_index=False).sum()

print("\nDados após corte:")
print(corte)

print("\nDados após soma:")
print(soma)

# Organizando as colunas
corte = corte[['co', 'no', 'ano', 'social_subcategoria', 'valor', 'mes']]
soma = soma[['co', 'no', 'ano', 'social_subcategoria', 'valor', 'mes']]

# Adicionando colunas ausentes no DataFrame final 'dados'
dados['co_mun'] = dados['co']  # 'co_uf' não está disponível no código fornecido, então usemos 'co' como substituto
dados['no_mun'] = dados['no']  # 'no_uf' não está disponível no código fornecido, então usemos 'no' como substituto
dados['variavel'] = 'Assistência Social'
dados['inf_categoria'] = 'Bolsa Família'
dados['inf_subcategoria'] = dados['social_subcategoria']

# Organizando as colunas no DataFrame final 'dados'
dados = dados[['co_uf', 'no_uf', 'ano', 'variavel', 'inf_categoria', 'inf_subcategoria', 'valor', 'mes']]

# Filtrar apenas os meses iguais a 12 (dezembro)
dados = dados[dados['mes'] == 12]

# Aplique a formatação para a coluna 'valor'
dados['valor'] = dados['valor'].apply(lambda x: '{:,.0f}'.format(x)).str.replace(',', '.')
del dados['mes']
# Resultado final
print("Resultado Final:")
print(dados)

# Criação do arquivo CSV após o tratamento dos dados
output_file_path = 'Dados_tratados_bolsa_familia.csv'
dados.to_csv(output_file_path, index=False)

print(f'O arquivo {output_file_path} foi criado com sucesso!')
