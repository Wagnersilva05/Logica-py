produto = float(input("Digite o valor do produto: "))
pagamento = str(input("Digite a forma de pagamento: ")).strip().lower()

if(pagamento == 'dinheiro' or pagamento == 'cheque'):
    desconto = produto - (produto * 10 / 100)
    print(f"O pagamento foi a vista, o valor com 10% de desconto será R${desconto}")
    
elif(pagamento == 'cartao'):
    parcela = int(input("Quantas parcelas? "))

    if(parcela >= 3):
        juros = produto + (produto * 20 / 100)
        print(f"Parcelado no cartão {parcela} vezes, com o juros de 20% , o produto vai estar no valor de R${juros}")
    else:
        desconto = produto - (produto * 5 / 100)
        print(f"Pagamento no a vista no cartão, com o desconto de 5%, o valor do produto será R${desconto}")

else:
    print("Forma de pagamento inválida! Tente novamente.")