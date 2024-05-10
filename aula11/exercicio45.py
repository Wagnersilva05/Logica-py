import random
import os

os.system('cls')

usuario = str(input("Escolha: Pedra, Papel ou Tesoura: ")).strip().upper()

lista = ["PEDRA", "PAPEL", "TESOURA"]

if usuario in lista:
    maquina = random.choice(lista)

    if(maquina == "PEDRA" and usuario == "TESOURA") or (maquina == "TESOURA" and usuario == "PAPEL") or (maquina == "PAPEL" and usuario == "PEDRA"):
        print(f"Eu escolhi {maquina} e você {usuario}. Você perdeu! Tente novamente.")

    elif(usuario == maquina):
        print(f"Eu escolhi {maquina} e você {usuario}. Empatamos.")
    else:
        print(f"Eu escolhi {maquina} e você {usuario}. Parabéns! Você ganhou.")
else:
    print("Escolha Inválida! Tente novamente.")          