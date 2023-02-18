import pandas as pd

Lista_Matrix = []
for i in range(10):
    Lista_Matrix.append([])
    for j in range(5):
        Lista_Matrix[i].append('X')


OrigemPassageiros = []
NomePassageiros = []
CPFPassageiros = []
DestinoPassageiros = []

try:
    info = pd.read_excel("Dados.xlsx")
    Arquivos = info.to_dict('list')
    CD = Arquivos['CPF']
    CPFPassageiros, NomePassageiros = Arquivos['CPF'], Arquivos['Nome']
    OrigemPassageiros, DestinoPassageiros = Arquivos['Origem'], Arquivos['Destino']
except FileNotFoundError:
    pass

Dados_Passageiros = {'CPF': CPFPassageiros,
                     'Nome': NomePassageiros,
                     'Origem': OrigemPassageiros,
                     'Destino': DestinoPassageiros}

while True:
    print(Dados_Passageiros)
    Opcao = int(input("1- Cadastrar Passageiro\n"
                      "2- Reservar Assento de viagem\n"
                      "3- Consultar Relatorio dos Estados de origem\n"
                      "4- Consultar Relatorio dos Estados de Destino\n"
                      "5- Sair\n"
                      "Escolha uma das opção: "))

    if Opcao == 1:
        print(CPFPassageiros)
        while True:
            P_CPF = input("CPF do passageiro: ")
            if P_CPF in CPFPassageiros:
                print("Passageiro já cadastrado")
                break
            P_Nome = input("Nome do passageiro: ").title()
            P_Origem = input("Local do embarque: ").title()
            P_Destino = input("Destino do passageiro: ").title()
            D = str(P_CPF)
            CPFPassageiros.append(P_CPF)
            NomePassageiros.append(P_Nome)
            OrigemPassageiros.append(P_Origem)
            DestinoPassageiros.append(P_Destino)

            Dados = pd.DataFrame(Dados_Passageiros)

            Dados.to_excel('Dados.xlsx', sheet_name='Passageiros')
        else:
            break
    if Opcao == 2:
        for i in range(len(Lista_Matrix)):
            print(Lista_Matrix[i])

        Posicao = int(input("Escolha a posição: "))
        Assento = int(input("Escolha a cadeira: "))

        Lista_Matrix[Posicao-1][Assento-1] = '0'
    if Opcao == 5:
        break