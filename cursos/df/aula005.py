import pandas as pd

df = pd.read_csv('../arquivos/nba_draft_2015.csv')

# realizando filtragem através dos indíces
print(df.iloc[0:10, 1:5])
