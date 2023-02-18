#4 - Faça um programa usando Python para ler 3 números quaisquer e determinar (imprimir) o maior deles.
#    OBS: Suponha números diferentes

N1 = float(input("Digite um número: "))
N2 = float(input("Digite mais um número: "))
N3 = float(input("Digite outro número: "))

print("\nOs numero são {}, {} e {}".format(N1,N2,N3))

if (N1 > N2) and (N2 > N3):
    print("{} é o maior número.".format(N1))
elif (N1 > N3) and (N3 > N2):
    print("{} é o maior número.".format(N1))
elif (N2 > N1) and (N1 > N3):
    print("{} é o maior número.".format(N2))
elif (N2 > N3) and (N3 > N1):
    print("{} é o maior número.".format(N2))
elif (N3 > N2) and (N2 > N1):
    print("{} é o maior número.".format(N3))
elif (N3 > N1) and (N1 > N2):
    print("{} é o maior número.".format(N3))