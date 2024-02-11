#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import numpy as np

# Criando um array de 10 elementos, todos com valor 1
a1 = np.ones(10, dtype=int)

# Multiplicando todos os elementos de a1 por 10 e depois dividindo por 2
a1 = (a1 * 10) // 2

# Gerando um array de 10 números inteiros aleatórios entre 0 e 20
a2 = np.random.randint(0, 20, size=(10))

# Somando os arrays a1 e a2 elemento por elemento
a3 = a1 + a2

# Gerando duas matrizes aleatórias de dimensões diferentes
m1 = np.random.randint(1, 10, size=(2, 3))
m2 = np.random.randint(1, 10, size=(3, 2))

# Exibindo as matrizes m1 e m2
print(m1)
print('-=' * 5)
print(m2)
print('-=' * 5)

# Multiplicando as matrizes m1 e m2
print(m1.dot(m2))

# Coparação de arrays
b2 = np.array([[2, 5, 3, 5], [1, 5, 2, 5]])
b3 = np.array([[1, 5, 2, 5], [2, 5, 3, 5]])
b4 = np.array([[1, 5, 2, 5], [2, 5, 3, 5]])

# faz uma comparação de elemento por elemento O(n)
comp1 = b2 == b3  # retorna um array de booleano

# realiza uma comparação do contéudo inteiro
comp2 = np.array_equal(b4, b3)

