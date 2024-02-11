number = int(input('Digite um número: '))

count = 0

for i in range(1, number + 1):
    if number % i == 0:
        print(f' {i} ', end='->')
        count += 1

if count == 2:
    print(' é primo')
else:
    print(' não é primo')
