
lotes = []

while True:
    print("\n===== MENU DE GERENCIAMENTO DE LOTES =====")
    print("1) Inserir lote")
    print("2) Listar lotes")
    print("3) Retirar um lote")
    print("4) Limpar todos os lotes")
    print("5) Contar lotes com produção maior que X")
    print("6) Verificar se um código está presente")
    print("7) Encontrar maior e menor código")
    print("8) Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        codigo = int(input("Digite o código do lote (par): "))

        if codigo % 2 == 0:
            lotes.append(codigo)
            print("Lote inserido com sucesso!")
        else:
            print("ERRO: somente códigos pares são permitidos!")

    elif opcao == 2:
        if len(lotes) > 0:
            print("Lotes cadastrados:")
            for lote in lotes:
                print(lote)
        else:
            print("Não há lotes cadastrados.")

    elif opcao == 3:
        codigo = int(input("Digite o código do lote que deseja retirar: "))

        if codigo in lotes:
            lotes.remove(codigo)
            print("Lote retirado com sucesso!")
        else:
            print("Lote não encontrado.")

    elif opcao == 4:
        lotes.clear()
        print("Todos os lotes foram removidos.")

    elif opcao == 5:
        x = int(input("Digite o valor de X: "))
        contador = 0

        for lote in lotes:
            if lote > x:
                contador += 1

        print("Quantidade de lotes maiores que X:", contador)

    elif opcao == 6:
        codigo = int(input("Digite o código que deseja procurar: "))

        if codigo in lotes:
            print("Código encontrado!")
        else:
            print("Código não encontrado.")

    elif opcao == 7:
        if len(lotes) > 0:
            print("Maior código:", max(lotes))
            print("Menor código:", min(lotes))
        else:
            print("Não há lotes cadastrados.")

    elif opcao == 8:
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida! Tente novamente.")
