expresso = 0
cappuccino = 0
cha = 0

for i in range(10):
    voto = input("Digite sua opção (A - Expresso, B - Cappuccino, C - Chá): ")

    if voto == "A":
        expresso = expresso + 1
    else:
        if voto == "B":
            cappuccino = cappuccino + 1
        else:
            if voto == "C":
                cha = cha + 1

porcentagem_expresso = (expresso / 10) * 100
porcentagem_cappuccino = (cappuccino / 10) * 100
porcentagem_cha = (cha / 10) * 100

print("\n--- RESULTADO ---")
print("Café Expresso:", expresso, "votos -", porcentagem_expresso, "%")
print("Cappuccino:", cappuccino, "votos -", porcentagem_cappuccino, "%")
print("Chá:", cha, "votos -", porcentagem_cha, "%")
