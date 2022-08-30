p1 = float(input('Valor primeiro produto:'))
p2 = float(input('Valor segundo produto:'))
p3 = float(input('Valor terceiro produto:'))
p4 = float(input('Valor quarto produto:'))
p5 = float(input('Valor quinto produto:'))
pagamento = float(input('Valor pago:'))
troco = float(pagamento - (p1 + p2 + p3 + p4 + p5))

print(troco)