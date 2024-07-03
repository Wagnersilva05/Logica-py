from os import system
from time import sleep
soma = 0
multiplicar = 1
numeros = []
for i in range(2):
    numero = int(input(f"{i+1}º Número: "))
    numeros.append(numero)
    
while True:
    print("\n\t===MENU===")
    print('''\t[1] - Somar 
        [2] - Multiplicar
        [3] - Maior número
        [4] - Novos números
        [5] - Sair do programa''')
    opcao = int(input("Digite a opção desejada: "))

    if(opcao == 1):
        for numero in numeros:
            soma = sum(numeros)
        print(f"Soma: {soma}")
        sleep(4)
        system('cls')
    elif (opcao == 2):
        for numero in numeros:
            multiplicar = numeros[0] * numeros[1]
        print(f"Multiplicação: {multiplicar}")
        sleep(4)
        system('cls')
    elif(opcao == 3):
        maiorNumero = max(numeros)
        print(f"Maior número: {maiorNumero}")
        sleep(4)
        system('cls')
    elif(opcao == 4):
        numeros.clear()
        for i in range(2):
            numero = int(input(f"{i+1}º Número: "))
            numeros.append(numero)
    elif(opcao == 5):
        break