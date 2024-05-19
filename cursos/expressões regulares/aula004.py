# metacaractere : . ^ $ * + ? { } [ ] \ | ( )

# * : 0 ou n repetições
# + : 1 ou n repetições
# ? : 0 ou 1

# expressões gulosas e não gulosas

# Analogia
# O guloso come ate não ter mais comida.
#
# O não-guloso come um pouco verifica se é suficiente,
# então come mais um pouco e verifica se já é suficiente, e assim vai.

import re

texto_1 = '''
<p> </p> <p>Eita</p> <p>Qualquer Frase</p> <p></p> <div>magia</div><div>UEBA</div><div>Frase 7</div>
'''

# forma gulosa onde faz a verificação da última expressão por todo o texto
print(re.findall(r'<[dpiv]{1,3}>.+</[dpiv]{1,3}>', texto_1, flags=re.I))

# forma não gulosa, onde para a satisfação da expressão
print(re.findall(r'<[dpiv]{1,3}>.+?</[dpiv]{1,3}>', texto_1, flags=re.I))
