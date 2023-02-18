Lista = []
Lista_Senha = []
while len(Lista) < 10:
    Nome = input("Digite um nome: ")
    Senha = input("Digite sua senha: ")
    Cont = 0
    Cond = 0
    while Nome in Lista:
        Nome = input("Digite um nome diferente. Este se encontra em noss banco de dados: ")
        if Nome not in Lista:
            break
        Cont += 1
        if Cont == 3:
            Confirmacao = input("Para sabermos que é você, digite a sua senha: ")
            if Confirmacao != Lista_Senha:
                print("INVASÃO!")
                Cond += 1
                break
    if Cond == 1:
        break
    Lista.append(Nome)
    Lista_Senha.append(Lista_Senha)
    print(len(Lista))
    print(Lista)
