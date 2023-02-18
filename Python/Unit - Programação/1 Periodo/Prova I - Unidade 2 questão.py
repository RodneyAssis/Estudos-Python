#2º Questão
#Nome do Aluno: Rodney Assis Matos Furtado
#Nº de Matricula: 1201131119
Num_InfectadosT = 0
QuantPacieTotal = 0
QuantMortTotal = 0
Maior = 0
Menor = 99999999999999
NomeM = ""
NomeMe = ""
while True:
    Cd_Estado=int(input("Digite o Codigo do Estado: "))
    if Cd_Estado < 0:
        print("")
        break
    N_Estado=str(input("Digite o nome do Estado: "))
    Quant_Paciêntes = int(input("Digite a quantidade de paciêntes infectados: "))
    Quant_Mort=int(input("Digite a quantidade de pessoas que morreram pelo COVID-19: "))
    if(Quant_Mort > Maior):
        Maior = Quant_Mort
        NomeM = N_Estado
    if(Quant_Paciêntes < Menor):
        Menor = Quant_Paciêntes
        NomeMe = N_Estado
    QuantMortTotal = QuantMortTotal + Quant_Mort
    QuantPacieTotal = QuantPacieTotal + Quant_Paciêntes

print(f"O Estado com o maior numero de mortos é: {NomeM} com {Maior} paciêntes em Obito.") #Letra A
print(f"O Estado com o menor numero de paciêntes é: {NomeMe} com {Menor} paciêntes com COVID19.") #Letra B
Porcent = (QuantMortTotal/QuantPacieTotal)*100
print(f"Porcentual de infectados em Obito: {Porcent:.2f}%") #Letra C