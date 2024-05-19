# metacaractere : . ^ $ * + ? { } [ ] \ | ( )

# * : 0 ou n repetições
# + : 1 ou n repetições
# ? : 0 ou 1
# {} : pode ser n repetições ou min e max. exemplo {0,} isso seria de 0 até n

# nota: os quantificadores são aplicados sempre ao caractere da esquerda

import re

texto_4 = '''
João trouxe
flores para sua amada namorada em 10 de janeiro de 1970,
8
9
Maria era O nome dela.
10
11
12 oi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
13
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
14 domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
15 pão de queijo.
16 Não canso de ouvir a Maria:
17 " Jooooãoo:0oo:oo, o café tá prontinho aqui. Veeemm veem vem"!
Jã
'''

texto_5 = 'João ama ser amado, Por isso Maria não o amara de volta, já que ela o amou antes e foi rejeitada.'

# print(re.findall('jo+ão+|maria', texto_4, flags=re.I))
# print(re.sub('jo+ão+', 'Kauã', texto_4, flags=re.I))
print(re.findall('jo{0,}ão{0,}', texto_4, flags=re.I))
# print(re.findall(r'[vV]e{1,3}m+', texto_4))
# print(re.findall(r'am[a-z]*', texto_5))

texto_6 = '''
Em uma cidade distante, havia uma antiga biblioteca que guardava milhares de livros. O ar rarefeito e empoeirado envolvia cada canto daquela vasta coleção. Os livros estavam dispostos em estantes antigas e desgastadas, organizados em fileiras intermináveis.

Na seção de literatura clássica, você poderia encontrar obras como 'Dom Quixote', 'Romeu e Julieta', 'Os Miseráveis' e 'Orgulho e Preconceito'. Cada livro era um portal para um mundo diferente, um mundo criado pelas palavras de autores talentosos que viveram em épocas distintas.

Na ala de ciências, os tomos encadernados tratavam de assuntos como física, química, biologia e astronomia. Desde as leis de Newton até os mistérios do universo, os livros continham conhecimentos acumulados ao longo de séculos de pesquisa e descobertas.

A seção de história abrangia desde a antiguidade até os tempos contemporâneos, cobrindo civilizações perdidas, grandes impérios, guerras e revoluções. Cada página revelava os eventos que moldaram o mundo em que vivemos hoje.

No entanto, a biblioteca não estava imune ao tempo. Algumas páginas estavam desbotadas, outras rasgadas pelo uso constante ao longo dos anos. Mas, apesar dos estragos do tempo, o conhecimento contido ali permanecia intacto, esperando ser descoberto por aqueles que se aventurassem entre suas estantes.

Ao explorar aquele vasto tesouro de sabedoria, os visitantes podiam sentir a presença dos grandes pensadores do passado, cujas palavras continuavam a ecoar pelos corredores silenciosos da biblioteca, inspirando e educando as gerações presentes e futuras.

'''

# print(re.findall('[lL]ivro.|[Bb]lioteca.', texto_6))


texto_7 = '''
Existem diversas formas de se escrever um endereço de e-mail. Alguns exemplos incluem: john.doe@example.com, alice_smith@example.co.uk, bob123@example.net.

Além disso, endereços de e-mail podem conter caracteres especiais, como ponto (.), underscore (_), e hífen (-), além dos caracteres alfanuméricos.

Por exemplo, o endereço de e-mail mary-ann.jones123@example-domain.info é válido, assim como mark@example.co.jp.

No entanto, há algumas restrições quanto ao formato dos endereços de e-mail. Por exemplo, eles devem começar com um caractere alfanumérico, seguido de zero ou mais caracteres alfanuméricos, pontos, underscores ou hífens. Após o caractere '@', deve haver pelo menos um caractere alfanumérico, seguido por zero ou mais grupos de caracteres alfanuméricos, pontos, underscores ou hífens, separados por um ponto. O último grupo de caracteres após o ponto deve conter entre dois e quatro caracteres alfabéticos.

Exemplos de endereços de e-mail válidos incluem: user@example.com, john.doe@example.co.uk, alice_smith@example.net, bob123@example.org, mary-ann.jones@example-domain.info, mark@example.co.jp.
'''

repex = re.compile('[a-z0-9_-]')

print(re.findall('[a-z0-9_.-]+@[a-z0-9_.]+', texto_7, flags=re.I))
