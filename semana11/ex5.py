def calcular_media(n1, n2, n3, n4, n5):
    media = (n1 + n2 + n3 + n4 + n5) / 5
    return media


def verificar_situacao(media):
    if media >= 7:
        aprovado()
    elif media >= 4:
        recuperacao()
    else:
        reprovado()


def aprovado():
    print("Aluno aprovado!")


def recuperacao():
    print("Aluno em recuperação!")


def reprovado():
    print("Aluno reprovado!")


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
nota5 = float(input("Digite a quinta nota: "))

media = calcular_media(nota1, nota2, nota3, nota4, nota5)

print(f"Média do aluno: {media:.2f}")

verificar_situacao(media)
