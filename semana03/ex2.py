valor = float(input("Digite o valor da inscrição: R$ "))
opcao = int(input("Escolha a forma de pagamento (1 - À vista | 2 - 2x | 3 - 3x): "))

if opcao == 1:
    print(f"Pagamento à vista: R$ {valor:.2f}")

elif opcao == 2:
    parcela = valor / 2
    print(f"Valor de cada parcela: R$ {parcela:.2f}")

elif opcao == 3:
    parcela = valor / 3
    print(f"Valor de cada parcela: R$ {parcela:.2f}")

else:
    print("Opção de pagamento inválida!")
