maior = menor = 0

for i in range(0, 5):
    peso = float(input(f'Peso {i + 1}º pessoa: '))

    if i == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(maior)
print(menor)
