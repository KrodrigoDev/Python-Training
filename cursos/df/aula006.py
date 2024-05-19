import pandas as pd
import numpy as np

# anos = np.random.randint(1800, 2026, 500)
#
# df_anos = pd.DataFrame({
#     'Ano': anos
# })
#
# bins = [1800, 1850, 1900, 1950, 2000, np.inf]
# labels = ['< 1850', '> 1850 < 1900', '> 1900 < 1950', ' > 1950 < 2000', '> 2000']
#
# faixas = pd.cut(df_anos['Ano'], bins=bins, labels=labels)
#
# df_anos['faixa'] = faixas
# df_anos['nome'] = 'caju'
# df_anos.to_csv('teste.csv', index=False)

import numpy as np
import pandas as pd

dados = np.arange(0, 1000, step=0.5)
percentis = [5, 15, 50, 85, 95]

resultados = np.percentile(dados, percentis).round(decimals=1)
labels = [f'< {resultados[0]}', f'> {resultados[0]} < {resultados[1]}', f'> {resultados[1]} < {resultados[2]}',
          f'> {resultados[2]} < {resultados[3]}',
          f'> {resultados[3]}']

df = pd.DataFrame({'valores': dados})
faixa = pd.cut(df['valores'], bins=[-np.inf,resultados[0], resultados[1], resultados[2], resultados[3], np.inf], labels=labels)
df['faixa'] = faixa

print(df)
