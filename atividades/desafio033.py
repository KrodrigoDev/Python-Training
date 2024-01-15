n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = round((n1 + n2) / 2, 1)

if media < 5.0:
    print(f'REPROVADO: {media}')
elif 5.0 <= media <= 6.9:
    print(f'RECUPERAÇÃO: {media}')
else:
    print(f'APROVADO: {media}')
