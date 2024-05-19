n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))
opcao = 0
while opcao != 5:

    print('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR
    ''')
    opcao = int(input('Opção selecionada: '))

    if opcao == 1:
        print(f'A soma entre {n1} + {n2} é {n1 + n2}')
    elif opcao == 2:
        print(f'A multiplicação entre {n1} + {n2} é {n1 * n2}')
    elif opcao == 3:
        maior = n1 if n1 > n2 else n2
        print(f'O maior número digitado entre {n1} e {n2} é {maior}')
    elif opcao == 4:
        n1 = int(input('Valor 1: '))
        n2 = int(input('Valor 2: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Essa opção não existe')

print('Adeus jovem')