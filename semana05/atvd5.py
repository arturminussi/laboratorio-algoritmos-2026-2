maiores = 0

for i in range(10):
    idade = int(input("Digite a idade: "))

    if idade >= 18:
        maiores = maiores + 1

print("Quantidade de pessoas com 18 anos ou mais:", maiores)
