tupla = ()
pares = ()

for i in range(1, 5):
    value = int(input(f'Enter a value {i}º : '))
    if value % 2 == 0:
        pares += (value,)
    tupla += (value,)

print('-=' * 20)

print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu: {tupla.count(9)} vezes')

if 3 in tupla:
    print(f'O valor três apareceu pela primeira vez no índice {tupla.index(3) + 1}º')
else:
    print(f'O número 3 não está presente')

print(f'Os números pares foram: ', end='')
for i in tupla:
    if i % 2 == 0:
        print(i, end=' ')
