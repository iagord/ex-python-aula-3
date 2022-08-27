p = float(input("Digite seu peso: "))
a = float(input("Digite sua altura: "))

imc = p / (a**2)

if (imc >= 18.5) and (imc <= 24.9):
    print(f"Seu IMC é {imc:.1f} e você está no peso ideal!")
elif (imc <= 18.5) or (imc >= 24.9):
    print(f"Seu IMC é {imc:.1f} e você não está no peso ideal!")