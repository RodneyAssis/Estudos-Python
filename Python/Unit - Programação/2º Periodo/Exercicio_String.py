Texto = input("Digite alguma informação: ")

Cont = 0
for Palavra in Texto:
    if Texto.startswith("para"):
        Cont += 1
print(Cont)