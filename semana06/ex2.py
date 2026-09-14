pacotes = int(input("Digite a quantidade total de pacotes: "))
caixas = int(input("Digite a quantidade de caixas disponíveis: "))

por_caixa = pacotes // caixas
sobrando = pacotes % caixas

print(f"\nPacotes em cada caixa: {por_caixa}")
print(f"Pacotes que irão sobrar: {sobrando}")
