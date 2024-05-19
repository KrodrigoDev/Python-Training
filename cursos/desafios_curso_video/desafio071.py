listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
            'Estojo', 25.00, 'Trasnferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'canetas', 22.30, 'Livro', 34.90)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for i in range(0, len(listagem), 2):
    for j in range(i + 1, len(listagem)):
        print(f'{listagem[i]:.<30}R${listagem[j]}')
        break
