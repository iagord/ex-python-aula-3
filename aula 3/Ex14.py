v1 = float(input("Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valor: "))

print("-------------Calculadora-------------")
print("1 - Multiplicação")
print("2 - Adição")
print("3 - Divisão")
print("4 - Subtração")
print("5 - Fim do processo")
print("-------------------------------------")

resposta = int(input("Digite sua opção: "))

if resposta == 1:
    print(v1 * v2)
    print("-------------Fim do programa-------------")
elif resposta == 2:
    print(v1 + v2)
    print("-------------Fim do programa-------------")
elif resposta == 3:
    if v1 == 0  or v2 == 0:
        print("Erro")
        print("-------------Fim do programa-------------")
    else:
        print(v1 / v2)
        print("-------------Fim do programa-------------")
elif resposta == 4:
    print(v1 - v2)
    print("-------------Fim do programa-------------")
elif resposta == 5:
    print("-------------Fim do programa-------------")
else:
    print("Comando não encontrado.")