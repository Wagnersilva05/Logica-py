from datetime import date

maiorIdade = 0
menorIdade = 0

for i in range(7):
    nascimento = int(input(f"{i+1}ª Data de nascimento: "))

    atual = date.today().year
    idade = atual - nascimento

    if(idade >= 21):
        maiorIdade += 1
    else:
        menorIdade += 1

print(f"Maior idade: {maiorIdade} Pessoas")
print(f"Menor idade: {menorIdade} Pessoas")