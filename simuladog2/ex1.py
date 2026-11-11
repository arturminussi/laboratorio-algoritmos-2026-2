def menu():
    print("\n===== MENU =====")
    print("1 - Somar dois valores")
    print("2 - Subtrair dois valores")
    print("3 - Mostrar valores")
    print("4 - Sair")
    opcao = int(input("Escolha uma opção: "))
    return opcao


def somar(valor1, valor2):
    resultado = valor1 + valor2
    return resultado


def subtrair(valor1, valor2):
    resultado = valor1 - valor2
    return resultado


def apresentar_valores(valor1, valor2):
    print("Primeiro valor:", valor1)
    print("Segundo valor:", valor2)


def main():
    valor1 = 0
    valor2 = 0

    while True:
        opcao = menu()

        if opcao == 1:
            valor1 = float(input("Digite o primeiro valor: "))
            valor2 = float(input("Digite o segundo valor: "))
            resultado = somar(valor1, valor2)
            print("Resultado da soma:", resultado)

        elif opcao == 2:
            valor1 = float(input("Digite o primeiro valor: "))
            valor2 = float(input("Digite o segundo valor: "))
            resultado = subtrair(valor1, valor2)
            print("Resultado da subtração:", resultado)

        elif opcao == 3:
            apresentar_valores(valor1, valor2)

        elif opcao == 4:
            print("Programa encerrado!")
            break

        else:
            print("Opção inválida! Tente novamente.")


main()
