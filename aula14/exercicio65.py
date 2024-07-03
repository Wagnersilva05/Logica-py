r = 'S'
soma = 0
contador = 0
ns = []
while r  == 'S':
    n = int(input("Digite um número: "))
    ns.append(n)
    soma+=n
    contador+=1
    maior = max(ns)
    menor = min(ns)

    r = str(input("Dejesa continuar? [S/N]: ")).upper()
    
media = soma / contador

print(f'Média: {media:.1f}')
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')