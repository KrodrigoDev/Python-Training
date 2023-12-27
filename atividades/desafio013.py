from math import sin, tan, cos, radians, degrees

angulo = float(input('Digite o ângulo desejado: '))

# primeira se transforma o valor dado em radiano
# para depois converter em seno, cosseno ou tangente

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'o ângulo de {angulo} tem o SENO {seno:.2f}')
print(f'o ângulo de {angulo} tem o COSSENO {cosseno:.2f}')
print(f'o ângulo de {angulo} tem o TANGENTE {tangente:.2f}')
