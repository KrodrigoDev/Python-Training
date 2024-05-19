massa_inicial = 100
tempo = 0

while massa_inicial >= 0.05:
    massa_inicial /= 2
    tempo += 50
    print(f'Massa: {massa_inicial} no tempo: {tempo}')
