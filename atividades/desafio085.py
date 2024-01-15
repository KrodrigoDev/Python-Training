turma = []

aluno = []
notas = []

while True:
    nome = str(input('Type your name: '))
    av1 = float(input('Note one: '))
    av2 = float(input('Note Two: '))

    aluno.append(nome)

    notas.append(av1)
    notas.append(av2)

    aluno.append(notas[:])
    notas.clear()

    turma.append(aluno[:])
    aluno.clear()

    continuar = str(input('type yes to continue or no to exit? [S/N]')).strip()[0]

    if continuar in 'Nn':
        break

print('-=' * 20)

print(f'NO.{" ":^10}NOME{" ":^10}MÉDIA')
print('--' * 20)
for j, i in enumerate(turma):
    media = sum(i[1]) / 2
    print(f'{j}{" ":^10} {i[0]}{" ":^10} {media:.1f}')

print('--' * 20)

while True:
    selecionar_aluno = int(input('Mostrar notas de qual aluno? (999 para interrompe): '))

    if selecionar_aluno == 999:
        break

    print(f'As notas do aluno {turma[selecionar_aluno][0]} são {turma[selecionar_aluno][1]}')
