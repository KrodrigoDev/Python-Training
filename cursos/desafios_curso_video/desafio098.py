from random import randint
from time import sleep


def sorteio(tamanho_lista):
    ls = []
    print('Sorteando os valores da lista: ', end='')

    for i in range(0, tamanho_lista):
        ls.append(randint(0, 100))
        print(ls[i], end=' ', flush=True)
        sleep(0.3)
    print('PRONTO !')

    return ls


def soma_par(lista):
    total_pares = 0
    print(f'Somando os valores pares de {lista}, temos ', end='')
    for i in lista:
        if i % 2 == 0:
            total_pares += i
    print(total_pares)


soma_par(sorteio(5))
