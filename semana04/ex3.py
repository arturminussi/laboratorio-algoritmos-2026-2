
litros = float(input("Digite a quantidade de litros abastecidos: "))
valor = float(input("Digite o valor total: R$ "))

if litros >= 20 and valor > 100:
    desconto = valor * 0.10

elif litros >= 20 and valor <= 100:
    desconto = valor * 0.05

else:
    desconto = 0

valor_final = valor - desconto

print("\n--- Resultado ---")
print(f"Desconto aplicado: R$ {desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")
