n = int(input("Digite um número: "))
x = 0
cores = {"WHILE": "\033[0;30m", "RED": "\033[0;31m",
         "GREEN": "\033[0;32m", "BLUE": "\033[0;34m"}

while x <= 9:
    # For c in range(1,10+1): Desafio 49
    x = x + 1
    v = n + x
    print(f"{cores['BLUE']}{n}{cores['WHILE']}+{cores['RED']}{x}{cores['WHILE']}={cores['GREEN']}{v}")
