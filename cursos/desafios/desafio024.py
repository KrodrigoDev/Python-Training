name_full = str(input('enter the your name full: '))


list_name = name_full.split()

print(f""""
Name full: {name_full}
Fisrt name: {list_name[0]}
lat name: {list_name[len(list_name) - 1]}
""")
