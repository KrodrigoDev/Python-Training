import pandas as pd

data = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [10, 20, 30],
    'C': [100, 200, 300],
}, index=['l1', 'l2', 'l3'])


def somatorio_linha(linha):
    return linha.sum()


# criação de uma nova coluna
data['SOMA'] = data.apply(somatorio_linha, axis=1)

print(data)

# criação de uma nova linha

data.loc['l4'] = data.apply(somatorio_linha, axis=0)

print(data)
