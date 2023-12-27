nome_completo = str(input('Digite seu nome completo : ')).strip()

print(f'Nome com todas as letras em maiúsculo: {nome_completo.upper()}')

print(f'Nome com todas as letras em minúsculo: {nome_completo.lower()}')

print(f'Total de letras ao todo, sem considerar os espaços em branco: {len(nome_completo) - nome_completo.count(' ')}')

# existem muitas maneirass de se fazer o último desfio
# que é descobrir quantas letras tem o primeiro nome

one_blak_space = nome_completo.find(' ')

list_name = nome_completo.split()

print(f'Total de letras no primeiro nome: {len(nome_completo[:one_blak_space])}')
print(f'Total de letras no primeiro nome: {len(list_name[0])}')
