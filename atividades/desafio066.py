# print('~~~~' * 5)
# print('BANCO KR')
# print('~~~~' * 5)
#
# n = int(input('Valor: R$ '))
#
# nota_cinqueta = nota_vinte = nota_dez = nota_um = 0
#
# while True:
#     cinquenta = n // 50
#     nota_cinqueta += cinquenta
#     n %= 50
#
#     vinte = n // 20
#     nota_vinte += vinte
#     n %= 20
#
#     dez = n // 10
#     nota_dez += dez
#     n %= 10
#
#     um = n // 1
#     nota_um += um
#     n %= 1
#
#     if n == 0:
#         break
#
# print(nota_cinqueta)
# print(nota_vinte)
# print(nota_dez)
# print(nota_um)


print('=-' * 10)
print('BANCO KR')
print('=-' * 10)

valor = int(input('Insira o valor a ser sacado : R$'))
cedula = 50
qntd = 0

while True:

    qntd = valor // cedula
    valor = valor % cedula

    if qntd != 0:
        print(f'São {qntd} cédulas de R${cedula}')
    else:
        if cedula == 50:
            cedula = 20

        elif cedula == 20:
            cedula = 10

        elif cedula == 10:
            cedula = 1

    if valor == 0:
        break

print('Volte sempre ao banco KR')
