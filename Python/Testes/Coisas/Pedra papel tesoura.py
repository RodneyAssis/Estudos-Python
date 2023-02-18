import random
from time import sleep

player = 0  # Contador de pontos
machine = 0
drawn = 0

cores={"normal": "\033[1;30m", "vermelho": "\033[1;31m", # Variavél de cores
       "verde": "\033[1;32m", "amarelo": "\033[1;33m",
       "azul": "\033[1;34m", "roxo": "\033[1;35m",
       "turqueza": "\033[1;36m", "cinza": "\033[1;37m"}

print(f"{cores['amarelo']}=-" * 20)
print(" "*7, "Pedra, Papel e Tesoura")
print("-="*20, "{}".format(cores["normal"]))

while True:
    Jogador = str(input("{}Escolha uma das alternativas: {}".format(cores["azul"], cores["normal"]))).upper()
    # Decisão do "Jogador"
    opcoes = {"PEDRA", "PAPEL", "TESOURA"}
    PC = random.choice(opcoes) # Decisão do "PC"
    print("{}Analisando...{}".format(cores["vermelho"],cores["normal"]))
    print("")
    sleep(2)
    if (Jogador=="PEDRA" and PC=="TESOURA") or (Jogador=="PAPEL" and PC=="PEDRA") or (Jogador=="TESOURA" and PC=="PAPEL"):
        print("{}Jogador ganhou!".format(cores["verde"]))
        print(f"Jogador: {Jogador}\nPC: {PC}")
        player=player+1
    elif (PC=="PEDRA" and Jogador=="TESOURA") or (PC=="PAPEL" and Jogador=="PEDRA") or (PC=="TESOURA" and Jogador=="PAPEL"):
        print("{}PC Ganhou!".format(cores["vermelho"]))
        print(f"Jogador: {Jogador}\nPC: {PC}")
        machine=machine+1
    else:
        print("{}Empate!".format(cores["amarelo"]))
        print(f"Jogador: {Jogador}\nPC: {PC}")
        drawn=drawn+1
    print("{}".format(cores["normal"]))
    cont = str(input("Deseja continuar: "))
    print("")
    if cont == "n":
        break

print("{}Jogador: {}{}".format(cores["verde"], player, cores["normal"]))
print("{}PC: {}{}".format(cores["vermelho"], machine, cores["normal"]))
print("{}Empates: {}{}".format(cores["amarelo"], drawn, cores["normal"]))

