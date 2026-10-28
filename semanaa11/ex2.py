valores = []

for i in range(10):
    numero = int(input(f"Digite o {i + 1}º valor: "))
    valores.append(numero)

print("\nValores pares e suas posições:")

for i in range(10):
    if valores[i] % 2 == 0:
        print(f"Valor: {valores[i]} - Posição: {i}")
