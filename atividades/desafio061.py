soma = count = 0

print('~~~~' * 20)

while True:
    n = int(input('Enter a number: '))

    if n == 999:
        break
    count += 1
    soma += n

print('~~~~' * 20)

print(f'A soma de todos os {count} números digitados é de {soma}')
