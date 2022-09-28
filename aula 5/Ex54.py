n = []
r = []

for i in range (0, 20, 1):
    x = int(input("Digite um valor: "))
    n.append(x)

m = int(input("Digite uma constante multiplicativa: "))

for i in range (0, 20, 1):
    y = n[i] * m
    r.append(y)
    print(n[i], r[i])