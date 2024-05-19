from datetime import date

meses = {
    '1': 31,
    '2': 28,
    '3': 31,
    '4': 30,
    '5': 31,
    '6': 30,
    '7': 31,
    '8': 31,
    '9': 30,
    '10': 31,
    '11': 30,
    '12': 31
}

data_atual = '15/02/2024'
data_nascimento = '30/07/1984'

ano_atual = int(data_atual[6:])
ano_nascimento = int(data_nascimento[6:])

mes_atual = int(data_atual[3:5])
mes_nascimento = int(data_nascimento[3:5])

dia_atual = int(data_atual[:2])
dia_nascimento = int(data_nascimento[:2])

idade = ano_atual - ano_nascimento

cont_ano = ano_nascimento

tot = 0

for i in range(0, idade + 1):

    if (cont_ano % 4 == 0) and (cont_ano % 100 != 0) or cont_ano % 400 == 0:
        meses['2'] = 29
    else:
        meses['2'] = 28

    if cont_ano == ano_nascimento or cont_ano == ano_atual:
        for chave, valor in meses.items():

            if int(chave) == mes_nascimento and cont_ano == ano_nascimento:
                tot += valor - dia_nascimento
            elif int(chave) == mes_atual and cont_ano == ano_atual:
                tot += dia_atual
            elif int(chave) > mes_nascimento and cont_ano == ano_nascimento:
                tot += valor
            elif int(chave) < mes_atual and cont_ano == ano_atual:
                tot += valor
    else:
        tot += sum(meses.values())

    cont_ano += 1

print(tot)
