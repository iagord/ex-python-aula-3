s = input("Digite seu sexo:")
p = float(input("Digite seu peso: "))
a = float(input("Digite sua altura: "))

imc = p / (a**2)

if s == "Feminino" or s == "fem" or s == "F":
    if imc < 19:
        print(f"Seu IMC é {imc:.1f} e você está abaixo do peso.")
    elif (imc >= 19) and (imc <= 24):
        print(f"Seu IMC é {imc:.1f} e você está no peso ideal.")
    elif imc > 24:
        print(f"Seu IMC é {imc:.1f} e você está acima do peso.")
elif s == "Masculino" or s == "masc" or s == "M":
    if imc < 20:
        print(f"Seu IMC é {imc:.1f} e você está abaixo do peso.")
    elif (imc >= 20) and (imc <= 25):
        print(f"Seu IMC é {imc:.1f} e você está no peso ideal.")
    elif imc > 25:
        print(f"Seu IMC é {imc:.1f} e você está acima do peso.")