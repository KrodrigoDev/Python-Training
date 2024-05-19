import numpy as np


def pegar_info(texto, tipo):
    while True:
        try:
            entrada = tipo(input(texto))
        except ValueError:
            print('O valor passado não condiz com o contéudo do tipo. Tente novamente.')
        except KeyboardInterrupt:
            print('O programa foi encerrado pelo usuário')
            break
        else:
            if tipo == str:
                entrada = entrada.lower().strip()

            return entrada


def converter(valor, unidade, unidade_convertida):
    unidades_medidas = ('km', 'hm', 'dam', 'm', 'dm', 'cm', 'mm')

    if (unidade in unidades_medidas) and (unidade_convertida in unidades_medidas):

        index_inicial = unidades_medidas.index(unidade)
        index_convertido = unidades_medidas.index(unidade_convertida)

        diferenca = index_convertido - index_inicial
        print(diferenca)
        if diferenca < 0:
            for _ in range(abs(diferenca)):
                print(valor)
                valor /= 10
        elif diferenca > 0:
            for _ in range(diferenca):
                print(valor)
                valor *= 10

        return valor


medida_informada = pegar_info('Digite a unidade de medida: ', str)
valor_inicial = pegar_info('Agora digite o valor da unidade: ', float)
medida_conversao = pegar_info('Deseja converter para qual unidade?  ', str)

print(converter(valor=valor_inicial, unidade=medida_informada, unidade_convertida=medida_conversao))
