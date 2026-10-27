saldo = 0.0

def mostrar_menu():
    print("\n===== MENU =====")
    print("1 - Sacar dinheiro")
    print("2 - Depositar dinheiro")
    print("3 - Mostrar saldo")
    print("4 - Sair")


def sacar():
    global saldo
    valor = float(input("Digite o valor do saque: "))

    if valor > 0 and valor <= saldo:
        saldo -= valor
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente ou valor inválido!")


def depositar():
    global saldo
    valor = float(input("Digite o valor do depósito: "))

    if valor > 0:
        saldo += valor
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido!")


def mostrar_saldo():
    print(f"Saldo atual: R$ {saldo:.2f}")


opcao = 0

while opcao != 4:
    mostrar_menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        sacar()
    elif opcao == 2:
        depositar()
    elif opcao == 3:
        mostrar_saldo()
    elif opcao == 4:
        print("Obrigado por utilizar o sistema!")
    else:
        print("Opção inválida! Tente novamente.")
