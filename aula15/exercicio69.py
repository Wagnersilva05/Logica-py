from time import sleep
from os import system
contadorMaiorIdade = 0
contadorHomens = 0
mulheresMenosDe20 = 0
while True:
    idade = int(input("Idade: "))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input("Sexo [M/F]: ")).upper()



    if idade >= 18:
        contadorMaiorIdade+=1
    if sexo == 'M':
        contadorHomens+=1
    elif sexo == 'F' and idade < 20:
        mulheresMenosDe20+=1
    
    opcao = str(input("Deseja continuar? [S/N]: ")).upper()
    if opcao == 'S':
        continue
    else:
        break
print(f"Maiores de idade: {contadorMaiorIdade}")
print(f"Quantidade de homens cadastrados: {contadorHomens}")
print(f"Quantidade de mulheres ccom menos de 20 anos: {mulheresMenosDe20}")