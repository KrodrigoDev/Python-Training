print('===' * 20)
print('10 TERMOS DE UMA PA')
print('===' * 20)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão da progressão: '))

# progresso = termo
#
# for i in range(0, 10):
#     progresso += razao
#     print(f'{progresso} ', end='->')


decimo = termo + (10 * razao)

for i in range(termo, decimo, razao):
    print(f'{i}', end='->')

print('ACABOU')
