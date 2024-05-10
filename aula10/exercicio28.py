from random import randint

escolhido = randint(0, 5)

numero = int(input("Adivinhe o numero de 0 a 5: "))



if(numero == escolhido):
    print("Parabéns! Você acertou.")
else:
    print(f"Errou! Eu pensei no {escolhido}.")    