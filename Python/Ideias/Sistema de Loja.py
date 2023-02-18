from time import sleep

# CUSTOMIZAÇÃO DE CORES

cores = {"normal": "\033[1;30m", "vermelho": "\033[0;31m",
         "verde": "\033[0;32m", "amarelo": "\033[0;33m",
         "azul": "\033[1;34m", "roxo": "\033[1;35m",
         "turqueza": "\033[1;36m", "cinza": "\033[1;37m"}

Nome_Clientes = []
C_CPF = []
PdTotal = 0
Cont = 0
i = 0

while True:
    print("{}-={}".format(cores["turqueza"], cores["normal"]) * 52)
    print("{}Digite qual função deseja realizar:{}".format(cores["roxo"], cores["normal"]))
    print("{}| 1-Iniciar compra | 2-Cliêntes cadastrados com CPF | 3- Consultar lucro total | 4-Encerrar expediênte |{}"
          .format(cores["azul"], cores["normal"]))
    Opcao = int(input("Digite a função: "))
    print("{}-={}".format(cores["turqueza"], cores["normal"]) * 52)

    # INICIALIZÃO DE COMPRAS:
    if Opcao == 1:
        CPF_Cliente = str(input("Digite o CPF do cliênte: "))
        N_Cliente = str(input("Digite o nome do cliênte: ")).capitalize()
        if CPF_Cliente != C_CPF:  # AJUSTES
            print("| S-SIM | | N-NÃO |")
            Cond = str(input("Deseja cadastrar o CPF do cliênte: ")).capitalize()
            if Cond == "S":
                C_CPF.append(CPF_Cliente)
                Nome_Clientes.append(N_Cliente)
                print("{}Salvando CPF do cliente{}".format(cores["verde"], cores["normal"]), end="")
                for i in range(0, 3):
                    print("{}.{}".format(cores["verde"], cores["normal"]), end="")
                    sleep(0.6)
                print("")
            elif Cond == "N":
                print("{}Continuando Transição{}".format(cores["vermelho"], cores["normal"]), end="")
                for i in range(0, 3):
                    print("{}.{}".format(cores["vermelho"], cores["normal"]), end="")
                    sleep(1)
                print("")
            print("{}-={}".format(cores["turqueza"], cores["normal"]) * 52)

        for i in range(1, 99):
            Produtos = float(input("Digite o valor do produto: "))
            Qtd = int(input("Digite a quantidade desse produto: "))
            V_Compra = (Produtos * Qtd)
            PdTotal = PdTotal + V_Compra
            print("| S-SIM | | N-NÃO |")
            Cont_2 = str(input("Deseja adicionar mais pedidos: ")).capitalize()
            if Cont_2 == "S":
                print("{}-={}".format(cores["turqueza"], cores["normal"]) * 52)
            elif Cont_2 == "N":
                break

    # CPF DOS CLIÊNTES:
    if Opcao == 2:
        if len(C_CPF) == 0:
            print("{}Nenhum cliente cadastrado no momento...{}".format(cores["vermelho"], cores["normal"]))
        else:
            for i in range(0, len(C_CPF)):
                Cont = Cont + 1
                print(f"Cliente nº{Cont}: ", Nome_Clientes[i], end=" ")
                print("\nCPF: ", C_CPF[i], end=" ")
                print("")

    # LUCRO TOTAL DO EXPEDIÊNTE:
    if Opcao == 3:
        if PdTotal == 0:
            print("{}Total de compras feitas no expediênte: R${:.2f}{}"
                  .format(cores["vermelho"], PdTotal, cores["normal"]))
        else:
            print("{}Total de compras feitas no expediênte: R${:.2f}{}"
                  .format(cores["verde"], PdTotal, cores["normal"]))

    # ENCERRAMENTO DO PROGRAMA
    if Opcao == 4:
        print("Fim do expediênte em:")

        print("3", end=" ")
        sleep(1)
        print("2", end=" ")
        sleep(1)
        print("1")
        sleep(1)
        print("{}-={}".format(cores["turqueza"], cores["normal"]) * 52)
        break
