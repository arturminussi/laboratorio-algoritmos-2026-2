
etiquetas = []

while len(etiquetas) < 15:
    codigo = int(input(f"Digite o código da etiqueta {len(etiquetas) + 1}: "))

    if codigo in etiquetas:
        print("Código já cadastrado! Digite outro código.")
    else:
        etiquetas.append(codigo)
        print("Código cadastrado com sucesso!")

print("\nEtiquetas cadastradas:")
for codigo in etiquetas:
    print(codigo)
