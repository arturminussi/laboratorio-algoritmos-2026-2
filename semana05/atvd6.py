contador = 0

for i in range(10):
    temperatura = float(input("Digite a temperatura da cidade: "))

    if temperatura >= 15 and temperatura <= 25:
        contador = contador + 1

print("Quantidade de cidades entre 15 °C e 25 °C:", contador)
