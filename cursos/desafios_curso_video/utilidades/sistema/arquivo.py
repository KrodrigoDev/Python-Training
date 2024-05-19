import pandas as pd

caminho_arquivo = (r'C:\Users\Kauã Rodrigo\Documents\Scripts-Python\Curso em '
                   r'vídeo\Idea\CursoEmVideo\cursos\desafios\utilidades\sistema\sistema.csv')


def ler_arquivo():
    df = pd.read_csv(caminho_arquivo, sep=';')
    return df


def criar_arquivo():
    df = pd.DataFrame(columns=['Nome', 'Idade'])
    df.to_csv('../sistema/sistema.csv', index=False, sep=';')


def validacao_arquivo():
    while True:
        try:
            df = ler_arquivo()
        except FileNotFoundError:
            criar_arquivo()
            continue
        else:
            return df
