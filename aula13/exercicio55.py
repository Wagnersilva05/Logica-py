pesos = []
for i in range(3):
    peso = float(input(f"{i+1}º Peso: "))
    pesos.append(peso)

maiorPeso = max(pesos)
menorPeso = min(pesos)

print(f"Maior peso: {maiorPeso:.2f}")
print(f"Menor peso: {menorPeso:.2f}")