import Funcoes_Prova

"""Você possui um estacionamento de carros e precisa desenvolver um sistema em PYTHON para
controlar esse estacionamento. A regra geral é que cada cliente aluga uma vaga por dia. O
estacionamento possui um total de 20 vagas.
O sistema deve ter um menu com as seguintes funcionalidades e requisitos:
a) Cadastro de Clientes; (1,0)
a. CPF, Nome, Placa do Carro, Status [Ativo, Inativo];
b) Registro de Aluguel de Vaga; (1,0)
a. Usuário informa CPF para reservar a vaga;
c) Relatório de Vagas (todas as vagas); (0,5)
a. Informar o Nome do cliente + Placa para as vagas alugadas;
d) Relatório de Clientes Ativos. (0,5)
O sistema deve ser capaz de armazenar dados para serem visualizados, mesmo após o término
da execução do programa.
Não é necessário controlar fisicamente a vaga no estacionamento, o cliente pode estacionar em
qualquer vaga livre."""

Matrix = []
Status_Cliente = {}
Reserva_Cliente = {}
D = " | "
for i in range(4):
    Linha = []
    for k in range(5):
        Linha.append("︻")
    Matrix.append(Linha)
while True:
    Funcoes_Prova.Clientes_Reservas(Reserva_Cliente)
    Funcoes_Prova.Clientes_Status(Status_Cliente)
    print(Status_Cliente)
    print(Reserva_Cliente)
    print("Menu de Estacionamento:\n"
          "1- Cadastro de Cliente.\n"
          "2- Registro de Aluguel de Vaga.\n"
          "3- Relatorio de Vagas.\n"
          "4- Relatório de Cliente ativos.")
    Escolha = int(input("\nEscolha uma das opções: "))

    # Cadastro dos Clientes:
    if Escolha == 1:
        while True:
            while True:
                with open("Cadastro_Cliente.txt", "a") as Adicionar:
                    CPF_Cliente = input("\nDigite o CPF: ")
                    while len(CPF_Cliente) != 11 or CPF_Cliente.isalpha():
                        print("Erro! CPF deve possui apenas 11 digitos:")
                        CPF_Cliente = input("Digite o CPF:")
                        if (len(CPF_Cliente) == 11) and (not CPF_Cliente.isalpha()):
                            break
                    with open("Cadastro_Cliente.txt", "r") as Leitor:
                        if CPF_Cliente in Leitor.read():
                            print("\nCliente cadastrado em nosso banco de dados.\n")

                            break
                    Nome_Cliente = input("Digite o Nome: ").title()
                    Placa = input("Digite a placa do carro: ").upper()
                    if len(Placa) == 7:
                        if Placa[:2].isalpha() and Placa[3:].isnumeric():
                            print()
                        else:
                            print("Erro!")
                            break
                    else:
                        print("Erro!")
                        break
                    Statu_Cliente = int(input("[1- Ativo || 2- Inativo]\n"
                                               "Escolha uma das alternativas: "))
                    Adicionar.write(f"{CPF_Cliente} {Nome_Cliente} {Placa[:3]}-{Placa[3:]} ")
                    if Statu_Cliente == 1:
                        Statu_Cliente = "Ativo"
                        Adicionar.write(f"{Statu_Cliente}\n\n")
                        with open("Registro_Atividade.txt", "a") as Registra:
                            Status_Cliente[CPF_Cliente] = Statu_Cliente
                            Registra.write(f"{CPF_Cliente} {Statu_Cliente}\n")
                        break
                    elif Statu_Cliente == 2:
                        Statu_Cliente = "Inativo"
                        Adicionar.write(f"{Statu_Cliente}\n\n")
                        with open("Registro_Atividade.txt", "a") as Registra:
                            Status_Cliente[CPF_Cliente] = Statu_Cliente
                            Registra.write(f"{CPF_Cliente} {Statu_Cliente}\n")
                        break
            Saida = input("Para sair basta apertar a tecla 'Enter'")
            if Saida == "":
                print("")
                break
    # Resevar de Aluguel de Vagas
    if Escolha == 2:
        while True:
            while True:
                    try:
                        for i in range(0, len(Matrix)):
                            print(f"| {D.join(Matrix[i])} |")

                        CPF_Cliente = input("\nDigite o CPF do cliente:")
                        while len(CPF_Cliente) != 11 or CPF_Cliente.isalpha():
                            print("Erro! CPF deve possui apenas 11 digitos:")
                            CPF_Cliente = input("Digite o CPF:")
                            if (len(CPF_Cliente) == 11) and (not CPF_Cliente.isalpha()):
                                break

                        with open("Cadastro_Cliente.txt", "r") as Leitor:
                            if CPF_Cliente not in Leitor.read():
                                print("Cliente não cadastrado ou ocorreu algum erro na digitação")
                                break
                        if Status_Cliente[CPF_Cliente] == "Inativo":
                            print("\nVocê não pode fazer um cadastro, pois encontra-se inativo.\n")
                        elif Status_Cliente[CPF_Cliente] == "Ativo":
                            Coluna = int(input("Digite qual coluna deseja reservar: "))
                            Linha = int(input("Digite qual linha deseja reservar: "))
                            Matrix[Coluna - 1][Linha - 1] = "🔒"
                            with open("Registro_Reserva.txt", "a") as Reserva:   # Terminar depois #imcompleto
                                Reserva.write(f"{CPF_Cliente} {Coluna-1, Linha-1}\n")
                    except ValueError:
                        print("Erro!")
            Saida = input("\nPara sair basta apertar a tecla 'Enter'\n")
            if Saida == "":
                print("")
                break
