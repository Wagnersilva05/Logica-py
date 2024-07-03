from time import sleep
from os import system
def cabecalho():
    print('-'*30)
while True:
    try:    
        cabecalho()
        num = int(input("Digite um valor para a tabuada: "))
        if(num < 0):
            break 

        for i in range(1, 11):
            print(f"{num} X {i} = {num * i}")
    except ValueError:
        print("Digite um número!")
        sleep(2)
        system('cls')
        continue
