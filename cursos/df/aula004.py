import pandas as pd

classe = pd.DataFrame({
    'student': ['Kauã', 'Léo', 'Duda', 'Peu'],
    'age': [20, 15, 18, 17],
    'av1': [5.4, 6.0, 7.8, 10],
    'av2': [8, 9.5, 7.45, 6.0]
})


media_colunas = classe[['av1', 'av2']].apply(lambda coluna: coluna.mean(), axis=1)

print(media_colunas)
