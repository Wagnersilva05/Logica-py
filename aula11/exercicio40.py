notas = []

for i in range(2):
    nota = float(input(f"{i+1}ª Nota: "))
    notas.append(nota)


soma = sum(notas)
media = soma / 2

print(f"\nMédia: {media}")

if(media >= 7):
    print("Aprovado!")
elif(media >= 5):
    print("Recuperação!")
else:
    print("Reprovado!")