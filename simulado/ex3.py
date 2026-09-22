gasolina = 0
diesel = 0

while True:
    print("\n===== POSTO DE GASOLINA =====")
    print("1. Vender combustível")
    print("2. Sair")

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        print("\n===== COMBUSTÍVEIS =====")
        print("1. Gasolina - R$ 6,89")
        print("2. Diesel   - R$ 4,80")

        combustivel = int(input("Escolha o combustível: "))

        while combustivel != 1 and combustivel != 2:
            print("Erro! Opção de combustível inválida.")
            combustivel = int(input("Escolha o combustível: "))

        litros = float(input("Digite o total de litros abastecidos: "))

        if combustivel == 1:
            preco = 6.89
            gasolina += litros
        else:
            preco = 4.80
            diesel += litros

        valor = litros * preco

        print("Valor do abastecimento: R$", round(valor, 2))

        pago = float(input("Digite o valor pago: R$ "))

        if pago >= valor:
            troco = pago - valor
            print("Troco: R$", round(troco, 2))
        else:
            falta = valor - pago
            print("Valor que falta para pagar: R$", round(falta, 2))

    elif opcao == 2:
        print("\n===== TOTAL VENDIDO =====")
        print("Total de gasolina vendido:", gasolina, "litros")
        print("Total de diesel vendido:", diesel, "litros")
        break

    else:
        print("Erro! Opção inválida.")
