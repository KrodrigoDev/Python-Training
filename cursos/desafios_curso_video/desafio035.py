from datetime import date

ano_atual = date.today().year

ano_nascimento = int(input('Digite o ano em que vc nasceu: '))

idade = ano_atual - ano_nascimento

if idade <= 9:
    print(f'MIRIM: {idade}')
elif idade <= 14:
    print(f'INFANTIL: {idade}')
elif idade <= 19:
    print(f'JUNIOR: {idade}')
elif idade <= 20:
    print(f'SÊNIOR: {idade}')
else:
    print(f'MASTER: {idade}')
