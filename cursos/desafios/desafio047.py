# método 1 e implementado por mim
# lista = []
#
# for i in range(len(algo) - 1, -1, -1):
#     lista.append(algo[i])
#
# algo_invertido = ''.join(lista)
#
# print(f'O inverso de {algo} é {algo_invertido}')
#
# if algo_invertido == algo:
#     print('A frase digitada é um polidromo')
# else:
#     print('A frase digitada não é um polidromo')

# método 2 visto com o professor

algo = str(input('Digite uma frase ou uma palvra: '))

lista_algo = algo.split(sep=' ')

junto = ''.join(lista_algo)
inverso = ''

for i in range(len(junto) - 1, -1, -1):
    inverso += junto[i]
    print(inverso)

print(f'A frase {junto} ao contrário é {inverso} ')

if junto == inverso:
    print('A frase digitada é um polidromo')
else:
    print('A frase digitada não é um polidromo')

# lista de palavras para testar
# APOS A SOPA,
# A SACADA DA CASA,
# A TORRE DA DERROTA,
# O LOBO AMA O BOLO,
# ANOTARAM A DATA DA MARATONA.
