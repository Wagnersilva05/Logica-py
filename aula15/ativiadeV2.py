from time import sleep

subTotal = 0
pratoDesejado = False
pratosSelecionados = []

while True:
    print("====MENU===")
    print('''Opção 1 - LASANHA - R$25,00
    Opção 2 - PIZZA - R$15,00
    Opção 3 - MACARRONADA - R$22,00
    Opção 4 - FEIJOADA - R$20,00
    Opção 5 - BIFE ACEBOLADO - R$10,00
    Opção 6 - PICANHA - R$40,00
    Opção 7 - CHURRASCO - R$35,00
    Opção 0 - SAIR''')
    opcao = int(input("Escolha a opção desejada: "))

    match opcao:
        case 1:
            subTotal += 25
            print("Opção 1 - LASANHA - R$25,00")
            pratosSelecionados.append("LASANHA - R$25,00")
            pratoDesejado = True
            sleep(2)
        case 2:
            subTotal += 15
            print("Opção 2 - PIZZA - R$15,00")
            pratosSelecionados.append("PIZZA - R$15,00")
            pratoDesejado = True
            sleep(2)
        case 3:
            subTotal += 22
            print("Opção 3 - MACARRONADA - R$22,00")
            pratosSelecionados.append("MACARRONADA - R$22,00")
            pratoDesejado = True
            sleep(2)
        case 4:
            subTotal += 20
            print("Opção 4 - FEIJOADA - R$20,00")
            pratosSelecionados.append("FEIJOADA - R$20,00")
            pratoDesejado = True
            sleep(2)
        case 5:
            subTotal += 10
            print("Opção 5 - BIFE ACEBOLADO - R$10,00")
            pratosSelecionados.append("BIFE ACEBOLADO - R$10,00")
            pratoDesejado = True
            sleep(2)
        case 6:
            subTotal += 40
            print("Opção 6 - PICANHA - R$40,00")
            pratosSelecionados.append("PICANHA - R$40,00")
            pratoDesejado = True
            sleep(2)
        case 7:
            subTotal += 35
            print("Opção 7 - CHURRASCO - R$35,00")
            pratosSelecionados.append("CHURRASCO - R$35,00")
            pratoDesejado = True
            sleep(2)
        case 0:
            if not pratoDesejado:
                print("Nenhum prato foi selecionado.")
                break

            while True:
                formaPagamento = str(input('''Forma de pagamento: C - Cartão de crédito
                    \tD - À vista: ''')).upper()

                if formaPagamento == 'D':
                    desconto = subTotal * 0.10
                    totalAPagar = subTotal - desconto
                    print("Pratos selecionados: ")
                    for prato in pratosSelecionados:
                        print(prato)
                    print(f"\nSubtotal: R$ {subTotal:.2f}")
                    print(f"Desconto: R$ {desconto:.2f}")
                    print(f"Total a pagar: R$ {totalAPagar:.2f}")
                    break
                elif formaPagamento == 'C':
                    acrescimo = subTotal * 0.10
                    totalAPagar = subTotal + acrescimo
                    print("Pratos selecionados: ")
                    for prato in pratosSelecionados:
                        print(prato)
                    print(f"\nSubtotal: R$ {subTotal:.2f}")
                    print(f"Acréscimo: R$ {acrescimo:.2f}")
                    print(f"Total a pagar: R$ {totalAPagar:.2f}")
                    break
                else:
                    input("Forma de pagamento inválida, tente novamente.")
            break
        case _:
            print("Opção inválida. Tente novamente.")
            sleep(2)
