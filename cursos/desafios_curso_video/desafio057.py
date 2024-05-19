sum_number = 0
count = 0
n = 0
while n != 999:
    n = int(input('Enter number:'))
    if n != 999:
        count += 1
        sum_number += n

print(f'Vc digitou {count} números e a soma total entre eles foi de {sum_number}')
