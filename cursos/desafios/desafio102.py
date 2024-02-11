#!/usr/bin/python
# -*- coding: latin-1 -*-

def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


name = input('Nome do jogador: ')
points = input('Números de gols: ')

if len(name) != 0 and len(points) != 0:
    ficha(name, int(points))
elif len(name) != 0 and len(points) == 0:
    ficha(name)
elif len(points) != 0 and len(name) == 0:
    ficha(gols=int(points))
else:
    ficha()
