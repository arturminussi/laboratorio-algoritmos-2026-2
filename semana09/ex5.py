
maior_idade = 0

olhos_azuis = 0
olhos_verdes = 0
olhos_castanhos = 0

cabelos_loiros = 0
cabelos_castanhos = 0
cabelos_pretos = 0

masculino = 0
feminino = 0

verdes_pretos_18_35 = 0


for i in range(15):
    print("\nPessoa", i + 1)

    sexo = input("Digite o sexo (M/F): ").upper()
    olhos = input("Digite a cor dos olhos (A/V/C): ").upper()
    cabelos = input("Digite a cor dos cabelos (L/C/P): ").upper()
    idade = int(input("Digite a idade: "))

  
    if idade > maior_idade:
        maior_idade = idade

  
    if sexo == "M":
        masculino += 1
    elif sexo == "F":
        feminino += 1

  
    if olhos == "A":
        olhos_azuis += 1
    elif olhos == "V":
        olhos_verdes += 1
    elif olhos == "C":
        olhos_castanhos += 1

  
    if cabelos == "L":
        cabelos_loiros += 1
    elif cabelos == "C":
        cabelos_castanhos += 1
    elif cabelos == "P":
        cabelos_pretos += 1

  
    if 18 <= idade <= 35 and olhos == "V" and cabelos == "P":
        verdes_pretos_18_35 += 1

porcentagem_azuis = (olhos_azuis / 15) * 100
porcentagem_verdes = (olhos_verdes / 15) * 100
porcentagem_castanhos_olhos = (olhos_castanhos / 15) * 100

porcentagem_loiros = (cabelos_loiros / 15) * 100
porcentagem_castanhos_cabelos = (cabelos_castanhos / 15) * 100
porcentagem_pretos = (cabelos_pretos / 15) * 100

porcentagem_masculino = (masculino / 15) * 100
porcentagem_feminino = (feminino / 15) * 100


print("\n===== RESULTADOS =====")

print("Maior idade do grupo:", maior_idade)

print(
    "Quantidade de pessoas entre 18 e 35 anos, "
    "com olhos verdes e cabelos pretos:",
    verdes_pretos_18_35
)

print("\nPorcentagem por cor dos olhos:")
print("Olhos azuis:", porcentagem_azuis, "%")
print("Olhos verdes:", porcentagem_verdes, "%")
print("Olhos castanhos:", porcentagem_castanhos_olhos, "%")

print("\nPorcentagem por cor dos cabelos:")
print("Cabelos loiros:", porcentagem_loiros, "%")
print("Cabelos castanhos:", porcentagem_castanhos_cabelos, "%")
print("Cabelos pretos:", porcentagem_pretos, "%")

print("\nPorcentagem por sexo:")
print("Masculino:", porcentagem_masculino, "%")
print("Feminino:", porcentagem_feminino, "%")
