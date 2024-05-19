from datetime import date

ano_atual = date.today().year

ano_nascimento = int(input('Digite o ano em que vc nasceu: '))

idade = ano_atual - ano_nascimento

if idade < 18:
    print(f'Vc ainda deve esperar {18 - idade} anos para se alistar aos serviços brasileiros')
elif idade > 18:
    print(f'Infelizmente, o seu tempo acabou há {idade - 18} anos')
else:
    print('Ainda há tempo para se alistar!!')
