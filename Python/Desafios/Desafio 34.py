Salario=float(input("Digite o Salario: "))

if Salario < 1250:
    Salario_Novo = Salario + (Salario*0.15)
    print(f"O salário teve aumento de 15%: R${Salario_Novo:.2f}")
else:
    Salario_Novo = Salario + (Salario*0.10)
    print(f"O salário teve aumento de 10%: R${Salario_Novo:.2f}")
