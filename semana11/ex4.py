def calcular_compra(laranjas):
    if laranjas <= 12:
        total = laranjas * 0.40
    else:
        total = laranjas * 0.25

    return total


quantidade = int(input("Digite a quantidade de laranjas compradas: "))

valor = calcular_compra(quantidade)

print(f"Valor total da compra: R$ {valor:.2f}")
