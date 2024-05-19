
algo = input("Digite algo: ")
tipo = type(algo)

print(f'''
    Tipo: {type(algo)}
    Númerico: {algo.isnumeric()},
    Alfabético: {algo.isalpha()},
    Alfa númerico: {algo.isalnum()},
    Somente espaço: {algo.isspace()},
    É um título: {algo.istitle()},
    Só letras minúsculas: {algo.islower()},
    Só letras maiúsculas: {algo.isupper()},
    Somente números: {algo.isdigit()}
''')
