valores = [[], []]

for i in range(0, 7):
    valor = int(input('Type a value: '))

    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)

valores[0].sort()
valores[1].sort()

print(f'Pares: {valores[0]}')
print(f'Impares: {valores[1]}')
