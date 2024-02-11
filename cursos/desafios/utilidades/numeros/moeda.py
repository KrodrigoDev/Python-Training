def aumentar(valor, porcento, formato=False):
    valor = valor + ((valor * porcento) / 100)
    if formato:
        valor = moeda(valor)

    return valor


def diminuir(valor, porcento, formato=False):
    valor = valor - ((valor * porcento) / 100)

    if formato:
        valor = moeda(valor)

    return valor


def dobro(valor, formato=False):
    valor = valor * 2
    if formato:
        valor = moeda(valor)

    return valor


def metade(valor, formato=False):
    valor = valor / 2

    if formato:
        valor = moeda(valor)

    return valor


def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')


def resumo(valor, aumento, reducao):
    print('-' * 25)
    print(f'{"RESUMO DO VALOR":^25}')
    print('-' * 25)

    print(f'Preço analisado: {moeda(valor):<10}')
    print(f'Drobro do preço: {dobro(valor, True):<10}')
    print(f'Métade do preço: {metade(valor, True):<10}')
    print(f'{aumento}% de aumento: {aumentar(valor, aumento, True):<10}')
    print(f'{reducao}% de redução: {diminuir(valor, reducao, True):<10}')
