import pandas as pd

notas = [2, 3, 4, 4, 4, 1, 3, 4, 5, 3, 3, 4, 4, 2, 3, 3, 4, 4, 5, 1]
notas.sort()


def valor_absoluto(conjunto):
    distribuicao = {}

    for i in conjunto:
        if i in distribuicao:
            distribuicao[i] += 1
        else:
            distribuicao[i] = 1
    return distribuicao


df = valor_absoluto(notas)

df = pd.DataFrame(list(df.items()), columns=['valor', 'abs'])


def abs_acumulada(df, coluna_valor, nova_coluna):
    valores = []
    for i in range(df.shape[0]):
        if i == 0:
            valor = df[coluna_valor].loc[i]
        else:
            valor = valores[i - 1] + df[coluna_valor].loc[i]
        valores.append(valor)
    df[nova_coluna] = valores
    return df


df = abs_acumulada(df, 'valor', 'abs_acu')


def valor_relativa(df, coluna_abs):
    soma_valores = sum(df[coluna_abs])

    df['rela'] = df[coluna_abs].apply(lambda i: (i / soma_valores) * 100)

    return df


df = valor_relativa(df, 'abs')

df = abs_acumulada(df, 'rela', 'rela_acu')


print(df)