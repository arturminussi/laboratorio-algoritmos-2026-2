numero = int(input("Digite um número inteiro positivo: "))

while numero < 0:
    print("Valor inválido! Digite um número positivo.")
    numero = int(input("Digite um número inteiro positivo: "))

while numero >= 0:
    print(numero)
    numero = numero - 1
