Cores={"Branco":"\033[0;30m","Vermelho":"\033[1;31m","Amarelo":"\033[1;33m","Verde":"\033[1;32m"}

Salario=float(input("Digite seu salário: "))
N_Salario = Salario + (Salario*0.15)
Aumento = Salario*0.15
print("Seus salario era de {}R${:.2f}{}, terá o aumento de {}15%(R${:.2f}){} onde ficará por {}R${:.2f}"
      .format(Cores["Vermelho"],Salario,Cores["Branco"],Cores["Amarelo"],Aumento,Cores["Branco"],Cores["Verde"],N_Salario))