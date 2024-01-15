palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso',
            'Gratis', 'Estudar', 'Praticar', 'Trabalhar', 'Mercado',
            'Programador', 'Futuro')

for palavra in palavras:

    print(f'\nNa palavra {palavra.upper()} temos ', end='')

    palavra = palavra.lower()

    for i in range(0, len(palavra)):
        if palavra[i] in 'aeiou':
            print(palavra[i], end=' ')
