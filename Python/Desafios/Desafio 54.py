X = 7
Y = 0
for i in range(7):
    Nome=(input("Por favor digite o seu nome:"))
    Nascimento=(int(input("Digite também seu ano de nascimento: ")))
    Condicao = 2020 - Nascimento
    if Condicao < 21:
        X -= 1
Y = 7 - X
print("\nQuantidade pessoas maiores de idade:",X)
print("Quantidade pessoas menores de idade:",Y)