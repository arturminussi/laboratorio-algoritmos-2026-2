
producao = []

for i in range(5):
    kg = int(input(f"Digite a produção da árvore {i + 1} (kg): "))
    producao.append(kg)

maior = max(producao)
menor = min(producao)

print("\nProduções por árvore:", producao)

print("\nMaior produção:", maior, "kg")
for i in range(5):
    if producao[i] == maior:
        print("Árvore:", i + 1, "- Índice:", i)

print("\nMenor produção:", menor, "kg")
for i in range(5):
    if producao[i] == menor:
        print("Árvore:", i + 1, "- Índice:", i)
