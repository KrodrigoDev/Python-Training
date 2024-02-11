valores = []

while True:
    valor = int(input('typed a value between 0 and 10000: '))
    valores.append(valor)

    while True:
        continuar = str(input('Please,typed yes to continue or no to exit: ')).strip().upper()[0]
        if continuar in 'SN':
            break

    if continuar == 'N':
        break

print(f'Foram digitados um total de {len(valores)} ')

valores.sort(reverse=True)
print(f'Lista de valores em ordem descrecente {valores}')
print('O valor cinco está na lista' if 5 in valores else 'O valor 5 não está na lista')
