from time import sleep


def maior(*valores):
    print('-=' * 30)
    print('Analisando os valores passados...')

    maior_valor = 0

    if len(valores) != 0:
        for valor in valores:
            print(valor, end=' ', flush=True)
            if valor > maior_valor:
                maior_valor = valor
            sleep(0.6)

    print(f'Foram informados {len(valores)} valores ao todo.')
    print(f'O maior valor informado foi {maior_valor}.')


maior(4, 7, 8, 5, 9, 8, 7, 4, 5, 7, 4, 5, 7, 4, 5, 1, 7, 100, 1, 4, 1, 1, 5, 7)
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
