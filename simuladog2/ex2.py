vetor = []

for i in range(30):
    numero = int(input(f"Digite o {i+1}º número: "))

    if numero % 4 == 0:
        vetor.append(numero)
    else:
        print("ERRO! O número não é múltiplo de 4. Será inserido o número 4.")
        vetor.append(4)

print("\nVetor preenchido:")
print(vetor)
