producao = []

for dia in range(1, 8):
    kg = float(input("Digite a quantidade produzida no dia " + str(dia) + ": "))
    producao.append(kg)

total = sum(producao)
maior = max(producao)
menor = min(producao)

dia_maior = producao.index(maior) + 1
dia_menor = producao.index(menor) + 1

media = total / 7

print("\n--- RESULTADO ---")
print("Total produzido na semana:", total, "kg")
print("Maior produção: Dia", dia_maior, "-", maior, "kg")
print("Menor produção: Dia", dia_menor, "-", menor, "kg")
print("Média diária:", media, "kg")
