matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

soma_pares = soma_terceira_coluna = maior_valor_segunda = 0

for i in range(0, len(matriz)):
    for j in range(0, len(matriz)):
        valor = int(input(f'Digite um valor para [{i}, {j}] :'))
        matriz[i][j] = valor

print('-=' * 30)

for i in range(0, len(matriz)):
    for j in range(0, len(matriz)):

        print(f'[{matriz[i][j]:^5}]', end='')

        if matriz[i][j] % 2 == 0:
            soma_pares += matriz[i][j]

        if j == len(matriz) - 1:
            soma_terceira_coluna += matriz[i][j]

        if i == 1:
            if matriz[i][j] > maior_valor_segunda:
                maior_valor_segunda = matriz[i][j]

    print()

print('-=' * 30)

print(f'Soma de todos os valores pares: {soma_pares}')
print(f'Soma dos valores da terceira coluna: {soma_terceira_coluna}')
print(f'Maior valor da segunda linha: {maior_valor_segunda}')
