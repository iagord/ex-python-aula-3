n = []

for i in range (0, 10, 1):
    x = int(input("Digite um número: "))
    n.append(x)

    if (i == 0):
        maior = n[i]
    elif (n[i] > maior):
        maior = n[i]

print("O maior número é: ", maior)