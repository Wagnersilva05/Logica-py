from random import randint
vitorias = 0
while True:
    jogador = int(input("Digite um valor: "))

    computador = randint(0, 10)
    somaJogo = jogador + computador
    escolhaJogador = ' '

    while escolhaJogador not in 'IP':
        escolhaJogador = str(input("Você quer par ou ímpar? [P/I] ")).strip().upper()[0]
        print(f"Você jogou {jogador} e o computador {computador}. Total de {somaJogo}")
    if escolhaJogador == 'P':
        if somaJogo % 2 == 0:
            print("Você venceu!")
            vitorias+=1
        else:
            print('Você Perdeu!')
            break    
    elif escolhaJogador == 'I':
        if somaJogo % 2 == 1:
            print("Você venceu!")
            vitorias+=1
        else:
            print('Você Perdeu!')
            break
    print('Vamos jogar novamente...')
print(f"GAME OVER! VOCÊ VENCEU {vitorias} VEZES.")