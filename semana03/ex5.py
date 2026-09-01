opcao = int(input("Digite a opção do kit (1, 2 ou 3): "))
valor_entregue = float(input("Digite o valor entregue: R$ "))

if opcao == 1:
    kit = "Kit Básico"
    valor = 100.00

elif opcao == 2:
    kit = "Kit Plus"
    valor = 120.00

elif opcao == 3:
    kit = "Kit Premium"
    valor = 150.00

else:
    print("Opção de kit inválida!")
    valor = 0

if opcao >= 1 and opcao <= 3:
    if valor_entregue >= valor:
        troco = valor_entregue - valor

        print(f"\nCategoria: {kit}")
        print(f"Valor do kit: R$ {valor:.2f}")
        print(f"Troco: R$ {troco:.2f}")
        print("Valor suficiente!")

    else:
        falta = valor - valor_entregue

        print("\nValor insuficiente!")
        print(f"Falta: R$ {falta:.2f}")
