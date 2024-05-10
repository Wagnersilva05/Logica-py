import os
import time

contador = 0
soma = 0

numero = int(input("Digite um numero positivo: "))

while(numero <= 0):
    print("O numero inserido não é válido. Por favor, insira um número positivo.")
    time.sleep(4)
    os.system('cls')
    numero = int(input("Digite um numero positivo: "))

while(numero > 0):
    soma += numero
    contador += 1
    numero = int(input("Digite um numero: "))

if contador != 0:
    media = soma / contador
    print(f"A media dos numeros é: {media:.2f}")
else:
    print("Nenhum número positivo foi inserido.")