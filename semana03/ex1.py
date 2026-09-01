time1 = int(input("Digite a pontuação do Time 1: "))
time2 = int(input("Digite a pontuação do Time 2: "))

if time1 > time2:
    print("Time 1 venceu!")
    print("Time 2 perdeu!")
elif time2 > time1:
    print("Time 2 venceu!")
    print("Time 1 perdeu!")
else:
    print("Houve empate!")
