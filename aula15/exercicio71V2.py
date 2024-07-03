total = int(input('digite um valor inteiro: '))
for i in (50, 20, 10, 1):
    tced = 0
    while total >= i:
        total -= i
        tced += 1
    if tced != 0:
         print(f"Total de {tced} cédulas de R${i}")
        
