import re
from typing import List

# Lookahead: vai fazer uma checagem no final da palavra
# Lookbehind: vai fazer uma checagem no inicio da palavra


texto = '''
Online 198.457.87.1 Active
Offline 198.457.87.2 Inactive
Offline 198.457.87.3 Inactive
Online 198.457.87.4 Active
Online 198.457.87.5 Active
Offline 198.457.87.6 Inactive
'''

# lookahead positive
a = re.findall(r'\w+\s(\d{3}\.\d{3}\.\d{2}\.\d{1})\s(?=Active)', texto)

# lookahead negativo
b = re.findall(r'\w+\s(\d{3}\.\d{3}\.\d{2}\.\d{1})\s(?!Inactive)', texto)

texto_2 = '2.50kg - R$45.00 4.35kg - R$122.00 5.60kg - R$122.00...'

c = re.findall(r'\d+\.\d+(?=kg)', texto_2)

# Lookbehind positivo

d = re.findall(r'(?<=R\$)\d+\.\d+', texto_2)

emails: List[str] = ['john_doe@gmail.com', 'marilia022@yahoo.com.br', 'gustavo_amado@outlook.com']

for email in emails:
    print(re.findall(r'\w+\w+@(\w+)\.\w+',email))