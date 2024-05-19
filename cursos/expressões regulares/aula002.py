# metacaractere : . ^ $ * + ? { } [ ] \ | ( )

# | : é o nosso "OU"
# . : é qualquer caracatere (com exceção da qeubra de linha)
# [] : serve para definir uma cadeia de caracteres
# - : funciona como um range. exemplo [a-z]
# flags : auxiliar que pode usr ignorecase e outros


import re

texto_1 = '''
Uma raposa conseguiu invadir a casa de um ator e começou a remexer nos seus pertences. Foi aí que 
encontrou uma máscara linda, repleta de ornamentos e decorações. Segurou o objeto e exclamou: "Que cabeça bonita! 
Pena que não tem um cérebro lá dentro”. Moral: A aparência exterior nem sempre reflete aquilo que existe no nosso 
espírito.'''

texto_2 = '''
Tudo acontece e tudo permanece,

mas a nossa é passar,

passar caminhos

estradas sobre o mar
'''

texto_3 = '''35T3 P3QU3N0 T3XTO 53RV3 4P3N45 P4R4 M05TR4R COMO NO554 C4B3Ç4 CONS3GU3 F4Z3R CO1545 1MPR3551ON4ANT35! 
R3P4R3 N155O! NO COM3ÇO 35T4V4 M310 COMPL1C4DO, M45 N3ST4 L1NH4 SU4 M3NT3 V41 D3C1FR4NDO O CÓD1GO QU453 
4UTOM4T1C4M3NT3, S3M PR3C1S4R P3N54R MU1TO, C3RTO? POD3 F1C4R B3M ORGULHO5O D155O! SU4 C4P4C1D4D3 M3R3C3! P4R4BÉN5!
'''


print(re.findall(r'[0-9]N.', texto_3))
