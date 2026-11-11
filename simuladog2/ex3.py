def menu():
    print("\n===== MENU =====")
    print("1 - Inserir total de venda em um dia específico")
    print("2 - Apresentar valores registrados")
    print("3 - Apresentar média e maior valor do mês")
    print("4 - Alterar valor de um dia")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))
    return opcao


def inserir_venda(vetor):
    if len(vetor) < 30:
        dia = int(input("Digite o dia de novembro (1 a 30): "))

        if dia >= 1 and dia <= 30:
            valor = float(input("Digite o total de vendas do dia: "))

            if len(vetor) < dia:
                vetor.append(valor)
                print("Venda registrada com sucesso!")
            else:
                vetor[dia - 1] = valor
                print("Venda registrada com sucesso!")
        else:
            print("Dia inválido!")
    else:
        print("Todos os 30 dias já possuem valores registrados!")


def apresentar_valores(vetor):
    if len(vetor) == 0:
        print("Nenhum valor registrado!")
    else:
        print("\nValores registrados:")
        for i in range(len(vetor)):
            print("Dia", i + 1, ":", vetor[i])


def apresentar_media_maior(vetor):
    if len(vetor) == 0:
        print("Nenhuma venda registrada!")
    else:
        media = sum(vetor) / len(vetor)
        maior = max(vetor)

        print("Média de vendas:", media)
        print("Maior valor de venda:", maior)


def alterar_valor(vetor):
    if len(vetor) == 0:
        print("Nenhuma venda registrada!")
    else:
        dia = int(input("Digite o dia que deseja alterar (1 a 30): "))

        if dia >= 1 and dia <= len(vetor):
            novo_valor = float(input("Digite o novo valor de venda: "))
            vetor[dia - 1] = novo_valor
            print("Valor alterado com sucesso!")
        else:
            print("Dia inválido ou sem valor registrado!")


def main():
    vetor = []

    while True:
        opcao = menu()

        if opcao == 1:
            inserir_venda(vetor)

        elif opcao == 2:
            apresentar_valores(vetor)

        elif opcao == 3:
            apresentar_media_maior(vetor)

        elif opcao == 4:
            alterar_valor(vetor)

        elif opcao == 5:
            print("Programa encerrado!")
            break

        else:
            print("Opção inválida!")


main()
