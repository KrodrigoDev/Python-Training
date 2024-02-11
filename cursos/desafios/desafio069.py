from random import randint

tupla = ()

maior = menor = 0

for i in range(0, 5):

    number_random = randint(1, 10)
    tupla += (number_random,)

    if i == 0:
        maior = menor = number_random
    else:

        if number_random > maior:
            maior = number_random

        if number_random < menor:
            menor = number_random

print(f'Os valores sorteados foram : {tupla}')
print(f'O maior valor sorteado foi: {max(tupla)}')
print(f'O menor valor sorteado foi: {min(tupla)}')