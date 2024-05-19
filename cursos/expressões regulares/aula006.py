import random
import re

# para validação dos campos
# ^ : começa com
# $ : termina com
# [^0-9] : negação

texto = '''Em 2023, João comprou 5 maçãs por R$ 10,00 cada. Ele gastou um total de R$ 50,00. Maria, por sua vez, 
          adquiriu 10 laranjas por R$ 1,50 cada, totalizando R$ 15,00. Ambos os amigos foram ao mercado no dia 15 de 
          junho.'''

a = re.findall(r'[0-9]+,[0-9]+', texto)
b = re.findall(r'[^A-Za-zçã ]{4}', texto)

texto_2 = ['457.475.457-56 , 754.754.747-98']

for i in texto_2:
    print(re.findall(r'^((?:[0-9]{3}\.){2}(?:[0-9]{3}-)(?:[0-9]{2}))$', str(i)))
