capacidade = 100
ingressos_disponiveis = 100

while True:
    print("\n--- CONTROLE DE INGRESSOS ---")
    print("1 - Vender ingresso")
    print("2 - Adicionar ingressos extras")
    print("3 - Mostrar ingressos disponíveis")
    print("4 - Encerrar")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        quantidade = int(input("Quantos ingressos deseja vender? "))

        if quantidade <= ingressos_disponiveis:
            ingressos_disponiveis = ingressos_disponiveis - quantidade
            print("Ingresso(s) vendido(s) com sucesso!")
        else:
            print("Não há ingressos suficientes disponíveis.")

    else:
        if opcao == "2":
            quantidade = int(input("Quantos ingressos extras deseja adicionar? "))

            ingressos_disponiveis = ingressos_disponiveis + quantidade
            print("Ingressos adicionados com sucesso!")

        else:
            if opcao == "3":
                print("Ingressos disponíveis:", ingressos_disponiveis)

            else:
                if opcao == "4":
                    print("Sistema encerrado.")
                    break

                else:
                    print("Opção inválida.")
