print('-=' * 20)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

print('-=' * 20)

if (b + c > a) and (a + c > b) and (a + b > c):
    print('Os segmentos acima PODEM FORMAR triângulo')

    if a == b == c:
        print('Equilátero')
    elif a == b or c == a:
        print('Isósceles')
    else:
        print('Escaleno')

else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
