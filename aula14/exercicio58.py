from random import randint

contadorPalpite = 0
computador = randint(0, 10)

print("Adivinhe o numero de 0 a 10")
acertou = False

while not acertou:
   
    jogador = int(input("Qual o seu palpite? "))
    contadorPalpite +=1

    if(jogador == computador):
        acertou = True
    else:
        if(jogador < computador):
            print("Mais...Tente mais uma vez.")
        elif(jogador > computador):
            print("Menos...Tente outra vez.")

print(f"Acertou com {contadorPalpite} palpites!")