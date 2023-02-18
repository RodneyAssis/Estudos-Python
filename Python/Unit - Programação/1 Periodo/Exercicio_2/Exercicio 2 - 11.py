from random import randint
Qtd6=0
for i in range (10):
    d= randint(1,6)
    print(d, end=" ")

    if d == 6:
        Qtd6 = Qtd6 + 1

print(f"\nA quantidade de numeros 6 é {Qtd6}")