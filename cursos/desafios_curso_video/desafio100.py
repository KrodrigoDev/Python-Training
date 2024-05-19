#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import datetime as dt

import numpy as np


def voto(ano_nasicmento):
    idade = dt.date.today().year - ano_nasicmento

    res = list()
    res.append(f'com {idade} anos seu voto é: ')

    if 18 <= idade < 25:
        res.append('OBRIGÁTORIO')
    elif idade < 18:
        res.append('NEGADO')
    else:
        res.append('OPCIONAL')

    return res


print('-' * 20)
votacao = voto(int(input('Em que ano você nasceu: ')))
print(votacao)
