nome = input("Digite o nome do cliente: ")


valor = float(input("Digite o valor da compra: R$ "))


pagamento = input("Digite a forma de pagamento (1 - Dinheiro / 2 - Cartão): ")


if valor > 200:
    if pagamento == "1":
        desconto = valor * 0.15
    else:
        desconto = valor * 0.05
else:
    if pagamento == "1":
        desconto = valor * 0.10
    else:
        desconto = 0


valor_final = valor - desconto


print("Cliente:", nome)
print("Valor original:", valor)
print("Valor final:", valor_final)
