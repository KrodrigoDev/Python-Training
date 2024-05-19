import re

# Flags
# re.A : pega apenas os caracteres da tabela ascii
# re.I : ignorecase
# re.M : é o multilane que é igual ao ^ $
# re.S : para reconhcer as quebras de linhas

texto = '''
458.745.787-29 AVC
795.745.254-79 ADA
697.325.456-59
'''

# print(re.findall(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', texto, flags=re.MULTILINE))

texto_2 = '''O joão gosta de folia 
           E adora ser amado'''

print(re.findall(r'^o.*o$', texto_2, flags=re.I | re.S))
