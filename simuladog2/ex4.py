def somaValor(valor):
    valor = valor + 1
    print(valor)


def main():
    dado = 5

    for i in range(0, 15):
        somaValor(dado)

    print(dado)


main()
