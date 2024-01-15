from datetime import date

count_maior = 0
count_menor = 0

ano_atual = date.today().year

for i in range(0, 7):
    ano = int(input(f'Em que ano nasceu a {i}º pessoa?'))

    if ano_atual - ano >= 18:
        count_maior += 1
    else:
        count_menor += 1

print(f'Ao total tivemos {count_maior} pessoas maiores de idade')
print(f'E também tivemos {count_menor} pessoas menores de idade')
