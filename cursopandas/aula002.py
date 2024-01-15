from bases import data_frame_curso, data_frame_ana, pd

# print(data_frame_curso.columns)

data_frame_curso.drop(columns='Unnamed: 0', inplace=True)

# data_frame_curso.to_csv('Arquivo_curso.csv', index=False)

# print(data_frame_curso['ESTADO'].unique())

# print(data_frame_curso[(data_frame_curso['PREÇO MÉDIO REVENDA'] >= 10) & (data_frame_curso['ESTADO'] == 'ALAGOAS')])

# print(data_frame_curso['ANO'].value_counts())

# selecao = data_frame_curso['ESTADO'] == 'ALAGOAS'

# print(data_frame_curso.loc[selecao, ['ANO', 'ESTADO']].value_counts())

# postos_alagoas = data_frame_curso.query('(ESTADO == "ALAGOAS") & (ANO >= 2010)').reset_index(drop=True)
# print(postos_alagoas.reset_index(drop=True, inplace=True))
# print(postos_alagoas)

# postos_rio_janeiro = (data_frame_curso.query('(ESTADO == "RIO DE JANEIRO") and (`PREÇO MÉDIO REVENDA` > 2)')
# .reset_index(drop=True))

# print(postos_rio_janeiro.head())

# selecao_por_estado = data_frame_curso[data_frame_curso['ESTADO'] == 'ALAGOAS']
# selecao_estado_por_preco = selecao_por_estado[selecao_por_estado['PREÇO MÉDIO REVENDA'] > 2.0].reset_index(drop=True)

# selecao_por_estado = data_frame_curso.query('ESTADO == "ALAGOAS"')
# preco_minimo_estado = selecao_por_estado.query('`PREÇO MÉDIO REVENDA` > 2.0')

# selecao_estado = data_frame_curso.query('ESTADO == "RIO DE JANEIRO" or ESTADO == "SAO PAULO"')
# print(f'linhas selecionadas dentro do estado {selecao_estado.shape[0]}')

# selecao_produto = selecao_estado.query('PRODUTO == "GASOLINA COMUM"')
# print(f'linhas selecionadas dentro do produto {selecao_produto.shape[0]}')

# selecao_preco = selecao_produto.query('`PREÇO MÉDIO REVENDA` > 2.0')
# print(f'linhas selecionadas dentro do preço {selecao_preco.shape[0]}')

# selecao_1 = ((data_frame_curso['ESTADO'] == "ALAGOAS") |
#              (data_frame_curso['ESTADO'] == "SAO PAULO") |
#              (data_frame_curso['ESTADO'] == "RIO DE JANEIRO"))
#
# selecao_al_rj_sp = data_frame_curso[selecao_1]
# print(selecao_al_rj_sp.shape[0])
#
# selecao_2 = selecao_al_rj_sp['PRODUTO'] == "GASOLINA COMUM"
#
# gasolina_comum = selecao_al_rj_sp[selecao_2]
# print(selecao_al_rj_sp.shape[0])
#
# selecao_3 = gasolina_comum['PREÇO MÉDIO REVENDA'] >= 2.0
#
# preco_min_al_rj_sp = gasolina_comum[selecao_3].reset_index(drop=True)
#
# preco_min_al_rj_sp[['ESTADO', 'PREÇO MÉDIO REVENDA', 'PRODUTO']].to_csv('teste.csv', index=False)

# estado_selecionado = data_frame_curso.query('ESTADO == "ALAGOAS" | ESTADO == "SAO PAULO" | ESTADO == "RIO DE JANEIRO"')
#
# produto_selecionado = estado_selecionado.query('PRODUTO == "ETANOL HIDRATADO"')
#
# valor_minimo = produto_selecionado.query('`PREÇO MÉDIO REVENDA` >= 3')
#
# ano_selecionado = valor_minimo.query(' 2015 < ANO < 2018').reset_index(drop=True)
#
# print(ano_selecionado)

# selecao_ano = data_frame_curso.query('ANO == 2008 | ANO == 2010 | ANO == 2012')

# ano = data_frame_curso['PRODUTO'].isin(["ETANOL HIDRATADO"])

# print(data_frame_curso[ano]['PRODUTO'])

lista_anos = [2008, 2010, 2012]

selecao_ano = data_frame_curso.query(f'ANO in {lista_anos}')

print(selecao_ano['ANO'].unique())
