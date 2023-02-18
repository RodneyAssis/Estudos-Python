Criar = open('Cadastrados.txt', 'a')
Dic = {}
while True:
    print(Coisa)
    Nome = str(input("Nome:"))
    CPF = str(input("CPF: "))
    Dic[CPF] = Nome
    with open("Cadastrados.txt", "r") as Leitor:
        for Coisa in Leitor:
            Coisa = Coisa.rsplit()
            if Leitor in Coisa:
                print(f"O CPF {CPF} Já está cadastrado")
                print(Coisa)
                break
    print(Dic[CPF])
    if CPF not in Coisa:
        print(Coisa)
        with open("Cadastrados.txt", "a") as Arquivo:
            Arquivo.write(f"{str(Dic)}\n")
