peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

pesoIdeal = peso / (altura * altura)

print(f"\nSeu IMC é {pesoIdeal:.2f}")

if(pesoIdeal < 18.5):
    print("Abaixo do peso.")
elif(pesoIdeal <= 25):
    print("Peso ideal.")
elif(pesoIdeal > 25):
    print("Sobrepeso.")
elif(pesoIdeal >= 30):
    print("Obesidade.")    
elif(pesoIdeal > 40):
    print("Obesidade mórbida")