from random import randint
from time import sleep

mega_sena = []

jogo = []

print(f'{"":->30} ')
print(f'{"":^5} JOGO NA MEGA SENA')
print(f'{"":->30} ')

qtd_jogos = int(input('Quantos jogos serão: '))

for i in range(0, qtd_jogos):

    for j in range(0, 6):
        palpite = randint(1, 60)

        if j == 0:
            jogo.append(palpite)
        else:
            while palpite in jogo:
                palpite = randint(1, 60)

            jogo.append(palpite)

    jogo.sort()
    mega_sena.append(jogo[:])

    jogo.clear()

print(f'-=-=-= SORTEANDO {qtd_jogos} JOGOS -=-=-=')

for i, j in enumerate(mega_sena, start=1):
    print(f'Jogo {i}: {j}')
    sleep(1)
