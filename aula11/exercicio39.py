from datetime import date

atual = date.today().year
nascimento = int(input("Digite sua data de nascimento: "))

idade = atual - nascimento

print(f"Você tem {idade} anos")

if(idade == 18):
    print("É hora de se alistar!")
elif(idade < 18):
   saldo = 18 - idade
   print(f" Ainda falta {saldo} anos para o alistamento.")
elif (idade > 18):
   saldo = idade - 18
   print(f"Você já deveria ter se alistado há {saldo} anos")