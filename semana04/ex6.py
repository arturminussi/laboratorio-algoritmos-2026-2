morangos = float(input("Digite a quantidade de morangos em Kg: "))
macas = float(input("Digite a quantidade de maçãs em Kg: "))

if morangos <= 5:
    valor_morangos = morangos * 2.50
else:
    valor_morangos = morangos * 2.20

if macas <= 5:
    valor_macas = macas * 1.80
else:
    valor_macas = macas * 1.50

total = valor_morangos + valor_macas

if morangos + macas > 8 or total > 25:
    desconto = total * 0.10
else:
    desconto = 0

valor_final = total - desconto

print("\n--- Resultado ---")
print(f"Valor dos morangos: R$ {valor_morangos:.2f}")
print(f"Valor das maçãs: R$ {valor_macas:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {valor_final:.2f}")
