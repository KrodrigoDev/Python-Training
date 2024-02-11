#!/usr/bin/python
# -*- coding: latin-1 -*-

import utilidades.numeros.moeda as moeda
import utilidades.dados.leitor as leitor

p = leitor.leiaDinheiro('Digite o pre�o: R$')

print(f'A m�tade de {moeda.moeda(p)} � {moeda.metade(p, False)}')
print(f'O dobro de {moeda.moeda(p)} � {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')


moeda.resumo(p, 35, 22)
