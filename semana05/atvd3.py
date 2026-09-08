soma = 0
menos_30 = 0
entre_30_e_60 = 0

for i in range(7):
    tempo = float(input("Digite o tempo do corredor: "))

    soma = soma + tempo

    if tempo < 30:
        menos_30 = menos_30 + 1
    else:
        if tempo >= 30 and tempo <= 60:
            entre_30_e_60 = entre_30_e_60 + 1

media = soma / 7
porcentagem = (entre_30_e_60 / 7) * 100

print("Tempo médio:", media, "minutos")
print("Corredores que terminaram em menos de 30 minutos:", menos_30)
print("Porcentagem entre 30 e 60 minutos:", porcentagem, "%")
