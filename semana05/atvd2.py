contador = 0

codigo = int(input("Digite o código do brinquedo (0 para encerrar): "))

while codigo != 0:
    if codigo == 1040:
        contador = contador + 1

    codigo = int(input("Digite o código do brinquedo (0 para encerrar): "))

print("O código 1040 foi digitado", contador, "vezes.")
