vetor = []

while True:
    print("\n===== MENU =====")
    print("1 - Inserir item")
    print("2 - Retirar item")
    print("3 - Listar itens")
    print("4 - Retirar todos os itens")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        item = input("Digite o item que deseja inserir: ")
        vetor.append(item)
        print("Item inserido com sucesso!")

    elif opcao == 2:
        if len(vetor) > 0:
            item = input("Digite o item que deseja retirar: ")

            if item in vetor:
                vetor.remove(item)
                print("Item retirado com sucesso!")
            else:
                print("Item não encontrado no vetor.")
        else:
            print("O vetor está vazio!")

    elif opcao == 3:
        if len(vetor) > 0:
            print("\nItens do vetor:")
            for item in vetor:
                print(item)
        else:
            print("O vetor está vazio!")

    elif opcao == 4:
        vetor.clear()
        print("Todos os itens foram retirados!")

    elif opcao == 5:
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida! Tente novamente.")
