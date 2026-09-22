n1 = 3
n2 = 11
n = n1 - 2

while n < n2:
    n = n % 12
    n = n + 2

    if n % 5 == 2:
        break

print(n)
