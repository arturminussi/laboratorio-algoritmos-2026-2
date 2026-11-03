
producao = []

for i in range(5):
    valor = float(input(f"Digite a produção de azeitonas da colheita {i + 1} (kg): "))
    producao.append(valor)

print("\nProduções na ordem inversa:")

for i in range(4, -1, -1):
    print(producao[i], "kg")
