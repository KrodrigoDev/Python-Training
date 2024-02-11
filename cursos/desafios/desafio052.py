from random import randint

numero_aleatorio = randint(0, 10)
tentativas = 0
acertou = False
print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10')

while not acertou:

    palpite = int(input('Qual seu palpite: '))
    tentativas += 1

    if palpite == numero_aleatorio:
        acertou = True
    elif numero_aleatorio > palpite:
        print('Chute um número maior')
    else:
        print('Chute um número menor')

print(f'Foi necessário no total de {tentativas} para conseguir ganhar')
