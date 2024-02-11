lista = [5, 6, 10, 15, 80, 100, 150]

fim = len(lista) - 1
inicio = 0

numeroDesejo = int(input('Digite o número desejado: '))

achou = False

while inicio <= fim:

    meio = (inicio + fim) // 2

    if lista[meio] == numeroDesejo:
        achou = True
        break

    elif numeroDesejo > lista[meio]:
        inicio = meio + 1

    else:
        fim = meio - 1

if achou:
    print('Encontrou')
else:
    print('não encontrou')
