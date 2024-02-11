#!/usr/bin/python
# -*- coding: latin-1 -*-

import numpy as np


def notas(nota, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param nota: uma ou mias notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    turma = {
        'Quantidade': np.size(nota),
        'Maior': np.max(nota),
        'Menor': np.min(nota),
        'Média': np.mean(nota)
    }

    if sit:
        turma['Situação'] = 'Boa' if np.mean(nota) >= 7 else 'Ruim'

    return turma


res = notas(np.array([3.5, 2, 6.5, 2, 7, 4]))

print(res)

help(notas)
