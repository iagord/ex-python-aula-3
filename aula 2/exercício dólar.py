dolar = float(input('Digite valor em dólar:'))
cotacao = float(input('Digite cotação do dólar hoje:'))
reais = float(dolar * cotacao)

print("{:.2f}".format(reais))