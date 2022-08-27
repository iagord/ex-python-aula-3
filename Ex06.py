v1 = int(input("Digite um valor: "))
v2 = int(input("Digite outro valor: "))
v3 = int(input("Digite mais um valor: "))

if v1 <v3 and v2 < v3:
    print(v3)
elif v2 < v1 and v3 < v1:
    print(v1)
elif v3 < v2 and v1 < v2:
    print(v2)