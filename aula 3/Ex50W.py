#Elabore um programa que apresente os números pares maiores que 10 no intervalo fechado [A, B]. Sendo que A e B serão números inteiros escolhidos pelo usuário. Um número é par quando este satisfaz a seguinte condição: (NÚMERO mod 2 = 0)

A = int(input("Digite o número inicial: "))
B = int(input("Digite o número final: "))
n = A
while (n <= B):
    if (n % 2 == 0):
        print(n)
    n = n + 1