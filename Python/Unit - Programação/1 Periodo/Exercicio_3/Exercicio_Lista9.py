from random import choice
Comp = ["PEDRA","PAPEL","TESOURA"]
print("JO-KEN-PO")
NickName = input("Digite seu nome: ").lower().capitalize()
Valor = int(input("Digite a quantidade rodadas: "))
Cont = 0
PtPlayer = 0
PtComputer = 0
while True:
    while Cont < Valor:
        print("Pedra, Papel e Tesoura")
        print(f"{Cont+1}º Jogo:")
        Computador = choice(Comp)
        print(Computador)
        Escolha = input("Escolha uma das alternativa: ").upper()
        while Escolha not in ("PEDRA", "PAPEL", "TESOURA"):
            if Escolha == "PEDRA" or Escolha == "PAPEL" or Escolha == "TESOURA":
                break
            print("Não existe essa opção...")
            Escolha = input("Escolha uma das alternativa: ").upper()

        if Escolha == "PEDRA" and Computador == "TESOURA" or Escolha == "PAPEL" and Computador == "PEDRA" or\
            Escolha == "TESOURA" and Computador == "PAPEL":
            PtPlayer += 1
            Cont += 1
            print(f"O {NickName} GANHOU!!")
            print(f"{NickName}: {Escolha}")
            print(f"Computador: {Computador}")
        elif Computador == "PEDRA" and Escolha == "TESOURA" or Computador == "PAPEL" and Escolha == "PEDRA" \
            or Computador == "TESOURA" and Escolha == "PAPEL":
            PtComputer += 1
            Cont += 1
            print(f"O COMPUTADOR GANHOU!!")
            print(f"{NickName}: {Escolha}")
            print(f"Computador: {Computador}")
        else:
            print("EMPATE!!")
            print(f"{NickName}: {Escolha}")
            print(f"Computador: {Computador}")

    if PtPlayer > PtComputer:
        print(f"O Vencedor foi jogador {NickName}!!!")
        print(f"Jogador = {PtPlayer}")
        print(f"Computador = {PtComputer}")
        break
    elif PtPlayer < PtComputer:
        print(f"O Vencedor foi Computador!!!")
        print(f"Jogador = {PtPlayer}")
        print(f"Computador = {PtComputer}")
        break
    else: #IMCOMPLETO
        print("Não houve vencedor..")
        print("Deseja jogar novamente?")
        Opcao = input("[SIM] | [NÃO]\n").upper()
        while Opcao not in ("SIM", "NÃO"):
            if Opcao == "SIM" or Opcao == "NÃO":
                break
            print("Não existe essa alternativa...")
            Opcao = input("[SIM] | [NÃO]\n").upper()
        if Opcao == "NÃO":
            break
