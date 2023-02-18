#A prefeitura de uma cidade deseja fazer uma pesquisa entre seus habitantes. Desenvolva um programa
#em PYTHON que permita a coleta da quantidade de entrevistados e dos dados do(a) responsável de
#cada residência, são eles: nome, salário, sexo (M - Masculino / F - Feminino), idade e o número de
#habitantes em seu lar. Após as leituras das informações coletadas, o programa deverá exibir as
#seguintes informações (0,5):
#a) A relação das pessoas com salário superior a R$1.500,00 (0,5);
#b) A média de salário nas residências que os homens são responsáveis (0,5);
#c) O percentual de mulheres que são responsáveis pela sua residência (0,5);
#d) O nome da mulher com menor salário dentre os entrevistados (1,0).

NT_Intr = []
Nfen_intr = []
Sal_Intr = []
Sex_Intr = []
Ide_Intr = []
Resi_intr = []
NSAL_Sup = []
Sal_Sup = []
Sal_Masc = []
Sal_Fen = []
N_Intr=int(input("Digite o numero de entrevistado: "))

Cont = 0
ContF = 0
ContM = 0
ContS = 0
while Cont < N_Intr:
    print(f"------------{Cont+1} entrevistado------------")
    Nome=input("Digite o seu nome: ")
    NT_Intr.append(Nome)
    Sal=float(input("Digite o seu salário: "))
    Sal_Intr.append(Sal)
    if Sal > 1500:
        NSAL_Sup = NSAL_Sup + [Nome]
        Sal_Sup = Sal_Sup + [Sal]
        ContS += 1
    print("|Masculino - M | Feminino - F|")
    Sex=input("Digite o seu sexo: ").capitalize()
    while Sex != "M" and "F":
        if Sex == "M" or Sex == "F":
            break
        Sex = input("Digite o seu sexo: ").capitalize()
    if Sex == "M":
        Sal_Masc = Sal_Masc + [Sal]
        ContM += 1
    if Sex == "F":
        ContF += 1
        Sal_Fen = Sal_Fen + [Sal]
        Nfen_intr.append(Nome)
    Idade = int(input("Digite sua idade: "))
    Ide_Intr.append(Idade)
    N_Hab = int(input("Digite o numero de pessoas que reside em sua casa: "))
    Resi_intr.append(N_Hab)
    Cont += 1

print("")
print("Pessoas com Salário superior à 1500:")
for i in range(0,ContS):
    print(f"{NSAL_Sup[i]} com salario de {Sal_Sup[i]:.2f}")
print("")
if ContM >= 1:
    print("Média do Salário dos homens responsaveis pelas suas residências:")
    media=sum(Sal_Masc)/ContM
    print(media)
else:
    print("Não possui homem para fazer a média")
print("")
print("Porcentual de mulheres responsaveis pelas suas residências:")
porcent=(ContF/Cont)*100
print(f"{porcent:.2f}%")

print("")
Menor = min(Sal_Fen)
X = Sal_Fen.index(Menor)
Salariomin = Sal_Fen[X]
Nomemin = Nfen_intr[X]
print(f"{Nomemin} com {Salariomin} de salário")