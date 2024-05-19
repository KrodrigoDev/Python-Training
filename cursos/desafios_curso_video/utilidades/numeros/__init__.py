def aumentar(valor, porcento, formato=False, localidade='R$'):
    valor = valor + (valor * porcento / 100)
    if formato:
        valor = moeda(valor, localidade)

    return valor


def diminuir(valor, porcento, formato=False, localidade='R$'):
    valor = valor - (valor * porcento / 100)

    if formato:
        valor = moeda(valor, localidade)

    return valor


def dobro(valor, formato=False, localidade='R$'):
    valor = valor * 2
    if formato:
        valor = moeda(valor, localidade)

    return valor


def metade(valor, formato=False, localidade='R$'):
    valor = valor / 2

    if formato:
        valor = moeda(valor, localidade)

    return valor


def moeda(valor, localidade='R$'):
    return f'{localidade}{valor:.2f}'.replace('.', ',')


def resumo(valor, aumento, reducao, localidade='R$'):

    """
    -> criado no dia 10 do mês 2 de 2024 - by: kauã rodrigo
    :param valor: valor que deve ser resumido
    :param aumento: aumento no valor de acordo com a porcentagem fornecida
    :param reducao: redução de acordo com a porcentagem fornecida
    :param localidade: formato da moeda
    :return:
    """
    print('-' * 25)
    print(f'{"RESUMO DO VALOR":^25}')
    print('-' * 25)

    print(f'Preço analisado: {moeda(valor, localidade):<10}')
    print(f'Drobro do preço: {dobro(valor, True, localidade):<10}')
    print(f'Métade do preço: {metade(valor, True, localidade):<10}')
    print(f'{aumento}% de aumento: {aumentar(valor, aumento, True, localidade):<10}')
    print(f'{reducao}% de redução: {diminuir(valor, reducao, True, localidade):<10}')
