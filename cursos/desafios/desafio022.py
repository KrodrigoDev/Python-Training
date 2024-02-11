cidade = str(input('Digite o nome de uma cidade: ')).strip().upper()

index = cidade.find('SANTO')
contains = cidade in 'SANTO'

print(contains)
print(cidade[:5])

if index != -1:
    print('Contém SANTO no nome da cidade')

