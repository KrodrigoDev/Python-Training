pessoa = dict()
pessoas = list()

while True:
    pessoa['nome'] = str(input('Nome : '))

    while True:
        pessoa['sexo'] = str(input('Sexo [M/F] : ')).strip().upper()[0]

        if pessoa['sexo'] in 'MF':
            break
        else:
            print('Por favor, digite apenas M ou F')

    pessoa['idade'] = int(input('Idade : '))

    pessoas.append(pessoa.copy())
    pessoa.clear()

    while True:
        cont = str(input('Deseja continuar [S/N]: '))[0].upper()
        if cont in 'SN':
            break
        else:
            print('ERRO, responda apenas S ou N')

    if cont in 'N':
        break

print('-=' * 20)

print(f'Total de pessoas cadastradas: {len(pessoas)}')

soma_idade = 0
mulheres_cadastradas = list()

for p in pessoas:
    soma_idade += p['idade']

    if p['sexo'] in 'Ff':
        mulheres_cadastradas.append(p['nome'])

media_idade = soma_idade / len(pessoas)

print(f'A média de idade das pessoas: {media_idade:5.2f}')

print(f'Todas as mulheres cadastradas: {mulheres_cadastradas}')

print('Lista das pessoas que estão acima da média: ')

for p in pessoas:
    if p['idade'] > media_idade:
        for i, j in p.items():
            print(f'{i} = {j} ', end=';')
        print()
print('<<< ENCERADO >>>')