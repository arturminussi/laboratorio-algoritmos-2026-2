numero_secreto = 57
tentativas = 0

while True:
    numero = int(input("Tente descobrir o número (1 a 100): "))
    tentativas += 1

    if numero < numero_secreto:
        print("Tente um número maior!")
    elif numero > numero_secreto:
        print("Tente um número menor!")
    else:
        print("Parabéns! Você encontrou a embalagem premiada!")
        break

print(f"Você precisou de {tentativas} tentativas.")
