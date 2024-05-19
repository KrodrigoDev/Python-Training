# https://docs.python.org/pt-br/3.8/howto/regex.html
# https://docs.python.org/pt-br/3.8/library/re.html#module-re

import re

# findall vai enocntrar todas as ocorrências
# search vai voltar a primeira ocorrências
# sub para realizar substituição

# compile para compilar as expressões regulares e evitar repetição


frase_1 = 'Essa palavra é um teste de expressões teste regulares.'

# método padrão e com repetição
print(re.search(r'teste', frase_1))
print(re.findall(r'teste', frase_1))
print(re.sub(r'teste', 'ABCD', frase_1, count=1))

# usando o compile e evitando repetição

regexp = re.compile(r'teste')  # isso evita a repetição da expressão
print(regexp.search(frase_1))
print(regexp.findall(frase_1))
print(regexp.sub('UAU', frase_1))
