

kg_colhidos = []
preco_por_kg = []
valor_por_arvore = []

print("Produção por árvore (kg):")
for i in range(5):
    kg = float(input(f"Digite os kg colhidos da árvore {i + 1}: "))
    kg_colhidos.append(kg)

print("\nPreço por kg:")
for i in range(5):
    preco = float(input(f"Digite o preço por kg da árvore {i + 1} (R$): "))
    preco_por_kg.append(preco)

for i in range(5):
    valor = kg_colhidos[i] * preco_por_kg[i]
    valor_por_arvore.append(valor)

print("\nKg colhidos:", kg_colhidos)
print("Preço por kg:", preco_por_kg)
print("Valor obtido por árvore:")

for i in range(5):
    print(f"Árvore {i + 1}: R$ {valor_por_arvore[i]:.2f}")
