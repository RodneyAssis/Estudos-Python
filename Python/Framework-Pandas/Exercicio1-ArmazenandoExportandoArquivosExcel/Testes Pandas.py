import pandas as pd

CPF_Paciente = []
Nome_Paciente = []
Idade_Paciente = []
Suspeita_COVID = []

while True:
    try:
        Arquivo_read = pd.read_excel("Banco_Dados.xlsx")
        Dados = Arquivo_read.to_dict('list')
        Nome_Paciente, Idade_Paciente = Dados["Paciente"], Dados["Idade"]
        CPF_Paciente, Suspeita_COVID = Dados["CPF do paciênte"], Dados["Suspeito de COVID"]
    except FileNotFoundError:
        pass

    Dados = {"Paciente": Nome_Paciente,
             "CPF do paciênte": CPF_Paciente,
             "Idade": Idade_Paciente,
             "Suspeito de COVID": Suspeita_COVID}

    Opcao = int(input("\nDigite uma das alternativas: "))

    # CADASTRAR PACIÊNTES
    if Opcao == 1:
        while True:
            Nome = input("\nPara encerrar o processo, digite 0\nNome do paciênte: ").title()
            if Nome == '0':
                break
            Idade = input("Idade do paciênte: ")
            CPF = input("CPF do paciente: ")
            while CPF in CPF_Paciente:
                print("Este CPF encontrasse salvo em nosso banco de dados.")
            Covid = input("S - SIM | N - NÃO\n"
                          "Está diagnosticado com Covid? ").capitalize()

            Nome_Paciente.append(Nome)
            Idade_Paciente.append(Idade)
            CPF_Paciente.append(CPF)
            Suspeita_COVID.append(Covid)

            Banco_Dados = pd.DataFrame(Dados)
            Banco_Dados.to_excel("Banco_Dados.xlsx", sheet_name='Dados_Paciente', index=False)
            print(f"Dados cadastrados com sucesso!")

    # REMOVER PACIÊNTE
    elif Opcao == 2:
        while True:
            CPF_Remover = int(input("Digite o CPF do paciênte: "))
            if CPF_Remover not in CPF_Paciente:
                print("Paciênte não encontrado em nosso banco de dados.")
                break
            Remover = CPF_Paciente.index(CPF_Remover)
            CPF_Paciente.pop(Remover)
            Nome_Paciente.pop(Remover)
            Idade_Paciente.pop(Remover)
            Suspeita_COVID.pop(Remover)

            Banco_Dados = pd.DataFrame(Dados)
            Banco_Dados.to_excel("Banco_Dados.xlsx", index=False)
            print(Banco_Dados)
            break
    elif Opcao == 3:
        if len(Arquivo_read) > 0:
            print(Arquivo_read)
        else:
            print("Não possuimos paciênte no momento, tente mais tarde.")
