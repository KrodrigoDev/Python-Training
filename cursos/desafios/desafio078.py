valores = []
pares = []
impares = []

while True:
    valor = int(input('Type the value: '))

    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

    valores.append(valor)

    continuar = str(input('type yes to continue or no to exit:')).strip()[0].upper()

    while not (continuar in 'SN'):
        continuar = str(input('Please, type yes or no: '))

    if continuar == 'N':
        break


print(f'Todos os valores digitados: {valores}')
print(f'Todos os valores pares: {pares}')
print(f'Todos os valores impares: {impares}')
