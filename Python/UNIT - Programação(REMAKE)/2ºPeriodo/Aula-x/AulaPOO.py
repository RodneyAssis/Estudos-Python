class Dentista:
    nome = ""
    CRM = ""
    CPF = ""
    data_nasc = ""
    status = ""

    def __init__(self, nome, crm, cpf, data_nasc, status):
        self.nome = nome
        self.CRM = crm
        self.CPF = cpf
        self.data_nasc = data_nasc
        self.status = status


class Cliente:
    nome = ''
    CPF = ''
    data_nasc = ''

    def __init__(self, nome, cpf, data_nasc):
        self.nome = nome
        self.CPF = cpf
        self.data_nasc = data_nasc


N_Dentistas = []
CRM_Dentistas = []
CPF_Dentistas = []
DATA_Dentistas = []
S_Dentistas = []

D_dados = Dentista(N_Dentistas, CRM_Dentistas, CPF_Dentistas, DATA_Dentistas, S_Dentistas)

while True:
    print(D_dados.nome)
    print("Bem-Vindo a Odonto Python!\n"
          "1 - Cadastrar Dentista\n"
          "2 - Cadastrar Cliente\n"
          "3 - Consultar\n"
          "4 - Sair")
    Opcao = int(input("Escolha o processo que deseja realizar: "))

    if Opcao == 1:
        print(D_dados.nome)
        if Dentista.nome == "":
            print("------Cadastro do Dentista------")
            D_Nome = input("Nome do dentista: ")
            D_CRM = input("CRM do dentista: ")
            D_CPF = input("CPF do dentista: ")
            D_DataNasc = int(input("Data de nascimento do dentista: "))
            D_Status = int(input("1-Ativo\n"
                                 "2-Inativo\n"
                                 "Disponibilidade do dentista: "))

            N_Dentistas.append(D_Nome.title())
            CRM_Dentistas.append(D_CRM)
            CPF_Dentistas.append(D_CPF)
            DATA_Dentistas.append(D_DataNasc)
            if D_Status == 1:
                S_Dentistas.append('Ativo')
            else:
                S_Dentistas.append('Inativo')

        elif Dentista.nome != "":
            print("Dentista já cadastrado.")
