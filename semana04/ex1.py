
nome = input("Digite o nome do treinador: ")
salario = float(input("Digite o salário atual: R$ "))
tempo = int(input("Digite o tempo de serviço em anos: "))

if tempo >= 5 and salario <= 2000:
    aumento = salario * 0.10
else:
    aumento = salario * 0.05

novo_salario = salario + aumento

print("\n--- Dados do treinador ---")
print(f"Nome: {nome}")
print(f"Aumento concedido: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")
