from time import sleep


def inicializador(mensagem):
    print('--' * len(mensagem))
    print(f'{mensagem:^60}')
    for i in range(1, 4):
        sleep(1)
        print(f'{i:^60}')
    print('--' * len(mensagem))


inicializador('INICIANDO O PACOTE DESAFIOS EM')
