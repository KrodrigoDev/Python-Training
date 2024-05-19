aluno = {
    'nome': str(input('Nome:')),
    'media': float(input('Média:'))
}

for i, j in aluno.items():
    print(f'{i} é igual a {j}')

aluno['situacao'] = 'aprovado' if aluno['media'] >= 7 else 'reprovado'

print(f'Situação é igual a {aluno['situacao']}')
