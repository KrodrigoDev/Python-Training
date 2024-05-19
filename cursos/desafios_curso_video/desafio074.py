valores = []
pos_maior_valor = ''
pos_menor_valor = ''

for i in range(0, 5):
    valor = int(input(f'Enter the value {i}º: '))
    valores.append(valor)

maior_valor = max(valores)
menor_valor = min(valores)

for i, j in enumerate(valores):
    if j == maior_valor:
        pos_maior_valor += str(i) + '... '
    elif j == menor_valor:
        pos_menor_valor += str(i) + '... '

print(f'Você Digitou os valores {valores}')
print(f'O maior valor digitado foi {maior_valor} nas posições {pos_maior_valor}')
print(f'O menor valor digitado foi {menor_valor} nas posições {pos_menor_valor}')
