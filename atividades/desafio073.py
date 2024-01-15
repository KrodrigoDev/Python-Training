notas = [0, 0, 9.0, 8.0, 5.0, 10.0, 7.0, 7.5, 4.0, 10.0, 7.0, 7.0, 8.0, 8.0, 7.5]

while 0 in notas:
    notas.remove(0)

soma = 0

for i in notas:
    soma += i

media = soma / len(notas)

print(f'{media:.2f}')