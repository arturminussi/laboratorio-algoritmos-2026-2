def somaImposto(taxaImposto, custo):
    custo = custo + (custo * taxaImposto / 100)
    return custo


taxa = float(input("Digite a taxa de imposto (%): "))
valor = float(input("Digite o custo do item: "))

valor_final = somaImposto(taxa, valor)

print(f"Valor do item com imposto: R$ {valor_final:.2f}")
