# 033[0:30:40m
# Tipo do texto: (0=normal); (1=negrito); (4=sublinhado); (7=invertido);
# Cor do texto: (30=branco); (31=Vermelho); (32=Verde); (33=amarelo); (34=azul); (35=roxo); (36=turqueza); (37=cinza)
# Cor de fundo: (30 à 37= mesma ordem)

Nome=input("Olá, qual é o seu nome? ").capitalize()
Sexo=str(input("Qual o seu sexo? [M] ou [F]"))
cores={"normal":"\033[1;30m", "vermelho":"\033[1;31m",
       "verde":"\033[1;32m", "amarelo":"\033[1;33m",
       "azul":"\033[1;34m", "roxo":"\033[1;35m",
       "turqueza":"\033[1;36m", "cinza":"\033[1;37m"} #Variavél de cores

if Sexo == "F":
    print("Olá, muito prazer em conhece-la, {}{}{}!!!".format(cores["roxo"],Nome,cores["normal"]))
else:
    print("Olá, Muito prazer em conhece-lo, {}{}{}!!!".format(cores["turqueza"],Nome,cores["normal"]))