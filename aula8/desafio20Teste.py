import os
os.system('cls')

notas = []

for i in range(5):
    nota = float(input(f" {i+1}ª Nota: "))
    notas.append(nota)
    
    somaNotas = sum(notas)
    media = somaNotas / 5


print(f"Média: {media}") 