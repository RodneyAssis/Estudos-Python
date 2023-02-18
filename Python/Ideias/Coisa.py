Dic = {}
Arquivo = open("Cadastados.txt", "a")
Leitor = open("Cadastados.txt", "r")
while True:
    Nome = str(input("Nome:"))
    for i in Arquivo:
        i = i.rsplit()
        if Nome in i:
            print(f"{Nome}")
            print(i)
    if Nome == "":
        break
    CPF = int(input("CPF:"))

    Dic[Nome] = CPF
    Arquivo.write(f"{Nome}, {CPF}\n")
    Arquivo.close()
