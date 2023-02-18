#7 - Faça um programa usando Python para ler 3 números quaisquer e calcular (imprimir)
#    a média aritmética dos dois maiores.

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
n3 = float(input("Digite outro número: "))

if (n1 > n3) and (n2 > n3):
    media=(n1+n2)/2
    print("O valor da soma é",media)

elif (n2 > n1) and (n3 > n1):
    media=(n2+n3)/2
    print("O valor da soma é",media)

else:
    media=(n1+n3)/2
    print("O valor da soma é",media)
