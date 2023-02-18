#3 - Faça um programa usando Python para ler o nome, o peso e a altura (em metros) de uma
#    pessoa. Calcule o IMC (Índice de Massa Corporal). Imprima o nome lido e o respectivo IMC.
#    Obs: IMC = peso / altura2

N = str(input("Nome: "))
P = float(input("Peso: "))
A = float(input("Altura: "))

IMC = P/A**2

print("\nNome: {}\nPeso: {}Kg\nAltura {}m\n\nIMC= %.2f".format(N,P,A) %IMC)