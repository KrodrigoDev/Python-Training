altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

area = altura * largura
litroTinta = area / 2  # cada dois metros quadrada de parede necessitam de um litro de tinta

print(f'Sua parede tem dimesão de {altura}X{largura} e a sua área é de {area}')
print(f'Para pintar essa parede, vc precisará de {litroTinta:.3} de tinta')
