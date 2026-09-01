valor = float(input("Digite o valor do ingresso: R$ "))

print("\nEscolha o tipo de ingresso:")
print("1 - Normal")
print("2 - Estudante")
print("3 - Criança até 12 anos")
print("4 - Idoso")

opcao = int(input("Digite a opção: "))

if opcao == 1:
    valor_final = valor

elif opcao == 2:
    valor_final = valor * 0.50

elif opcao == 3:
    valor_final = valor * 0.40

elif opcao == 4:
    valor_final = valor * 0.60

else:
    print("Opção inválida!")
    valor_final = 0

if opcao >= 1 and opcao <= 4:
    print(f"Valor a pagar: R$ {valor_final:.2f}")
