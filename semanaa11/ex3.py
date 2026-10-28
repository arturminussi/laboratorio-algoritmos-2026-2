A = []
B = []

for i in range(10):
    numero = int(input(f"Digite o {i + 1}º valor: "))
    A.append(numero)

for i in range(9, -1, -1):
    B.append(A[i])

print("Vetor A:", A)
print("Vetor B em ordem inversa:", B)
