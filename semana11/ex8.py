def converter_hora(hora, minutos):
    if hora == 0:
        hora12 = 12
        periodo = "A.M."
    elif hora < 12:
        hora12 = hora
        periodo = "A.M."
    elif hora == 12:
        hora12 = 12
        periodo = "P.M."
    else:
        hora12 = hora - 12
        periodo = "P.M."

    return hora12, minutos, periodo


def mostrar_hora(hora, minutos, periodo):
    print(f"Horário convertido: {hora}:{minutos:02d} {periodo}")


hora = int(input("Digite a hora (0 a 23): "))
minutos = int(input("Digite os minutos (0 a 59): "))

if 0 <= hora <= 23 and 0 <= minutos <= 59:
    hora12, minutos, periodo = converter_hora(hora, minutos)
    mostrar_hora(hora12, minutos, periodo)
else:
    print("Horário inválido! Digite uma hora entre 0 e 23 e minutos entre 0 e 59.")
