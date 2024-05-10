valorCasa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salário: "))
pagamentoAnual = int(input("Quantos anos vai pagar a casa: "))

valorPrestacao = valorCasa / (pagamentoAnual * 12)

if(valorPrestacao > (30 / 100) * salario):
    print("Empréstimo negado! Salário baixo.")
else:
    print(f"Empréstimo aceito! O valor da prestação será de {valorPrestacao:.2f}")