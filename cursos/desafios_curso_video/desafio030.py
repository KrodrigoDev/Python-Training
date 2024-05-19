from random import randint
from time import sleep

# feito no dia 27/12/2023
mega_sena = []
for i in range(6):
    mega_sena.append(randint(1, 60))

# print(f'Os números da mega sena são: {mega_sena}')

praias = ['Lagoa do pau', 'Pontal', 'Barreira']

sleep(1)
print('Realizando seleção em...')
sleep(1)
print('1')
sleep(1)
print('2')
sleep(1)
print('3')
sleep(2)

print(f'E a praia escolhida foi{praias[randint(0, 2)]}')
