from random import shuffle

vezes = int(input('Quantos alunos serão cadastrados: '))

listaAlunos = []

for i in range(vezes):
    aluno = str(input(f'Digite o nome do aluno número {i}: '))
    listaAlunos.append(aluno)


# Realizando o emparalhamento na lista de alunos
shuffle(listaAlunos)

print(f'A lista de alunos escolhidos pelo professor é: {listaAlunos}')

