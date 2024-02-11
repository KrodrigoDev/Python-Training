numbers_entered = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
                   'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
                   'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete',
                   'dezoito', 'dezenove', 'vinte')

print('~~~' * 10)

while True:
    option_user = int(input('Enter a number between zero and twenty: '))
    if 0 <= option_user < 21:
        break
    print('Tente novamente.', end='')

print('~~~' * 10)

print(f'Vc digito o número {numbers_entered[option_user]}')
