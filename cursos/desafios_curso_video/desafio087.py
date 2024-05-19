from random import randint
from time import sleep
from operator import itemgetter

# jogo = dict()
# rodadas = list()
#
# ranking = list()
#
# for i in range(0, 4):
#     jogo[f'jogador{i}'] = randint(1, 6)
#     rodadas.append(jogo.copy())
#     jogo.clear()
#
# print('Valores sorteados:')
# for rodada in rodadas:
#     for chave, valor in rodada.items():
#         sleep(1)
#         ranking.append(valor)
#         print(f'O {chave} tirou {valor}')
#
# print('-=' * 30)
# print('== Ranking dos jogadores BubbleSort == ')
# for i in range(0, len(rodadas) - 1):
#     aux = ranking[i]
#     for j in (i + 1, len(rodadas) - 1):
#         if aux < ranking[j]:
#             ranking[i] = ranking[j]
#             ranking[j] = aux
#
# for i, j in enumerate(ranking, start=1):
#     print(f'{i}º lugar: {j}')

jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}

for i, j in jogo.items():
    print(f'{i} tirou {j}')

print('-=' * 30)
print('== Ranking dos jogadores método sorted == ')

ranking_metodo = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for i, j in enumerate(ranking_metodo):
    print(f'{j[0]}º lugar: {j[1]}')
