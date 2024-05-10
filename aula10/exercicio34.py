salario = float(input("Digite o salário: "))

if(salario > 1250):
    aumento = salario + (salario * 10 / 100)
    
    print(f"Com o aumento de 10%, seu salario é de R${aumento:.2f}")
else:
    aumento = salario  + (salario * 15 / 100)

    print(f"Com o aumento de 15%, seu salário é de R${aumento:.2f}")