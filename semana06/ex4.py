soma = 0
maior = 0
menor = 999
todos_os_dias = 0

for i in range(20):
    vezes = int(input(f"Quantas vezes por semana a pessoa {i + 1} toma chimarrão? "))

    soma += vezes

    if vezes > maior:
        maior = vezes

    if vezes < menor:
        menor = vezes

    if vezes >= 7:
        todos_os_dias += 1

media = soma / 20

print("\n--- RESULTADO ---")
print(f"Média de vezes por semana: {media:.2f}")
print(f"Maior quantidade: {maior}")
print(f"Menor quantidade: {menor}")
print(f"Pessoas que tomam todos os dias: {todos_os_dias}")
