#!/usr/bin/python
# -*- coding: latin-1 -*-

def ajuda():
    while True:
        funcao = input('Fun��o ou Biblioteca >')
        if funcao not in 'fim':
            saudacao = ' SISTEMA DE AJUDA PyHELP '
            print('~' * len(saudacao))
            print(saudacao)
            print('~' * len(saudacao))

            help(funcao)
        else:
            adeus = ' AT� LOGO! '
            print('~' * len(adeus))
            print(adeus)
            print('~' * len(adeus))

            break


ajuda()
