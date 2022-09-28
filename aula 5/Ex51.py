n = []

for i in range (0, 10, 1):
    x = int(input("Digite um número: "))
    n.append(x)

print("Os números que você digitou foram: ")

for i in range (9, -1, -1):
    print(n[i])