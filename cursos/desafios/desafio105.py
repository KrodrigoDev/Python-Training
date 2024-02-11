#!/usr/bin/python
# -*- coding: latin-1 -*-

def ajuda():
    while True:
        funcao = input('Função ou Biblioteca >')
        if funcao not in 'fim':
            saudacao = ' SISTEMA DE AJUDA PyHELP '
            print('~' * len(saudacao))
            print(saudacao)
            print('~' * len(saudacao))

            help(funcao)
        else:
            adeus = ' ATÉ LOGO! '
            print('~' * len(adeus))
            print(adeus)
            print('~' * len(adeus))

            break


ajuda()
