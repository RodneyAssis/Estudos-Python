Valor_C=float(input("Digite o valor da casa que deseja: "))
Salario=float(input("Digite o valor do seu salario: "))
Anos=int(input("Quantos anos deseja para pagar: "))

Meses= Anos * 12
Limite= Salario*0.30
Valor_Men=Valor_C/Meses
print("")
if Valor_Men <= Limite:
    print("O emprestimo aprovado!!")
    print("O valor mensal não excedeu os {:.2f}(30%) do seu salário!".format(Limite))
    print("O valor a ser pago mensalmente será de: {:.2f}".format(Valor_Men))

else:
    print("O emprestimo foi repovado")
    print("O valor mensal excede os 30% do seu salário!")
    print("Valor da Prestação: {:.2f}\nValor Limite(30%): {:.2f}".format(Valor_Men,Limite))