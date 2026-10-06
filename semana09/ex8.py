dentro = 0
fora = 0

for i in range(10):
    numero = int(input("Digite um número: "))

    if 10 <= numero <= 20:
        dentro += 1
    else:
        fora += 1

print("Quantidade de números no intervalo [10,20]:", dentro)
print("Quantidade de números fora do intervalo:", fora)
