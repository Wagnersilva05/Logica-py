num = int(input("Digite um número inteiro: "))
print('''Escolha uma das bases para conversão:
[ 1 ] converter BINÁRIO
[ 2 ] converter OCTAL
[ 3 ] converter HEXADECIMAL''')
opcao = int(input("Digite a opção: "))

if(opcao == 1):
    print(f"{num} convertido para BINÁRIO é igual a {bin(num)[2:]}")
elif (opcao == 2):
    print(f"{num} convertido para OCTAl é igual a {oct(num)[2:]}")
elif (opcao == 3):
    print(f"{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}")
else:
    print("Opção inválida")   