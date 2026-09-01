
a = float(input("Digite o valor da força A: "))
b = float(input("Digite o valor da força B: "))
c = float(input("Digite o valor da força C: "))

if a + b > c and a + c > b and b + c > a:

    if a == b and b == c:
        print("Equilíbrio Simétrico")

    elif a == b or a == c or b == c:
        print("Equilíbrio Parcialmente Simétrico")

    else:
        print("Equilíbrio Assimétrico")

else:
    print("Não há equilíbrio.")
