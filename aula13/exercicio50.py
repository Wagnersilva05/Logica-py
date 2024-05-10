soma = 0

for i in range(6):
    numero = int(input(f"{i+1}º Número: "))
    

    if(numero % 2 == 0):
        soma += numero
print(f"Soma dos pares: {soma}")