from time import sleep
sexo = str(input("Digite seu sexo: ")).strip().upper()[0]
while sexo not in 'FM':
    sexo = str(input("Dados inválido. Por favor, digite seu sexo: ")).strip().upper()[0]
    
print(f"Sexo cadastrado: {sexo}")   