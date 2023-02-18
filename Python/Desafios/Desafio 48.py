Num1 = 0
Soma = 0
Total = 0
for i in range(1,500+1):
    print(f"{i}º intervelo")
    Num1 += 1
    Mult3 = Num1%3
    Par = Num1%2
    if Mult3 == 0 and Par != 0:
        print(f"O nº{Num1} é multiplo e 3 e também impar.")
        Total += Num1
        print(f"{Num1}+{Soma}={Total}")
        Soma += Num1