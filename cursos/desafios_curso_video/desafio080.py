tabuleiro = [['', '', ''], ['', '', ''], ['', '', '']]

tot_vazio = 9

# True(X) e False(O)
jogador = True

while tot_vazio != 0:

    simbolo = "X" if jogador else "O"

    print('-=' * 20)
    print(f'{"VEZ DO JOGADOR":>25} {simbolo}')
    print('-=' * 20)

    coluna = int(input('Escolha a coluna (1, 2 ou 3) :')) - 1
    linha = int(input('Escolha a linha (1, 2 ou 3) :')) - 1

    if tabuleiro[coluna][linha] == '':
        tabuleiro[coluna][linha] = simbolo

        if simbolo == "X":
            jogador = False
        else:
            jogador = True

        tot_vazio -= 1

    else:
        print("O lugar escolhido já estava ocupado")

    for i in range(0, len(tabuleiro)):
        for j in range(0, len(tabuleiro)):
            print(f'[{tabuleiro[i][j]:^3}]', end='')
        print()

    for j, i in enumerate(tabuleiro):
        if i.count('X') == 3:
            print(f'Vitória do X na coluna {j}')
            break

        if i.count('O') == 3:
            print(f'Vitória do O na coluna {j}')
            break

print('-=' * 20)

if tot_vazio == 0:
    print('DEU VELHA')