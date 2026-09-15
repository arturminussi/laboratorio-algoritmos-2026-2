preco = 18.90

print("Ervateira Recanto – Tabela de Preços")

for quantidade in range(1, 31):
    total = quantidade * preco
    print(f"{quantidade} pacote(s) – R$ {total:.2f}")
