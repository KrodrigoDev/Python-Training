from time import sleep


def escreva(mensagem):
    print('-=' * 20)
    print(mensagem)
    print('-=' * 20)


def contador(inicio, fim, passo):
    if passo < 0:
        passo = abs(passo)
    elif passo == 0:
        passo = 1

    escreva(f'Contagem de {abs(inicio)} até {abs(fim)} de {abs(passo)} em {abs(passo)}')

    if passo > 0 and inicio > fim:
        fim -= 1
        passo = -passo

    for i in range(inicio, fim, passo):
        print(i, end=' ', flush=True)
        sleep(0.5)
    print('FIM!')


contador(1, 10, 1)

contador(10, 0, 2)

escreva('Agora é a sua vez, personalize a contagem!')
contador(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passo: ')))
