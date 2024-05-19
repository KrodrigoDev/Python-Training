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
    'carga': time_to_minute(input('Digite sua carga hor�ria: ')),
    'entrada': time_to_minute(input('Digite o hor�rio de entrada1: ')),
    'almo�o': time_to_minute(input('Digite o hor�rio de sa�da para o almo�o: ')),
    'volta': time_to_minute(input('Digite o hor�rio de volta ap�s o almo�o: '))
    # qual ser� o hor�rio de sa�da? carga de trabalho = 8h
}


def calcular_tempo(carga=ponto['carga'], entrada=ponto['entrada'], almoco=ponto['almo�o'], volta=ponto['volta']):
    '''
    Aqui est� uma analogia: imagine que a � a quantidade total de dinheiro que voc� tem em sua carteira,
     e b � quanto voc� realmente gastou.
     Ent�o, a - b seria quanto dinheiro voc� tem deixado, ou seja, o dinheiro n�o utilizado.
    :param carga:
    :param entrada:
    :param almoco:
    :param volta:
    :return:
    '''
    hora = ((carga + volta) - (almoco - entrada)) // 60
    minuto = ((carga + volta) - (almoco - entrada)) - time_to_minute(str(hora))

    return f'{hora}:{minuto}'


ponto['sa�da'] = calcular_tempo()

print(calcular_tempo())
