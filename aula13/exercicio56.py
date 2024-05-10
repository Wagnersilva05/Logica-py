somaIdade = 0
idadeMulher = 0
maiorIdadeHomem = 0
totMulher = 0

for i in range (1, 5):
    print(f'----- {i}º PESSOA -----')
    nome = str(input(f" Nome: ")).strip()
    idade = int(input(f" Idade: "))
    sexo = str(input(f" Sexo [M/F]: ")).strip()
    somaIdade += idade

    if(i == 1 and sexo in 'Mm'):
        maiorIdadeHomem = idade
        nomeVelho = nome

    if(sexo in'Mm' and idade > maiorIdadeHomem):
        maiorIdadeHomem = idade
        nomeVelho = nome

    if(sexo in 'Ff' and idade < 20):
        totMulher += 1

media = somaIdade / 4
print("\n====EXIBINDO RESULTADOS====\n")
print(f'Média das idades: {media} anos')
print(f"O homem mais velho tem {maiorIdadeHomem} anos e se chama {nomeVelho}")
print(f"Quantidade de mulheres com menos de 20 anos: {totMulher}")
