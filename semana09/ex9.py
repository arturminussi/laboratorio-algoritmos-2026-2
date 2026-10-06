a = 0
b = 0
c = 0


for i in range(20):
    opiniao = input("Qual jornal você lê? (A, B ou C): ").upper()

    if opiniao == "A":
        a += 1
    elif opiniao == "B":
        b += 1
    elif opiniao == "C":
        c += 1


porcentagem_a = (a / 20) * 100
porcentagem_b = (b / 20) * 100
porcentagem_c = (c / 20) * 100


resultados = [
    ("Jornal A", porcentagem_a),
    ("Jornal B", porcentagem_b),
    ("Jornal C", porcentagem_c)
]


resultados.sort(key=lambda x: x[1])


print("\nPorcentagens em ordem crescente:")

for jornal, porcentagem in resultados:
    print(jornal, ":", porcentagem, "%")
