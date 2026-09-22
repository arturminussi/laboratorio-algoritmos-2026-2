elevador_a = 0
elevador_b = 0
elevador_c = 0

for i in range(10):
    elevador = input("Qual elevador você utiliza com mais frequência (A, B ou C)? ").upper()

    while elevador != "A" and elevador != "B" and elevador != "C":
        print("Elevador inválido!")
        elevador = input("Digite A, B ou C: ").upper()

    if elevador == "A":
        elevador_a += 1
    elif elevador == "B":
        elevador_b += 1
    else:
        elevador_c += 1

print("\nResultados:")
print("Elevador A:", elevador_a, "pessoas -", (elevador_a / 10) * 100, "%")
print("Elevador B:", elevador_b, "pessoas -", (elevador_b / 10) * 100, "%")
print("Elevador C:", elevador_c, "pessoas -", (elevador_c / 10) * 100, "%")
