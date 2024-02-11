jogador = dict()
jogadores = list()

while True:
    jogador['nome'] = str(input('Nome do jogador: '))

    qtd_partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))

    gols = list()
    for i in range(0, qtd_partidas):
        gols.append(int(input(f'Quantos gols na partida {i}? ')))

    jogador['gols'] = gols.copy()
    jogador['total'] = sum(gols)

    jogadores.append(jogador.copy())

    gols.clear()

    while True:
        cont = str(input('Quer continuar [S/N]: ')).strip()[0].upper()
        if cont in 'SN':
            break
        else:
            print('Digite apenas S ou N !!')

    if cont in 'Nn':
        break

    print('-' * 50)

print('-=' * 30)
print(f'cod nome {'':^8} gols {'':^10} total')

print('-' * 50)

for i, j in enumerate(jogadores):
    print(f'{i} {j['nome']} {'':^8} {j['gols']} {' ':^10} {j['total']}')

print('-' * 50)

while True:
    opcao = int(input('Mostrar dados de qual jogador (999 para sair) :'))

    if opcao == 999:
        break

    if 0 <= opcao < len(jogadores):
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[opcao]['nome']}:')
        for i, j in enumerate(jogadores[opcao]['gols']):
            print(f'{'':>3}No jogo {i}, fez {j} gols')
    else:
        print(f'Não existe jogador com código {opcao} ! Tente novamente')

print(f'<<< VOLTE SEMPRE >>>')
