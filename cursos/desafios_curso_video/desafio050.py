soma_idade = 0

nome_maior_idade = ''
maior_idade_homem = 0

menor_20_F = 0

for i in range(0, 4):
    print(f'---- {i + 1}º Pessoa ----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    if i == 0 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_maior_idade = nome
    else:
        if idade > maior_idade_homem and sexo in 'Mm':
            maior_idade_homem = idade
            nome_maior_idade = nome
        elif sexo in 'Ff' and idade < 20:
            menor_20_F += 1

    soma_idade += idade


media_idade = soma_idade / 4

print(f'A média de idade do grupo é de {media_idade:.1f} anos')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_maior_idade}')
print(f'Ao todo são {menor_20_F} mulheres com menos de 20 anos')
