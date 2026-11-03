
lotes = []

for i in range(10):
    codigo = int(input(f"Digite o código do lote {i + 1}: "))
    lotes.append(codigo)

print("\nLotes em ordem inversa:")

for i in range(len(lotes) - 1, -1, -1):
    print(lotes[i])
