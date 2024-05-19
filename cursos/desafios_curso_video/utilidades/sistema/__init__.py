from cursos.desafios_curso_video.utilidades.sistema.interface import *
from cursos.desafios_curso_video.utilidades.dados import leia_int
from cursos.desafios_curso_video.utilidades.sistema.arquivo import *


def menu():
    while True:
        try:
            cabecalho('MENU PRINCIPAL')
            opcoes(['VER PESSOAS CADASTRADAS', 'CADASTRAR NOVA PESSOA', 'SAIR DO SISTEMA'])

            opcao = leia_int('Informe sua opção: ')

        except (ValueError, TypeError):
            print('O formato enviado não é válido. Escolha novamente !!')
            continue
        except KeyboardInterrupt:
            print('O usuário optou por encerrar o sistema.')
            break
        else:
            if opcao == 1:
                listar()
            elif opcao == 2:
                cadastrar()
            elif opcao == 3:
                cabecalho('SAINDO DO SISTEMA... ATÉ LOGO')
                break
            else:
                print('Essa opção não existe. Escolha novamente !!')


def cadastrar():
    df = validacao_arquivo()

    cabecalho('NOVO CADASTRO')

    while True:
        try:
            nome = input('Nome: ')
            idade = leia_int('Idade: ')
        except (ValueError, TypeError):
            print('Os valores foram fornecidos de forma incorreta. Informe novamente!')
            continue
        except KeyboardInterrupt:
            print('O usuário optou por interroper a inserção !')
            break
        else:
            nova_linha = pd.Series({
                'Nome': nome,
                'Idade': idade
            })

            df = df._append(nova_linha, ignore_index=True)
            df.to_csv(caminho_arquivo, index=False, sep=';')

            break


def listar():
    df = validacao_arquivo()

    cabecalho('PESSOAS CADASTRADAS')

    for index, row in df.iterrows():
        print(f'{row["Nome"]:<30} {row["Idade"]} anos')
