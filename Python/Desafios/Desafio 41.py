Idade=int(input("Digite sua idade: "))
Caracter={"Negrito":"\033[1;33m", "Normal":"\033[;30m"}
print(f"\nVocê tem: {Idade} anos")
if (Idade >= 0 ) and (Idade <= 9):
    print("Você está classificado na categoria {}Mirim{}".format(Caracter["Negrito"],Caracter["Normal"]))
elif (Idade > 9) and (Idade <= 14):
    print("Você está classificado na categoria {}Infantil{}".format(Caracter["Negrito"],Caracter["Normal"]))
elif (Idade > 14) and (Idade <= 19):
    print("Você está classificado na categoria {}Junior{}".format(Caracter["Negrito"],Caracter["Normal"]))
elif (Idade > 19) and (Idade <= 20):
    print("Você está classificado na categoria {}Sênior{}".format(Caracter["Negrito"],Caracter["Normal"]))
else:
    print("Você está classificado na categoria {}Master{}".format(Caracter["Negrito"],Caracter["Normal"]))