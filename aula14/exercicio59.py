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
        [4] - novos números
        [5] - Sair do programa''')
    opcao = int(input("Digite a opção desejada: "))
    system('cls')

    if(opcao == 1):
        soma += numeros
        print(f"Soma: {soma}")
        sleep(2)
    elif (opcao == 2):
        multiplicar *= numeros
        print(f'Multiplicação: {multiplicar}')
        sleep(2)
    elif(opcao == 3):
        maiorNumero = max(numeros)
        print(f"Entre {numeros[0]} e {numeros[1]}, o maior é {maiorNumero}")
        sleep(2)
    elif(opcao == 4):
       numeros.clear()
       for i in range(2):
        numero = int(input(f"{i+1}º Número: "))
        numeros.append(numero)
    elif(opcao == 5):
        break  
    else:
        print('Opção inválida.Tente novamente.')
        sleep(2)