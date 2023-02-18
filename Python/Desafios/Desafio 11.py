b=float(input("Digite o comprimento da parede: "))
h=float(input("Digite a altura da parede: "))
a = b*h
umalt = 2
QLT = (a/umalt)
Cores={"Branco":"\033[0;30m","Verde":"\033[1;32m"}
print("Será necessário {}{}L{} de tinta".format(Cores["Verde"],QLT,Cores["Branco"]))