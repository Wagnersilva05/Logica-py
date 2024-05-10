numeros = []
for i in range(2):
    numero = int(input(f"{i+1}º Número: "))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)

if(numeros[0] == numeros[1]):
    print("Esses números são iguais.")
else:
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")