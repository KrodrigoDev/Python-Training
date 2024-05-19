def escreva(palavra):
    tamanho = len(palavra) + 2
    print('~' * tamanho)
    print(f'{palavra:^{tamanho}}')
    print('~' * tamanho)


for i in range(0, 3):
    escreva(input('Escreva:'))
