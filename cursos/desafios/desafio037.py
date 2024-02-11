# fazer o curso de bases númericas do curso em vídeo
# link: https://www.youtube.com/watch?v=J5q7s7l2EuI&list=PLHz_AreHm4dlmeSpWzJGWOmFnVF5k_IYi&ab_channel=CursoemV%C3%ADdeo

num = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL
''')

opcao = int(input('Digite sua opção: '))

if opcao == 1:
    print(f'{num} convertido para binário é igual a {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para octal é igual a {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para hexadecimal é igual a {hex(num)[2:]}')
else:
    print("A opção não existe")
