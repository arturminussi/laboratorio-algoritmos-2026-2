import random

lotes = []

for i in range(10):
    id_lote = random.randint(1, 100)
    lotes.append(id_lote)

print("IDs dos lotes:", lotes)

print("\nIDs pares:")
for id_lote in lotes:
    if id_lote % 2 == 0:
        print(id_lote)
