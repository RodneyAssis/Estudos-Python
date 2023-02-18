Multa=float(input("Digite a velocidade percorrida: "))
if Multa > 80:
    Adicional = Multa - 80
    Taxa = Adicional * 7
    Multa_total = Taxa
    print("Você passou do limite de velocidade.")
    print("Valor da Multa: R${:.2f}".format(Multa_total))
else:
    print("Velocidade Desejada, Dirija com cuidado.")
