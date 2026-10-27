def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media


def verificar_aprovacao(media):
    if media >= 7:
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado!")



nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = calcular_media(nota1, nota2)

print(f"Média do aluno: {media:.2f}")

verificar_aprovacao(media)
