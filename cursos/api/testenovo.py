import pandas as pd

# Tente ler o arquivo CSV com diferentes codificações
try:
    data = pd.read_csv('../cursoapi/famcad_uni_quant_renda_municipio.csv', sep=',', encoding='utf-8')
except UnicodeDecodeError:
    data = pd.read_csv('../cursoapi/famcad_uni_quant_renda_municipio.csv', sep=',', encoding='latin1')

# Aplique a formatação para a coluna 'valor'
data['valor'] = data['valor'].apply(lambda x: '{:,.0f}'.format(x)).str.replace(',', '.')

data.to_csv('famcad_uni_quant_renda_municipio1.csv', index=False)
