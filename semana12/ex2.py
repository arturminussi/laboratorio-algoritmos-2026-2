
fazenda_a = []
fazenda_b = []
producao_total = []

print("Produção da Fazenda A:")
for i in range(5):
    valor = int(input(f"Digite a produção do lote {i + 1} (kg): "))
    fazenda_a.append(valor)

print("\nProdução da Fazenda B:")
for i in range(5):
    valor = int(input(f"Digite a produção do lote {i + 1} (kg): "))
    fazenda_b.append(valor)

for i in range(5):
    soma = fazenda_a[i] + fazenda_b[i]
    producao_total.append(soma)

print("\nProdução da Fazenda A:", fazenda_a)
print("Produção da Fazenda B:", fazenda_b)
print("Produção total por lote:", producao_total)
