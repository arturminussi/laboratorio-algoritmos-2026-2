import random

lotes = []

for i in range(10):
    id_lote = random.randint(1, 50)
    lotes.append(id_lote)

pares = 0
impares = 0

for id_lote in lotes:
    if id_lote % 2 == 0:
        pares += 1
    else:
        impares += 1

print("IDs dos lotes:", lotes)
print("Quantidade de IDs pares:", pares)
print("Quantidade de IDs ímpares:", impares)
