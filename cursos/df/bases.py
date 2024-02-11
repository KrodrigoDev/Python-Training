import pandas as pd

# Carregando o dataSet que usa o separador ';'
data_frame_curso = pd.read_csv("../arquivos/GasPricesinBrazil_2004-2019.csv", sep=';')
data_frame_ana = pd.read_csv('../arquivos/BASE.csv')

data_frame_vazao = pd.read_csv('../arquivos/vazoes_C_49705000.csv')

data_frame_avaliacao = pd.DataFrame({
    'bom': [50, 81, 100],
    'ruim': [40, 37, 56],
    'péssimo': [27, 76, 29]
}, index=['XboxOne', 'Playstation4', 'Switch'])
