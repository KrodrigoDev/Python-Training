pessoas = []
pessoa = []

maior_peso = menor_peso = 0

while True:
    nome = str(input('Digite seu nome: '))
    peso = float(input('Digite seu peso: '))

    pessoa.append(nome)
    pessoa.append(peso)
    pessoas.append(pessoa[:])

    if len(pessoas) == 1:
        maior_peso = menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        elif peso < menor_peso:
            menor_peso = peso

    pessoa.clear()

    continuar = str(input('Deseja continuar? ')).strip()[0]

    if continuar in 'Nn':
        break

print(f'Foram cadastradas um total de {len(pessoas)}')

indice = [[], []]
for i in pessoas:
    if maior_peso == i[1]:
        indice[0].append(i[0])
    elif menor_peso == i[1]:
        indice[1].append(i[0])

print(f'O maior peso foi de {maior_peso:.0f}Kg. Peso de {indice[0]}')
print(f'\nO menor peso foi de {menor_peso:.0f}Kg. Peso de {indice[1]}')
