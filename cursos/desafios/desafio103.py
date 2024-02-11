#!/usr/bin/python
# -*- coding: latin-1 -*-

def lerint(palavra):
    number = input(palavra)
    while not number.isnumeric():
        print('Erro! Digite um número inteiro: ')
        number = input(palavra)
    return number


n = lerint('Digite um número: ')
print(f'Vc acabou de digitar o valor {n}')
