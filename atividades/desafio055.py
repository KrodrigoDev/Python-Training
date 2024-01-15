# termo = int(input('Termo: '))
# razao = int(input('Razão: '))
#
# decimo = termo + (10 * razao)
#
# while termo < decimo:
#     print(f'[{termo}]')
#     termo += razao

print('GERADOR DE PA')
print('-=' * 10)

termo = int(input('Digite o primeiro termo: '))

razao = int(input('Digite a razão da PA: '))

primeiro = termo

contador = 0

limite = 10

while contador < limite:
    print(f'{primeiro}', end=' -> ')
    primeiro += razao
    contador += 1

    if contador == limite:
        print('PAUSA')

        add = int(input('Quantos termos vc quer mostrar a mais? '))
        if add == 0:
            print(f'A progressão foi finalizada com {limite} termos mostrados')
        else:
            limite += add

# count = 10
#
# for i in range(0, 10):
#     print(primeiro)
#     primeiro += razao

print('FIM')
