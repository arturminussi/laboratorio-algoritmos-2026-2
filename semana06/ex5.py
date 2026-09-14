empresa1 = 5000
empresa2 = 8000
meses = 0

while empresa1 < empresa2:
    empresa1 = empresa1 * 1.05
    empresa2 = empresa2 * 1.01
    meses += 1

print(f"Meses necessários: {meses}")
print(f"Produção da primeira empresa: {empresa1:.2f} pacotes")
print(f"Produção da concorrente: {empresa2:.2f} pacotes")
