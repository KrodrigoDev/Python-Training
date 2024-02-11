mulheres_mais_20 = tot_homens = tot_mais_18 = 0

while True:

    print('----' * 10)
    print('CADASTRE UMA PESSOA')
    print('----' * 10)

    idade = int(input('Enter the your age: '))

    while True:
        sexo = str(input('Enter the your sex: ')).strip().upper()[0]
        if sexo in 'M' or sexo in 'F':
            break

    if idade > 18:
        tot_mais_18 += 1

    if sexo in 'Mm':
        tot_homens += 1

    if sexo in 'Ff' and idade < 20:
        mulheres_mais_20 += 1

    while True:
        continuar = str(input('Deseja continuar [S/N] ?')).strip().upper()[0]
        if continuar in 'S' or continuar in 'N':
            break

    if continuar == 'N':
        break

print(f'O total de pessoas com mais de 18 anos: {tot_mais_18}')
print(f'Ao todo temos {tot_homens} homens cadastrados')
print(f'E temos {mulheres_mais_20} mulheres com menos de 20 anos')
