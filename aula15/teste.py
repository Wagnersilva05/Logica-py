'''lista = [10, 20, 30, 40, 50]
menor = min(lista)
indice = lista.index(menor)  # Aqui, `indice` será 2
print(indice)'''

nomeProdutos = ["Produto A", "Produto B", "Produto C"]
precoProdutos = [100, 50, 75]

# Passo a passo do código
menor_preco = min(precoProdutos)  # menor_preco será 50
indice_menor_preco = precoProdutos.index(menor_preco)  # indice_menor_preco será 1
produtoMaisBarato = nomeProdutos[indice_menor_preco]  # produtoMaisBarato será "Produto B"

print(produtoMaisBarato)