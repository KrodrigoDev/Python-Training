from random import choice

numeroCadastro = 1

decisao = 'Sim'
listaAlunos = []

while decisao.lower() == 'sim':
    nome = str(input(f'{numeroCadastro} Aluno a ser cadastrado: '))
    listaAlunos.append(nome)
    numeroCadastro += 1
    decisao = str(input('Deseja continuar? (Sim/Não)'))

print(choice(listaAlunos))
