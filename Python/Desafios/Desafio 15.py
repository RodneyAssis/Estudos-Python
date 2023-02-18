x=int(input("Dias Alugados: "))
y=float(input("Km rodados:"))

b=60*x
c=0.15*y
a=b+c

print("Valor a ser pago: R${:.2f}".format(a))