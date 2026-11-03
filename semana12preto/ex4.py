
lotes = []

for i in range(6):
    kg = float(input(f"Digite a quantidade de azeitonas do lote {i + 1} (kg): "))
    lotes.append(kg)

rendimento = 0.18

print("\nLitros estimados de azeite por lote:")

for i in range(6):
    litros = lotes[i] * rendimento
    print(f"Lote {i + 1}: {litros:.2f} litros")
