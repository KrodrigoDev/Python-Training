valor_produto = float(input('Digite o valor do produto: R$ '))

print('-=' * 20)

print("""
[1] para comprar á vista
[2] para comprar á vista no cartão
[3] para parcelar em até 2x no cartão
[4] para parcelar em até 3x ou mais no cartão
""")

print('-=' * 20)

opcao = int(input('Digite sua opção de pagamento: '))

if opcao == 1:
    desconto = valor_produto - (valor_produto * 10 / 100)
    print(f'O preço do produto vai de R${valor_produto:.2f} para R${desconto:.2f}')
elif opcao == 2:
    desconto = valor_produto - (valor_produto * 5 / 100)
    print(f'O preço do produto vai de R${valor_produto:.2f} para R${desconto:.2f}')
elif opcao == 3:
    print(f'O preço do produto vai permanecer o mesmo R${valor_produto:.2f}')
else:
    juros = valor_produto + (valor_produto * 20 / 100)
    print(f'O preço do produto vai de R${valor_produto:.2f} para R${juros:.2f}')
