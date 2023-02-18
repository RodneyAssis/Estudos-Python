X = int(input("Digite algo: "))
Cont = 0
for i in range(1,X+1):
    if X%i == 0:
        Cont += 1
if Cont == 2 or X == 2:
    print(f"O número {X} é primo")
else:
    print(f"O número {X} não é primo")