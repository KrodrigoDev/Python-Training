#!/usr/bin/python
# -*- coding: latin-1 -*-

import utilidades.numeros.moeda as moeda
import utilidades.dados.leitor as leitor

p = leitor.leiaDinheiro('Digite o preço: R$')

print(f'A métade de {moeda.moeda(p)} é {moeda.metade(p, False)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')


moeda.resumo(p, 35, 22)
