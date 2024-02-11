#!/usr/bin/python
# -*- coding: latin-1 -*-

import numpy as np


def notas(nota, sit=False):
    """
    -> Fun��o para analisar notas e situa��es de v�rios alunos.
    :param nota: uma ou mias notas dos alunos (aceita v�rias)
    :param sit: valor opcional, indicando se deve ou n�o adicionar a situa��o
    :return: dicion�rio com v�rias informa��es sobre a situa��o da turma
    """
    turma = {
        'Quantidade': np.size(nota),
        'Maior': np.max(nota),
        'Menor': np.min(nota),
        'M�dia': np.mean(nota)
    }

    if sit:
        turma['Situa��o'] = 'Boa' if np.mean(nota) >= 7 else 'Ruim'

    return turma


res = notas(np.array([3.5, 2, 6.5, 2, 7, 4]))

print(res)

help(notas)
