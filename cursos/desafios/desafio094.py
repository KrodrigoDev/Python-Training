print(f'{'Controle de Terrenos':^30}')
print('-' * 30)


def area(l, c):
    res = l * c
    print(f'A área de um terreno {l}x{c} é de {res:.1f}m²')


print(' Controle de Terrenos')
print('-' * 20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

area(largura, comprimento)
