from random import randint, randrange

count = 0

print('=-' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 20)

while True:

    number_rd = randint(0, 10)

    user_entered_number = int(input('Enter the number, plase : '))

    user_option = ''

    while (user_option != 'I') and (user_option != 'P'):
        user_option = str(input('Par ou Impar? ')).strip().upper()[0]
        print(user_option)

    soma = user_entered_number + number_rd

    par_or_impar = soma % 2

    print(f'Sua jogada {user_entered_number} e a jogada do computador {number_rd}. Total entre eles {soma} ', end='')
    print(f'{"PAR" if par_or_impar == 0 else "IMPAR"}')

    if (user_option == 'P' and par_or_impar == 0) or (user_option == 'I' and par_or_impar == 1):
        count += 1
        print('MUITO BEM CAMPEÃO!!!')
    else:
        print('Você perdeu !!')
        break

print(f'FORAM NO TOTAL {count}º VITÓRIAS')
