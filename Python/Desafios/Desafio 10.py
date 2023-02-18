real = float(input("Digite o valor que deseja compra em dolar: "))

cores = {"verde": "\033[1;32m", "branco": "\033[1;30m", "vermelho": "\033[1;31m"}
dolar = real / 5.21
print("Com {}R${:.2f}{} terá convertendo em Dolar {}US${:.2f}"
      .format(cores["verde"], real, cores["branco"], cores["vermelho"], dolar))
