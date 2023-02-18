Soma = 0
for x in range(1,6+1):
    Num1=int(input("Digite um número:"))
    Par = Num1%2
    if Par == 0:
        Soma = Soma + Num1
        print(f"Somatorio dos nº pares no momento: {Soma}")
print(f"\nSoma total: {Soma}")