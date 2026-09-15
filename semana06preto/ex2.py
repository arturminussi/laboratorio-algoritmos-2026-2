chimarroes = int(input("Quantos chimarrões você prepara por dia? "))

consumo_diario = chimarroes * 40
consumo_mensal = consumo_diario * 30

print("Consumo mensal:", consumo_mensal, "gramas")

if consumo_mensal > 3000:
    print("Grande consumidor de erva-mate")
else:
    print("Consumidor moderado de erva-mate")
