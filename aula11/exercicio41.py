nascimento = int(input("Digite sua data de nascimento: "))

idade = 2024 - nascimento

if(idade <= 9):
    print(f"Você tem {idade} anos , sua categoria é MIRIM.")
elif(idade <= 14):
    print(f"Você tem {idade} anos, sua categoria é INFANIL.")
elif(idade <= 19):
    print(f"Você tem {idade} anos, sua categoria é JUNIOR.")
elif(idade <= 25):
    print(f"Você tem {idade} anos, sua categoria é SÊNIOR.")
else:
    print(f"Você tem {idade} anos, sua categoria é MASTER")   