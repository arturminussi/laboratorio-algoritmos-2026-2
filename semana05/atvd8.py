caixa = float(input("Digite o dinheiro atual em caixa: R$ "))

while True:
    print("\n--- CAIXA DA LOJA ---")
    print("1 - Realizar venda")
    print("2 - Retirar dinheiro")
    print("3 - Dinheiro em caixa")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Digite o valor da venda: R$ "))
        caixa = caixa + valor
        print("Venda realizada com sucesso!")

    else:
        if opcao == "2":
            valor = float(input("Digite o valor a retirar: R$ "))

            if valor <= caixa:
                caixa = caixa - valor
                print("Retirada realizada com sucesso!")
            else:
                print("Não há dinheiro suficiente em caixa.")

        else:
            if opcao == "3":
                print("Dinheiro em caixa: R$", caixa)

            else:
                if opcao == "4":
                    print("Caixa encerrado.")
                    break

                else:
                    print("Opção inválida.")
