
colheitas = []

for i in range(5):
    kg = int(input(f"Digite a quantidade de azeitonas da colheita {i + 1} (kg): "))
    colheitas.append(kg)

soma = sum(colheitas)
media = soma / 5

print("\nQuantidades colhidas:", colheitas)
print("Soma total da safra:", soma, "kg")
print("Média por colheita:", media, "kg")
