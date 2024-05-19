#!/usr/bin/python
# -*- coding: latin-1 -*-

def fat_rec(number, show=False):
    """
    -> essa � uma fun��o que usa chamada recursiva para obter o fatorial
    :param number: o n�mero que vai ter o fatorial c�lculado
    :param show: (opcional) Mostrar ou n�o a conta
    :return: o retorno do fatorial
    """
    if show:
        simbolo = 'x' if number != 1 else '='
        print(number, end=f' {simbolo} ')

    if number == 1:
        return 1
    else:
        return number * fat_rec(number - 1, show)


r = fat_rec(5, False)


def fat(number, show=False):
    """
    -> Fatorial de um n�mero sem a forma recursiva (deselegante)
    :param number: n�mero a ter o fatorial
    :param show: mostrar ou n�o o c�lculo do fatorial
    :return:
    """
    c = 1
    for i in range(number, 0, -1):
        c *= i
        if show:
            simbolo = 'x' if number != 1 else '='
            print(number, end=f' {simbolo} ')
            number -= 1

    return c


print(fat(5, True))
