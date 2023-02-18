#8 - Faça um programa usando Python para ler osdois lados de um triângulo retângulo. Calcule
#    e imprima o valor da hipotenusa.
import math
B = float(input("Digite um valor para a base de um triangunlo: "))
H = float(input("Digite um valor para a altura do triangulo:"))

Hip = B**2 + H**2
Hip = Hip**(1/2)

print("Valor é Hipotenusa é: ",Hip)