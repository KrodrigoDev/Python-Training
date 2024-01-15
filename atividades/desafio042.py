s = 0
entrou = 0
# maneira de número 1
for i in range(3, 501, 3):
    if i % 2 != 0:
        entrou += 1
        s += i

print(f'A soma de todoss os {entrou} valores solicitados é {s}')

print('-=-' * 50)

# maneira número 2

sm = 0

for i in range(1, 501, 2):
    if i % 3 == 0:
        sm += i

print(sm)
