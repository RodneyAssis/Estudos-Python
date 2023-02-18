Nota1=float(input("Digite sua nota: "))
Nota2=float(input("Digite sua nota: "))
Media=(Nota1+Nota2)/2

if Media < 5:
    print(f"Sua média foi de {Media}")
    print("Você está reprovado...")
elif (Media <= 6.9) and (Media > 5):
    print(f"Sua média foi de {Media}")
    print("Você está de recuperação.")
else:
    print(f"Sua média foi de {Media}")
    print("Parabêns você foi aprovado.")
