p=float(input("Digite o valor do preço do produto: "))

Cores= {"Branco":"\033[0;30m","Vermelho":"\033[1;31m","Verde":"\033[1;32m"}
des = p*0.05
vpa = p-des
print("Valor do produto é de {}R${}{} mais o desconto de 5% ficará {}R${}{}"
      .format(Cores["Vermelho"],p,Cores["Branco"],Cores["Verde"],vpa,Cores["Branco"]))