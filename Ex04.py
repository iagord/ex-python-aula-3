b = int(input("Digite a base: "))
a = int(input("Digite a altura: "))

area = b * a

if area < 100:
    print("O valor da área é: ", area)
elif area > 100:
    print("Terreno grande")
    print("O valor da área é: ", area)