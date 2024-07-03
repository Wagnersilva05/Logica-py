def calcular_desconto_irrf(salario_bruto, quantidade_dependentes):
    # Definindo as alíquotas e deduções conforme a faixa salarial
    # Aqui você precisa ajustar de acordo com a legislação tributária atual
    # Esses valores são apenas exemplos hipotéticos
    faixa1_aliquota = 0.1
    faixa2_aliquota = 0.15
    faixa3_aliquota = 0.20
    faixa1_deducao = 500
    faixa2_deducao = 700
    faixa3_deducao = 1000

    # Cálculo do desconto do IRRF com base no salário bruto e na quantidade de dependentes
    if salario_bruto <= 3000:
        desconto = salario_bruto * faixa1_aliquota - quantidade_dependentes * faixa1_deducao
    elif salario_bruto <= 5000:
        desconto = salario_bruto * faixa2_aliquota - quantidade_dependentes * faixa2_deducao
    else:
        desconto = salario_bruto * faixa3_aliquota - quantidade_dependentes * faixa3_deducao

    return desconto

# Solicitar informações ao usuário
salario = float(input("Digite o salário bruto do funcionário: "))
quantidade_filhos = int(input("Digite a quantidade de filhos do funcionário: "))
tem_esposa = input("O funcionário tem esposa? (S/N): ")

# Converter a resposta para maiúsculas para facilitar a comparação
tem_esposa = tem_esposa.upper()

# Definir a quantidade de dependentes com base nos filhos e na esposa (se tiver)
quantidade_dependentes = quantidade_filhos
if tem_esposa == "S":
    quantidade_dependentes += 1

# Calcular o desconto do IRRF
desconto_irrf = calcular_desconto_irrf(salario, quantidade_dependentes)
print("Desconto do IRRF:", desconto_irrf)
