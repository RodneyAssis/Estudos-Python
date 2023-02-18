Info = []
Cont = 0
D = ""
while True:
    Nome = input("Nome do usuario: ")
    if Nome == "":
        break
    CPF = int(input("Digite o CPF: "))
    Dia = int(input("Data de nascimento\nDia: "))
    Mes = int(input("Mês: "))
    Ano = int(input("Ano: "))
    Cont += 1
    Info += [f" {str(Cont).ljust(7)}{Nome.ljust(13)} {str(CPF).ljust(17)}"]

print(f"Nrº{D.rjust(5)}Nome{D.rjust(15)}CPF{D.rjust(15)}Data")
for i in range(len(Info)):
    print(D.join(Info[i]))
