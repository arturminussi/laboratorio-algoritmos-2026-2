quantidade = int(input("Digite a quantidade de pacotes: "))

preco = 20.00
valor_original = quantidade * preco

if quantidade <= 5:
    desconto = 0
elif quantidade <= 10:
    desconto = 5
elif quantidade <= 20:
    desconto = 10
else:
    desconto = 15

valor_desconto = valor_original * desconto / 100
valor_final = valor_original - valor_desconto

print(f"Valor original: R$ {valor_original:.2f}")
print(f"Desconto: {desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")
