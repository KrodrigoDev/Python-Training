from datetime import date

dados = dict()

ano_atual = date.today().year

dados['nome'] = str(input('Nome : '))
dados['idade'] = ano_atual - int(input('Ano de nascimento : '))
dados['ctps'] = int(input('Carteira de trabalho (0 caso não tenha) :'))

# para se aposentar é necessário ter trabalhado mais de 35 anos

if dados['ctps'] != 0:
    dados['ano contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: '))

    tempo_servico = ano_atual - dados['ano contratação']

    # mostrando com quantos anos vou me aposentar
    dados['aponsetar'] = (35 - tempo_servico) + dados['idade']

print('-=' * 20)
print(dados)
for chave, valor in dados.items():
    print(f'a chave {chave} tem o valor {valor}')
