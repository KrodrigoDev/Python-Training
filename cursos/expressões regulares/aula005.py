# metacaractere : . ^ $ * + ? { } [ ] \ | ( )

# grupos

# () :

# os grupos tem sua variável armazenada na memoria, isso torna possível
# conseguir acessá-los atráves da sintaxe "\1" que é chamado de retrovisor

# (?:) : para não salvar um grupo

# obs : deve se contar os indíces pela abertura do grupo

import re
from pprint import pprint

texto_1 = '''
<p> </p> <p>Eita</p> <p>Qualquer Frase</p> <p>Não</p> <div>magia</div><div>UEBA</div><div>Frase 7</div>
'''
texto_2 = 'leo lima kaua rodrigo barbosa'

# pprint(re.findall(r'(le)', texto_2))

# tags = re.findall(r'(<([dpiv]{1,3})>(.*?)</\2>)', texto_1, flags=re.I)
# tags_2 = re.findall(r'<([dpiv]{1,3})>(?:.*?)</\1>', texto_1, flags=re.I)
# pprint(tags_2)

# print(re.sub(r'(<([pdiv]{1,3})>)(.+?)(</\2>)', r'\1 kakau \4',texto_1))

# for tag in tags:
#     pprint(tag[2])

# texto_3 = '154.235.478-89, 154.235.478-89'
#
# print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', texto_3))

texto_3 = '''
<table>
  <tr>
    <th>Company</th>
    <th>Contact</th>
    <th>Country</th>
  </tr>
  <tr>
    <td>Alfreds Futterkiste</td>
    <td>Maria Anders</td>
    <td>Germany</td>
  </tr>
  <tr>
    <td>Centro comercial Moctezuma</td>
    <td>Francisco Chang</td>
    <td>Mexico</td>
  </tr>
</table>
'''

print(re.findall(r'(<([a-z]+)>)(.+)(</\2>)', texto_3))
print(re.sub(r'(<([a-z]+)>)(.+)(</\2>)',r'\1 RUSSO x EBERT \4', texto_3))
