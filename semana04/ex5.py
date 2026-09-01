pontos = 0

resposta = input("Você treinou regularmente nas últimas semanas? (Sim/Não): ")
if resposta.lower() == "sim":
    pontos += 1

resposta = input("Participou de treinos longos (acima de 10 km)? (Sim/Não): ")
if resposta.lower() == "sim":
    pontos += 1

resposta = input("Seguiu uma dieta especial para a corrida? (Sim/Não): ")
if resposta.lower() == "sim":
    pontos += 1

resposta = input("Já competiu em provas oficiais neste ano? (Sim/Não): ")
if resposta.lower() == "sim":
    pontos += 1

resposta = input("Conta com acompanhamento de treinador ou equipe? (Sim/Não): ")
if resposta.lower() == "sim":
    pontos += 1

print(f"\nRespostas positivas: {pontos}")

if pontos == 5:
    print("Atleta de Elite - pronto para o pódio!")

elif pontos == 3 or pontos == 4:
    print("Atleta Competitivo - tem boas chances de se destacar.")

elif pontos == 2:
    print("Participante Casual - ainda precisa de mais treino.")

else:
    print("Não Preparado - talvez seja melhor assistir da arquibancada este ano.")
