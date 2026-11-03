
lotes = []

for i in range(5):
    codigo = int(input(f"Digite o código do lote {i + 1}: "))
    lotes.append(codigo)

procurar = int(input("\nDigite o código do lote que deseja verificar: "))

if procurar in lotes:
    print("Lote encontrado!")
else:
    print("Lote não encontrado!")
