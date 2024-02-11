def leiaDinheiro(texto):
    while True:
        valor = input(texto).replace(',', '.', 1).strip()

        if valor.replace('.', '', 1).isnumeric():
            return float(valor)
        else:
            print(f'Erro: "{valor}" é um preço inválido!')
