expressao = str(input('Digite a expressão: '))

print('FORMA 1')
qtd_aberto = expressao.count('(')
qtd_fechado = expressao.count(')')

print('Sua expressão está correta' if qtd_fechado == qtd_aberto else 'Sua expressão está errada')

print('=+' * 30)

print('FORMA 2 (Guanabara)')

pilha = []

for caractere in expressao:
    if caractere == '(':
        pilha.append('(')
    elif caractere == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está correta')
else:
    print('Sua expressão está errada')