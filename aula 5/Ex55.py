n = []

q = int(input("Digite uma quantidade de valores entre 1 e 20: "))

while (q > 20) or (q <= 0):
    print("A quantidade de valor deve ser menor que 20 e maior que 1.")
    q = int(input("Digite uma quantidade de valores entre 1 e 20: "))
    
for i in range (0, q, 1):
    x = int(input("Digite um valor: "))
    n.append(x)
