#!/usr/bin/python
# -*- coding: latin-1 -*-

def lerint(palavra):
    number = input(palavra)
    while not number.isnumeric():
        print('Erro! Digite um n�mero inteiro: ')
        number = input(palavra)
    return number


n = lerint('Digite um n�mero: ')
print(f'Vc acabou de digitar o valor {n}')
