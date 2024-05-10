km = float(input("Informe a quantidade de KM rodados: "))
dias = int(input("Informe a quantidade de dias que ele foi alugado: "))

pagos = (dias * 60) + (km * 0.15)

print(f"O total a pagar é de R${pagos:.2f}")
