Candidato1 = 0
Candidato2 = 0
Candidato3 = 0
Candidato4 = 0
Voto_Nulo = 0
Total = 0

menor = 9999999999999
maior = 0

while (True):
    Menu = int(input("1- Canditado1"
                     "\n2- Candidato2"
                     "\n3- Candidato3"
                     "\n4- Candidato4"
                     "\n0 para voto nulo"
                     "\n\nEscolha o candidato selecionado: "))

    if Menu == 1:
        print("Canditato: Cantidato1 - 1")
        Num_Titulo = input("Digite o numero titulo de eleitor: ")
        Nome_eleitor = input("Digite o seu nome: ")
        opcao = int(input("1- Sim | 2- Não\nTem certeza de seu voto? "))
        if opcao == 1:
            Candidato1 += 1
            Total += 1
    
    elif Menu == 2:
        print("Canditato: Cantidato2 - 2")
        Num_Titulo = input("Digite o numero titulo de eleitor: ")
        Nome_eleitor = input("Digite o seu nome: ")
        opcao = int(input("1- Sim | 2- Não\nTem certeza de seu voto? "))
        if opcao == 1:
            Candidato2 += 1
            Total += 1

    elif Menu == 3:
        print("Canditato: Cantidato3 - 3")
        Num_Titulo = input("Digite o numero titulo de eleitor: ")
        Nome_eleitor = input("Digite o seu nome: ")
        opcao = int(input("1- Sim | 2- Não\nTem certeza de seu voto? "))
        if opcao == 1:
            Candidato3 += 1
            Total += 1

    elif Menu == 4:
        print("Canditato: Cantidato4 - 4")
        Num_Titulo = input("Digite o numero titulo de eleitor: ")
        Nome_eleitor = input("Digite o seu nome: ")
        opcao = int(input("1- Sim | 2- Não\nTem certeza de seu voto? "))
        if opcao == 1:
            Candidato4 += 1
            Total += 1

    elif Menu == 5:
        print("Opção de voto Nulo")
        Num_Titulo = input("Digite o numero titulo de eleitor: ")
        Nome_eleitor = input("Digite o seu nome: ")
        opcao = int(input("1- Sim | 2- Não\nTem certeza de seu voto? "))
        if opcao == 1:
            Voto_Nulo += 1
            Total += 1
    elif Menu == -1:
        break

    else:
        print("Canditato invalido, Tente outro novamente.")




#Questão A
print(f"NUMERO DE VOTOS:\n\nCandidato1: ", Candidato1,
        "\nCandidato2: ", Candidato2,
        "\nCandidato3: ", Candidato3,
        "\nCandidato4: ", Candidato4,
        "\nTotal de votos nulos: ", Voto_Nulo,
        "\nTotal de votos: ", Total)

#Questão B
print(f"O PERCENTUAL DE VOTOS VALIDOS:\n\nCandidato1: ",(Candidato1*100)/6,
      "\nCandidato2: ",(Candidato2*100)/6,
      "\nCandidato3: ",(Candidato3*100)/6,
      "\nCandidato4: ",(Candidato4*100)/6)

#Questão C

#Questão D

print(f"O PERCENTUAL DE VOTOS NULOS:", Voto_Nulo)
print((Voto_Nulo/Total)*100)
