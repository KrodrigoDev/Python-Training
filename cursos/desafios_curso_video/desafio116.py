import pandas as pd
from math import sqrt

idh_municipios = [0.754, 0.812, 0.698, 0.825, 0.639,
                  0.742, 0.871, 0.703, 0.819, 0.788,
                  0.654, 0.735, 0.802, 0.817, 0.712,
                  0.827, 0.758, 0.681, 0.799, 0.732]

df = pd.DataFrame({'massa': idh_municipios})


def amplitude_dados(base, colunas):
    ampli_total = max(base[colunas]) - min(base[colunas])

    # Método prático
    tam_base = base.shape[0]
    qtd_classes = 5 if tam_base < 25 else 7  # int(sqrt(tam_base))

    # Calculando a amplitude
    calc = ampli_total / qtd_classes
    return [calc, int(qtd_classes)]


def intervalos(base, coluna, qtd_classes, amplitude, qtd_casas):
    valor_min = min(base[coluna])

    limites = []

    for i in range(0, qtd_classes):
        if i == 0:
            limites.append([valor_min, round(valor_min + amplitude, qtd_casas)])
        else:
            calc_intervalo = round((limites[-1][1] + amplitude), qtd_casas)
            limites.append([limites[-1][1], calc_intervalo])

    return limites


def classificacao(base, coluna):
    # Retorna uma lista com a amplitude dos intervalos e a quantidade de classes
    ampli = amplitude_dados(df, 'massa')

    print(f'Qtd de classes: {ampli[1]}')
    # Obtendo o limite dos intervalos entre os dados
    limites = intervalos(df, 'massa', ampli[1], ampli[0], 3)

    classes = []

    for valor in base[coluna]:
        classificado = False
        for j in range(len(limites)):
            inf = limites[j][0]
            sup = limites[j][1]

            if valor < inf:
                classes.append(f'Até {inf}')
                classificado = True
                break
            elif valor >= inf and valor <= sup:
                classes.append(f'De {inf} até {sup}')
                classificado = True
                break

        if not classificado:
            classes.append(f'Acima de {limites[-1][1]}')  # nunca vai cair aqui

    return classes


df['classificacao'] = classificacao(df, 'massa')
print(df)
