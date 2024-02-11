from bases import data_frame_curso, data_frame_avaliacao, pd

# Exibindo primeiras, últimas e até linhas aleatórias do dataFrame

# print(dataFrame.head())
# print(dataFrame.tail())
# print(dataFrame.sample(n=10))
# print(dataFrame.loc[0]) # pegando por meio do indice
print(data_frame_avaliacao.loc['Playstation4':, ['ruim']])

# (dataFrame['ESTADO'])  # pegando uma coluna inteira
# print(f'Testando uma coisas: {dataFrame.iloc[0]}') # mesma coisa do loc[0]

# Exibindo informações sobre o dataFrame

# print(dataFrame.info())
# print(dataFrame.dtypes)
# print(type(dataFrame))
# print(f'O dataFrame possui o total de {dataFrame.shape[0]} linhas e {dataFrame.shape[1]} colunas')
# print(dataFrame.columns)

# Criando DataFrame

# alunos_dataFrame = pd.DataFrame({
#    'nome': ['Luke Skywalker', 'Yoda', 'Palpatine'],
#   'idade': [20, 108, 125],
#  'peso': [70.58, 35.20, 60.00],
# 'eh jedi': [True, True, False]  # nome das colunas podem ter espaço
# })

# Renomeando colunas do dataFrame (Isso vai gerar uma cópia)
# Para realizar a alteração no próprio dataFrame basta passar o paramêtro inplace= True

# alunos_dataFrame_copia = alunos_dataFrame.rename(
#   columns={'nome': 'Nome completo', 'idade': 'Idade'}
# )
