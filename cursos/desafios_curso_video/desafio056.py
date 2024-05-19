print('---' * 10)
print('Sequência de Fibonacci')
print('---' * 10)

qtd_termo = int(input('Quantos termos você quer mostrar? '))

antecessor = 0
sucessor = 1

print('~~~~' * 10)

while qtd_termo != 0:
    print(f'{antecessor} ', end=' -> ')
    sucessor += antecessor
    antecessor = sucessor - antecessor

    qtd_termo -= 1

print('FIM')
print('~~~~' * 10)
