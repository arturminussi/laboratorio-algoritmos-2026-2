numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

print("Números pares no intervalo:")

for numero in range(numero1, numero2 + 1):
    if numero % 2 == 0:
        print(numero)
