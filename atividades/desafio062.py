while True:
    n = int(input('Enter a number (enter zero to stop) :  '))

    if n <= 0:
        break

    for i in range(1, 11):
        print(f'{i} X {n} = {i * n}')

print('PROGRAMA TABUADA ENCERRADO. volte sempre!')
