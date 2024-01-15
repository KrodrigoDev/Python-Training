# valores = []
#
# for i in range(0, 5):
#     value_entered = int(input('please, enter a value: '))
#
#     if i == 0:
#         valores.append(value_entered)
#     else:
#
#         inserido = False
#         # 7 2 5 9 3
#         for indice, valor in enumerate(valores):
#             if value_entered <= valor:
#                 valores.insert(indice, value_entered)
#                 print(f'Adicionado na posição {indice} da lista')
#                 inserido = True
#                 break
#
#         if not inserido:
#             print('Inserido no final da lsita')
#             valores.append(value_entered)
#
# print(valores)
import  bisect
valores = []

for i in range(0, 5):
    valores.append(int(input('Type the value: ')))


for i in range(0, len(valores)):

    for j in range(i + 1, len(valores)):
        if valores[i] > valores[j]:

            aux = valores[i]

            valores[i] = valores[j]
            valores[j] = aux

print(valores)
