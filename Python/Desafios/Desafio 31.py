Km = float(input("Digite quantidade de Kilometros rodados: "))

if Km <= 200:
    V_cobrado=0.50*Km
    print(f"Valor cobrado: R${V_cobrado:.2f}")
else:
    V_cobrado=0.45*Km
    print(f"Valor cobrado: R${V_cobrado:.2f}")
