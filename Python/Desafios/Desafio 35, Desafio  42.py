Reta1=int(input("Digite o valor para a 1º reta: "))
Reta2=int(input("Digite o valor para a 2º reta: "))
Reta3=int(input("Digite o valor para a 3º reta: "))
print("")

if (Reta1 > Reta2) and (Reta2 >= Reta3):
    RetaX = Reta2+Reta3
    if Reta1 < RetaX:
        print("É possivel fazer um triângulo com essas retas.")
    elif Reta1 >= RetaX:
        print("Não é possível fazer um triângulo com essas retas")

elif (Reta2 >= Reta3) and (Reta3 >= Reta1):
    RetaX = Reta3+Reta1
    if Reta2 < RetaX:
        print("É possivel fazer um triângulo com essas retas.")
    elif Reta2 >= RetaX:
        print("Não é possível fazer um triângulo com essas retas")

elif (Reta3 >= Reta1) and (Reta1 >= Reta2):
    RetaX = Reta1+Reta2
    if Reta3 < RetaX:
        print("É possivel fazer um triângulo com essas retas.")
    elif Reta3 >= RetaX:
        print("Não é possível fazer um triângulo com essas retas")
else:                                                                     #Três retas iguais.
    print("É possivel fazer um triângulo com essas retas.")

if (Reta1 == Reta2) and (Reta2 == Reta3):
    print("É um Triangulo equilátero")
elif (Reta1 == Reta2) and (Reta2 != Reta3) or (Reta1 == Reta3) and (Reta3 != Reta2) or (Reta2 == Reta3) and (Reta3 != Reta1):
    print("É um Triangulo Isóceles")
else:
    print("É um Triangulo Escaleno")
print(f"{Reta1} x {Reta2} x {Reta3}")
