soma_salarios = 0
mais_novo = 0
mais_velho = 0
atacantes_ate_10000 = 0
atacantes = 0
defensores = 0

for i in range(10):
    idade = int(input("Digite a idade do jogador: "))
    posicao = input("Digite a posição (A para atacante ou D para defensor): ")
    salario = float(input("Digite o salário do jogador: R$ "))

    soma_salarios = soma_salarios + salario

    if i == 0:
        mais_novo = idade
        mais_velho = idade
    else:
        if idade < mais_novo:
            mais_novo = idade

        if idade > mais_velho:
            mais_velho = idade

    if posicao == "A":
        atacantes = atacantes + 1

        if salario <= 10000:
            atacantes_ate_10000 = atacantes_ate_10000 + 1
    else:
        defensores = defensores + 1

media_salarios = soma_salarios / 10

print("\n--- RESULTADOS ---")
print("Média dos salários: R$", media_salarios)
print("Jogador mais novo:", mais_novo, "anos")
print("Jogador mais velho:", mais_velho, "anos")
print("Atacantes com salário até R$ 10.000,00:", atacantes_ate_10000)
print("Quantidade de atacantes:", atacantes)
print("Quantidade de defensores:", defensores)
