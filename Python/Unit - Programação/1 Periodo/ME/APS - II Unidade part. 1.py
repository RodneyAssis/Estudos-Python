#APS – Unidade II - Parte 01
#Aluno: Rodney Assis Matos Furtado				Curso: Ciências da Computação
#Profº.: Virgilio Antonio N C de Faro
#Data: 27/05/2020

N_Windows=[]
N_Linux=[]
N_Mac_OS=[]
N_Outros=[]
print("-="*22)
while True:
    Nome = str(input("Digite o seu nome: ")).capitalize()
    print("|1-Windows| |2-Linux| |3-Max OS| |4-Outros|")
    Opcao = int(input("Escolha uma das alternativas: "))

    if Opcao == 0:
        break

    if Opcao < 0 or Opcao > 4:
        print("Numero não disponivel, por favor digite o voto novamente.")
    print("=-" * 22)

    if Opcao == 1:
        N_Windows = N_Windows + [Nome]
    elif Opcao == 2:
        N_Linux = N_Linux + [Nome]
    elif Opcao == 3:
        N_Mac_OS = N_Mac_OS + [Nome]
    elif Opcao == 4:
        N_Outros = N_Outros + [Nome]
print("=-"*22)
print("")


#TOTAL DE VOTOS:
Total = len(N_Windows) + len(N_Linux) + len(N_Mac_OS) + len(N_Outros)
print("=-"*22)
print(f"Total de votos computados: {Total}")


#QUANTIDADE DE VOTOS DE CADA SISTEMA OPERACIONAL E A RELAÇÃO ENTRE ELES:
print("=-"*22)
print("Total de votos de cada Sistema Operacional: ")
print(f"Windows: {len(N_Windows)}")
print(f"Linux: {len(N_Linux)}")
print(f"Mac_OS: {len(N_Mac_OS)}")
print(f"Outros: {len(N_Outros)}")

print("=-"*22)
print("Relação de cada sistema Sistema Operacional:")


if len(N_Windows) == len(N_Linux) == len(N_Mac_OS) == len(N_Outros) != 0:
    print("Todos possuem a mesma quantidade de votos")
    print(f"Votos: {len(N_Windows)}")
elif len(N_Windows) == len(N_Linux) == len(N_Mac_OS) != 0:
    print("Os sistemas operacionais Windows, linux e Mac_OS tiraram a mesma quantidade de votos.")
    print(f"Votos: {len(N_Windows)}")
elif len(N_Windows) == len(N_Mac_OS) == len(N_Outros) != 0:
    print("Os sistemas operacionais Windows, Mac_OS e a opção Outros tiraram a mesma quantidade de votos.")
    print(f"Votos: {len(N_Windows)}")
elif len(N_Windows) == len(N_Linux) == len(N_Outros) != 0:
    print("Os sistemas operacionais Windows, Linux e a opção Outros tiraram a mesma quantidade de votos.")
    print(f"Votos: {len(N_Windows)}")
elif len(N_Linux) == len(N_Mac_OS) == len(N_Outros) != 0:
    print("Os sistemas operacionais Linux, Mec_OS e a opção Outros tiraram a mesma quantidade de votos.")
    print(f"Votos: {len(N_Linux)}")

elif len(N_Windows) == len(N_Linux) != 0:
    print("Os sistemas operacionais Windows e Linux tiraram a mesma quantidade de votos.")
    print(f"Votos: {len(N_Windows)}")
elif len(N_Windows) == len(N_Mac_OS) != 0:
    print("Os sistemas operacionais Windows e o Mac_OS tiraram a mesma quantidade de votos.")
    print(f"Votos: {len(N_Windows)}")
elif len(N_Windows) == len(N_Outros) != 0:
    print("Os sistemas operacionais Windows e a opção Outros tiraram a mesma quantidade de votos.")
    print(f"Votos: {len(N_Windows)}")
elif len(N_Linux) == len(N_Mac_OS) != 0:
    print("Os sistemas operacionais Linux e o Mec_OS tiraram a mesma quantidade de votos.")
    print(f"Votos: {len(N_Linux)}")
elif len(N_Linux) == len(N_Outros) != 0:
    print("Os sistemas operacionais Linux e a opção Outros tiraram a mesma quantidade de votos.")
    print(f"Votos: {len(N_Linux)}")
elif len(N_Mac_OS) == len(N_Outros) != 0:
    print("Os sistemas operacionais Mec_OS e a opção Outros tiraram a mesma quantidade de votos.")
    print(f"Votos: {len(N_Mac_OS)}")
else:
    print("Não possui relações distintas.")

#PORCENTUAL DOS SISTEMAS OPERACIONAIS:
print("=-"*22)
print("Porcentual de cada Sistema Operacional:")
porc_Win = (len(N_Windows)/Total)*100
print(f"Porcent. Windows: {porc_Win:.2f}%")
porc_Li = (len(N_Linux)/Total)*100
print(f"Porcent. Linux: {porc_Li:.2f}%")
porc_Mc = (len(N_Mac_OS)/Total)*100
print(f"Porcent. Mac_OS: {porc_Mc:.2f}%")
porc_Other = (len(N_Outros)/Total)*100
print(f"Porcent. opção Outros: {porc_Other:.2f}%")


#SISTEMA OPERACIONAL MAIS VOTADO(Modificado):

Listamax = [len(N_Windows), len(N_Linux), len(N_Mac_OS), len(N_Outros)]
Os =["Windows","Linux","Mac_OS","Outros"]
Top = max(Listamax)
X = Listamax.index(Top)
print(f"O Sistema Operacional mais votado foi o {Os[X]} com aproximadamente {Listamax[X]}")

#SISTEMA OPERACIONAL MAIS VOTADO(Antigo):
#if (len(N_Windows) > len(N_Linux)) and (len(N_Windows) > len(N_Mac_OS)) and (len(N_Windows) > len(N_Outros)):
#    print("O sistema Operacional mais votado é o Windows.")
#elif (len(N_Linux) > len(N_Windows)) and (len(N_Linux) > len(N_Mac_OS)) and (len(N_Linux) > len(N_Outros)):
#    print("O sistema Operacional mais votado é o Linux.")
#elif (len(N_Mac_OS) > len(N_Windows)) and (len(N_Mac_OS) > len(N_Linux)) and (len(N_Mac_OS) > len(N_Outros)):
#    print("O sistema Operacional mais votado é o Mac_OS.")
#elif (len(N_Outros) > len(N_Windows)) and (len(N_Outros) > len(N_Linux)) and (len(N_Outros) > len(N_Mac_OS)):
#    print("O sistema Operacional mais votado é Outro.")
#else:
#    print("Não Houve Vencedor nesta votação.")
#print("=-"*22)