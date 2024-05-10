velocidade = int(input("Digite quantos KM o carro está: "))

limiteVelocidade = 80

if(velocidade > limiteVelocidade):

    kmAcima = velocidade - limiteVelocidade
    multa = 7 * kmAcima

    print(f"Sua multa será de R${multa}.")
else:
    print("você está dentro do limite de velocidade.") 