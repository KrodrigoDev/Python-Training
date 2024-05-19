#!/usr/bin/python
# -*- coding: iso-8859-15 -*-



def time_to_minute(time):
    time = time.split(sep=':')

    minutos = (int(time[0]) * 60)
    if len(time) == 2:
        minutos += int(time[1])

    print(minutos)
    return minutos


ponto = {
    'carga': time_to_minute(input('Digite sua carga horária: ')),
    'entrada': time_to_minute(input('Digite o horário de entrada1: ')),
    'almoço': time_to_minute(input('Digite o horário de saída para o almoço: ')),
    'volta': time_to_minute(input('Digite o horário de volta após o almoço: '))
    # qual será o horário de saída? carga de trabalho = 8h
}


def calcular_tempo(carga=ponto['carga'], entrada=ponto['entrada'], almoco=ponto['almoço'], volta=ponto['volta']):
    '''
    Aqui está uma analogia: imagine que a é a quantidade total de dinheiro que você tem em sua carteira,
     e b é quanto você realmente gastou.
     Então, a - b seria quanto dinheiro você tem deixado, ou seja, o dinheiro não utilizado.
    :param carga:
    :param entrada:
    :param almoco:
    :param volta:
    :return:
    '''
    hora = ((carga + volta) - (almoco - entrada)) // 60
    minuto = ((carga + volta) - (almoco - entrada)) - time_to_minute(str(hora))

    return f'{hora}:{minuto}'


ponto['saída'] = calcular_tempo()

print(calcular_tempo())
