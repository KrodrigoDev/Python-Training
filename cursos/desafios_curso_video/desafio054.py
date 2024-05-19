# from math import factorial
#
# fac = int(input('Digite um número para calcular seu fatorial: '))
# print(f'O fatorial de {fac} é {factorial(fac)}')

termo = int(input('Digite um número para calcular seu fatorial: '))

c = termo
f = 1

while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')

    f = f * c
    c -= 1

print(f)
