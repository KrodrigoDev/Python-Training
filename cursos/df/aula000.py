import pandas as pd
from unidecode import unidecode

df = pd.read_csv('../arquivos/municipios.csv')


a = df['nome'].apply(unidecode)
b = a.to_list()
for i, j in enumerate(a):
    print(j.upper())

    if i == 5:
        break
