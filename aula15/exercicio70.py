precoProdutos = []
nomeProdutos  = []
produtosMais100 = 0
while True:
    nomeProduto = str(input("Digite o nome do produto: "))
    precoProduto = float(input("Digite o preço do produto: "))
    nomeProdutos.append(nomeProduto)
    precoProdutos.append(precoProduto)

    soma = sum(precoProdutos)
    produtoMaisBarato = nomeProdutos[precoProdutos.index(min(precoProdutos))]
    if precoProduto > 1000:
        produtosMais100+=1



    opcao = str(input("Deseja continuar? [S/N]: ")).upper()
    if opcao == 'S':
        continue
    else:
        break

print(f"Total da compra: R${soma:.2f}")
print(f"Quantidade de produtos que custam mais de mil reais: {produtosMais100}")
print(f"Produto mais barato: {produtoMaisBarato}")