b = sum([800, 70, 5])

b_str = str(b)
comma_index = len(b_str) % 3

lista = []
for i, digit in enumerate(b_str):
    lista.append(digit)
    if (i + 1 - comma_index) % 3 == 0 and i != len(b_str) - 1:
        lista.append(',')

result = ''.join(lista)
print(result)


