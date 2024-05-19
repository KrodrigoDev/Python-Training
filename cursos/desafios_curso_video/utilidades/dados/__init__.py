def leiaDinheiro(texto):
    while True:
        valor = input(texto).replace(',', '.').strip()

        if valor.replace('.', '').isnumeric():
            return float(valor)
        else:
            print(f'Erro: "{valor}" é um preço inválido!')


def leia_int(numero):
    while True:
        try:
            numero = int(input(numero))
        except (ValueError, TypeError):
            print(f'ERRO: por favor, digite um valor válido.')
            continue
        except KeyboardInterrupt:
            print('O usuário optou por não digitar um número.')
            break
        else:
            return numero


def leia_float(numero):
    while True:
        try:
            numero = float(input(numero))
        except (ValueError, TypeError):
            print(f'ERRO: por favor, digite um valor válido.')
            continue
        except KeyboardInterrupt:
            print('O usuário optou por não digitar esse número')
            return 0
        else:
            return numero
