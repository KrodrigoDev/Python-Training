def linha(tamanho=42):
    print('-' * tamanho)


def cabecalho(msg):
    linha()
    print(msg.center(42))
    linha()


def opcoes(ls):
    for indice, mensagem in enumerate(ls, start=1):
        print(f'{indice} - {mensagem}')
    linha()