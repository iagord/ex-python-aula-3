a = float(input("Digite a acelerção: "))
v0 = float(input("Digite a velocidade inicial: "))
t = float(input("Digite o tempo de percurso: "))

v = (v0 + (a * t)) * 3.6

if (v <= 40):
    print("Veículo muit lento.")
elif (v > 40) and (v <= 60):
    print("Velocidade permitida.")
elif (v > 60) and (v <= 80):
    print("Velocidade de cruzeiro.")
elif (v > 80) and (v <= 120):
    print("Veícuo rápido.")
else:
    print("Veículo muito rápido.")