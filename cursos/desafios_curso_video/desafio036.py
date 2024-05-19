from random import randint
from time import sleep
print('''Suas opções:\n[0] PEDRA\n[1] PAPEL\n[2] TESOURA ''')

opcao_jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!')

opcao_computador = randint(0, 2)

itens = ['PEDRA', 'PAPEL', 'TESOURA']

print('-=' * 20)
print(f'O computador jogou {itens[opcao_computador]} ')
print(f'O jogador escolheu {itens[opcao_jogador]} ')
print('-=' * 20)

if opcao_computador == 0:
    if opcao_jogador == 0:
        print('DEU VELHA')
    elif opcao_jogador == 1:
        print('JOGADOR VENCEU')
    elif opcao_jogador == 2:
        print('COMPUTADOR VENCEU')
elif opcao_computador == 1:
    if opcao_jogador == 0:
        print('COMPUTADOR VENCEU')
    elif opcao_jogador == 1:
        print('DEU VELHA')
    elif opcao_jogador == 2:
        print('JOGADOR VENCEU')
elif opcao_computador == 2:
    if opcao_jogador == 0:
        print('JOGADOR VENCEU')
    elif opcao_jogador == 1:
        print('COMPUTADOR VENCEU')
    elif opcao_jogador == 2:
        print('DEU VELHA')
