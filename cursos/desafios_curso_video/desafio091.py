contato = dict()
contatos = list()
contatos_2 = list()

for i in range(0, 2):
    contato['nome'] = input('Nome: ')
    contato['telefone'] = input('Telefone: ')
    contatos.append(contato.copy())
print('AGENDA 1: ')
for i, j in enumerate(contatos):
    print(f'contanto{i} : {j.get('nome', 'O contato não existe')}')

for i in range(0, 2):
    contato['nome'] = input('Nome: ')
    contato['telefone'] = input('Telefone: ')
    contatos_2.append(contato.copy())

contatos_2.extend(contatos)
del contatos
print('AGENDA 2 (junção) : ')
for i, j in enumerate(contatos_2):
    print(f'contanto{i} : {j.get('nome', 'O contato não existe')}')
