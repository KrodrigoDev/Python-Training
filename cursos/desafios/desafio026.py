height = float(input('Enter your height:'))

weight = float(input('Enter your weigth: '))

imc = round(weight / (height * height), 2)

print(imc)
if imc < 18.5:
    print('magreza')
elif imc <= 24.9:
    print('Normal')
elif imc <= 29.9:
    print('Sobrepeso')
elif imc <= 34.9:
    print('Obesidade grau 1')
else:
    print('Faz exercício pelo amor de Deus!!')
