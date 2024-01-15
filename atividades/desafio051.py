sexo = str(input('Informe o seu sexo: ')).upper()

while sexo not in 'MF':
    # eu poderia tirar os espaços e depois pegar apenas o índice 0
    sexo = str(input('Dados inválidos. Informe o sexo novamente: ')).upper()

print(f'Sexo {sexo} registado com sucesso')
