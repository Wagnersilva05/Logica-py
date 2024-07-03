soma = 0
contador = 0

while True:
    n = int(input("Digite um número (Digite 999 para parar.) "))
    if(n == 999):
        break
    soma+=n
    contador+=1
    
print(f'Foram digitados {contador} números')
print(f'Soma: {soma}')
