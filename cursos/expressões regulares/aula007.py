import re

# shorthands são essas abreviações
# \w : [A-z0-9Á-Ú] significa isso aqui e outras coisas
# \W : é a negação do shorthand acima
# \d : [0-9] vai encontrar a mesma apenas números
# \D : [^0-9] vai encontrar o inverso
# \s : [ \n\r\f\t] isso vai capturar quebras de linha no geral e espaços em branco
# \b : [\bflo+] ou [\bj\w+] vai pegar as bordas de uma palavra

texto = '''Em 2023, João comprou 5 maçãs por R$ 10,00 cada. Ele gastou um total de R$ 50,00. Maria, por sua vez, 
          adquiriu 10 laranjas por R$ 1,50 cada, totalizando R$ 15,00. Ambos os amigos foram ao mercado no dia 15 de 
          junho.'''

# print(re.findall(r'[^A-z0-9Á-Ú]+', texto, flags=re.I))
# print(re.findall(r'\W+', texto))
# print(re.findall(r'/S+', texto))
print(re.findall(r'\bj\w+', texto))
print(re.findall(r'\w+a\b', texto))
print(re.findall(r'\b\w{4}\b', texto))
