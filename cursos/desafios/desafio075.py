values = []

while True:
    value = int(input('Enter the value: '))

    if not (value in values):
        values.append(value)
        print('Value add')
    else:
        print('Value duplication, not add')

    opc = str(input('Enter yes to continue or no to exit: ')).strip()[0].upper()

    while 'YN' in opc:
        opc = str(input('Enter the yes or no, please: '))

    if opc == 'N':
        break

values.sort()

print(f'you typed the values: {values}')
