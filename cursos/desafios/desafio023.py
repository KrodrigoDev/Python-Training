sentence = str(input('Digite qualquer coisa: ')).strip()

full_letter_A = sentence.count('A')

first_index_letter_A = sentence.find('A')

last_index_letter_A = sentence.rfind('A')

print(f"""
 full letters 'A' = {full_letter_A},
 first occurrence letters 'A' = {first_index_letter_A}
 last occurrence letters 'A' = {last_index_letter_A}
""")
