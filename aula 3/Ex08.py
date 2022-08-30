v1 = float(input("Digite o valor de um lado do triângulo: "))
v2 = float(input("Digite o valor de outro lado do triângulo: "))
v3 = float(input("Digite o valor de mais um lado do triângulo: "))

if (v1 + v2 > v3) or (v2 + v3 > v1) or (v3 + v1 > v2):
    if (v1 == v2) and (v1 == v3) and (v2 == v3):
        print("Seu triânguo é equilátero!")
    elif (v1 != v2) and (v1 != v3) and (v2 != v3):
        print("Seu triângulo é escaleno!")
    else:
        print("Seu triângulo é isósceles!")
else:
    print("Não é um triângulo.")