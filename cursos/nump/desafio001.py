#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import random
import numpy as np

# Arrays unidimensionais com numpy
ls_uni = [0, 1, 1, 2, 3, 4]
array_uni = np.array(ls_uni)

# Arrays bidimensionais com numpy
ls_bi = [[4, 5, 7], [4, 7, 8], [4, 8, 8]]
array_bi = np.array(ls_bi)

ls_tri = [[[4, 5, 8], [7, 8, 9], [78, 7, 8]], [[4, 5, 8], [7, 8, 9], [78, 7, 8]]]
array_tri = np.array(ls_tri)

def exemplos(array, tipo):
    print('-=' * 30)
    print(f'Array {tipo}:\n{array}')
    print(f'Dimensões do array {tipo}: {array.ndim}')
    print(f'Quantidade de linhas e colunas do array {tipo}: {array.shape}')
    print(f'Tamanho do array {tipo}: {len(array)}')

exemplos(array_bi, 'bidimensional')
exemplos(array_uni, 'unidimensional')
exemplos(array_tri, 'tridimensional')

# Funções na criação de um array

# Função semelhante ao range
c = np.arange(start=0, stop=9, step=0.1, dtype=float)  # Vai criar uma lista de 0 até 99
print(c)

# É colocado na lista o número de início até o final em até 4 passos
# Se o endpoint for false, ele não vai incluir o último número
d = np.linspace(start=0, stop=5, num=4, endpoint=False)
print(d)

# Criando arrays comuns

# Array apenas com o número 1 com o tamanho 10
e = np.ones(10, dtype=int)
print(e)

# Array apenas com o número 0 (usando o shape bidimensional)
f = np.zeros((5, 5))
print(f)

# Preenchendo um array bidimensional com números random
g = np.random.rand(3, 3)
print(g)

# Mexendo com diagonais

# Criação de array dimensional bidimensional de acordo com o tam de N
# Além de ter suas diagonais preenchidas com 1
h = np.eye(N=3)
print(h)


print('Exercícios')

print('Questão 1')
one = np.zeros((5, 5), dtype=int)
print(one)

print('Questão 2')
two = np.ones((3, 3), dtype=int)
print(two)

print('Questão 3')
three = np.random.randint(0, 21, size=(2, 3))
print(three)

print('Questão 4')
four = np.arange(start=9, stop=0, step=-1)
print(four)
