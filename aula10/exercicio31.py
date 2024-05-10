distancia = int(input("Digite a distância da viagem: "))

if(distancia <= 200):
    passagemPorKm = 0.50
    precoPassagem = passagemPorKm * distancia

    print(f"O preço da passagem séra de R${precoPassagem:.2f}")
else:
    passagemPorKm = 0.45
    precoPassagem = passagemPorKm * distancia

    print(f"O preço da passagem será de R${precoPassagem:.2f}")   
