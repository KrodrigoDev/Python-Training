# Entrada de dados
valor_casa = float(input('Digite o valor da casa: R$'))
salario_pessoa = float(input('Digite o seu salário: '))
anos_pagamento = int(input('Em quantos anos você pretende pagar: '))

# Transformando os anos em meses e calculando as prestações
prestacao = valor_casa / (anos_pagamento * 12)

# A prestação mensal não pode exceder 30% do salário ou o empréstimo será negado.
limite_prestacao = (salario_pessoa * 30) / 100

print(f'Para pagar uma casa de R${valor_casa:.2f} em {anos_pagamento} anos,', end='')
print(f' a prestação será de R${prestacao:.2f}')

if prestacao <= limite_prestacao:
    print('O empréstimo pode ser concedido.')
else:
    print('O empréstimo foi negado.')
