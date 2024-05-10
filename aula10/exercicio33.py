
numeros = []

for i in range(3):
    numero = int(input(f"{i+1}º Número: "))
    numeros.append(numero)

    maior = max(numeros)
    menor = min(numeros)

print(f"Maior número: {maior}")
print(f"Menor número: {menor}")