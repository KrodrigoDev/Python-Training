lista_ordenada = []

for i in range(2, 10000, 2):
    lista_ordenada.append(i)

inicio = 0
fim = len(lista_ordenada) - 1

print(lista_ordenada)

item = int(input('Número desejado: '))
n_etapas = 0
while inicio <= fim:
    meio = (inicio + fim) // 2
    n_etapas += 1
    if lista_ordenada[meio] == item:
        print(f'O número {lista_ordenada[meio]} se encontra na posição {meio} ')
        break

    elif item < lista_ordenada[meio]:
        fim = meio - 1
    else:
        inicio = meio + 1

print(n_etapas)