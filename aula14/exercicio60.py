n = int(input("Digite um número paa calcular o fatorial: "))
c = n
f = 1
print(f'Calculando {c}! = ', end='')

while(c > 0):
    print(f'{c}', end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')