contador = somatorio = maior = menor = 0

res = 'S'
while res in 'Ss':

    n = int(input('Enter a number: '))

    contador += 1
    somatorio += n

    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n

        if n < menor:
            menor = n

    res = str(input('wants to continue [S/N] :'))

media = somatorio / contador

print('Acabou')

print(f'you enter {contador} numbers and the average between it is {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
