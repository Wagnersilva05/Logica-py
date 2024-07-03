soma = 0
contador = 0

n = int(input("Digite um número: "))

while n != 999:
    soma+=n
    contador+=1
    n = int(input("Digite um número: "))
    
print(f'Foram digitados {contador} números')
print(f'Soma: {soma}')

