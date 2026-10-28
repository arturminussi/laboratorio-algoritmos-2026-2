vetor = []
quantidade = 0
soma_maiores_30 = 0
soma_total = 0

for i in range(8):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    vetor.append(numero)

for numero in vetor:
    soma_total += numero

    if numero > 30:
        quantidade += 1
        soma_maiores_30 += numero

print("\nValores do vetor:", vetor)
print("Quantidade de números maiores que 30:", quantidade)
print("Soma dos números maiores que 30:", soma_maiores_30)
print("Soma de todos os números:", soma_total)
