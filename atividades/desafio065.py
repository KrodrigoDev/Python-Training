# o limite vai ser de mil reais
tot_limite = tot_gasto = menor_valor = 0
produto_menor_valor = ''

while True:
    print('---' * 10)
    print('LOJA SUPER BARATÃO')
    print('---' * 10)

    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))

    if tot_gasto == 0 or preco < menor_valor:
        menor_valor = preco
        produto_menor_valor = nome

    if preco > 1000:
        tot_limite += 1

    tot_gasto += preco

    while True:
        opcao = str(input('Quer continuar? [S/N] ')).split()[0]
        if opcao in 'Ss' or opcao in 'Nn':
            break

    if opcao in 'Nn':
        break

print(f'{"---" * 5} FIM DO PROGRAMA {"---" * 5}')

print(f'A soma total dos preços foi de {tot_gasto:.2f}')
print(f'Temos {tot_limite} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {produto_menor_valor} que custa R${menor_valor:.2f}')
