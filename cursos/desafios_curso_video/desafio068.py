# brasileirão de 2023
brasileirao = ('Palmeiras', 'Gremio', 'Atletico', 'Flamengo',
               'Botafogo', 'Red Bull', 'Fluminense Rj', 'CA Paranaense PR',
               'Internacional' 'Fortaleza', 'São Paulo', 'Cuiabá Esporte',
               'Corinthians SP', 'Cruzeiro', 'Vasco Gama', 'Bahia', 'Santos FC',
               'Goiás EC GO', 'Coritiba PR', 'América FC MG')

print('-=' * 20)
print(f'Os cinco primeiros colocados do brasileirão 2023 são: {brasileirao[0:5]}')
print('-=' * 20)
print(f'Os últimos colocados do brasileirão 2023 são: {brasileirao[-5:]}')
print('-=' * 20)
print(f'Lista em ordem alfabética: {sorted(brasileirao)}')

# na perguntar original era pra ser o chapecoense, mas ele não se encontrava entre os 20
print('-=' * 20)
print(f'Posição em que se encontra o São paulo: {brasileirao.index("São Paulo") + 1}')
