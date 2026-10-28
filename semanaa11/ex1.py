valores = []

for i in range(10):
    numero = int(input(f"Digite o {i + 1}º valor: "))
    valores.append(numero)

maiores = []

for numero in valores:
    if numero > 100:
        maiores.append(numero)

print("Valores digitados:", valores)
print("Quantidade de valores maiores que 100:", len(maiores))
print("Valores maiores que 100:", maiores)
