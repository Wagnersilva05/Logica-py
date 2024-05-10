import os
import time
os.system('cls')

notas = []

try:

    for i in range(4):
        nota = int(input(f"{i+1}ª Nota: "))
        notas.append(nota)

        soma = sum(notas)
        media = soma / 4

except ValueError:
    print("Digite um Numero!")

finally:
    print("FIM!")    

print(f"Média: {media:.1f}")