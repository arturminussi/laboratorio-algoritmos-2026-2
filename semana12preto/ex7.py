
lotes = []

for i in range(5):
    codigo = int(input(f"Digite o código do lote {i + 1}: "))
    lotes.append(codigo)

if len(lotes) == len(set(lotes)):
    print("Distintos")
else:
    print("Há duplicatas")
