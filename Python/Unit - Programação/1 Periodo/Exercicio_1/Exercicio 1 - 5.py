#5 - Faça um programa usando Python para ler dois números quaisquer.
#    Determine e imprima o maior.
#    OBS.: Caso sejam iguais imprima uma mensagem “Números iguais”

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))

if n1 > n2:
    print("{} é maior que {}.".format(n1,n2))

elif n2 > n1:
    print("{} é maior que {}.".format(n2,n1))

else:
    print("Os dois numeros são iguais.")