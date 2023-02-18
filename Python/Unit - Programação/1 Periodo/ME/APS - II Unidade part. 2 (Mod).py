import random
LAluno = []
LIdade = []
LAno = []
x = 0
cont = 0
print("--------------------------------")
while cont < 12:
    cont += 1
    Aluno = input("Nome do aluno inscrito: ")
    LAluno.append(Aluno)
    Idade = int(input("Idade do aluno: "))
    LIdade.append(Idade)
    Ano = int(input("Ano de curso do aluno: "))
    while Ano not in (1, 2, 3):
        if Ano >= 1 and Ano <= 3:
            break
        Ano = int(input("Ano de curso do aluno: "))
    print("--------------------------------")
    LAno.append(Ano)
gA = []
gAid = []
gB = []
gBid = []
gC = []
gCid = []
gD = []
gDid = []
LMaster = []
cont = 0
Condenovo = 0
while cont < 12:
    LMaster = LMaster + [LAluno[cont], LIdade[cont], LAno[cont]]
    X = random.randint(1, 4)
    if X == 1 and len(gA) < 9:
        gA.append(LMaster[0])
        gA.append(LMaster[1])
        gAid.append(LMaster[1])
        gA.append(LMaster[2])
        cont += 1
    if X == 2 and len(gB) < 9:
        gB.append(LMaster[0])
        gB.append(LMaster[1])
        gBid.append(LMaster[1])
        gB.append(LMaster[2])
        cont += 1
    if X == 3 and len(gC) < 9:
        gC.append(LMaster[0])
        gC.append(LMaster[1])
        gCid.append(LMaster[1])
        gC.append(LMaster[2])
        cont += 1
    if X == 4 and len(gD) < 9:
        gD.append(LMaster[0])
        gD.append(LMaster[1])
        gDid.append(LMaster[1])
        gD.append(LMaster[2])
        cont += 1
    LMaster = []

print("")
print("Grupo A:", gA)
print("Grupo B:", gB)
print("Grupo C:", gC)
print("Grupo D:", gD)
print("")

# 1. LER O NOME DO ESTUDANTE E AS RESPECTIVAS IDADE E ANO:
# A. RELAÇÃO DA EQUIPES E SEUS RESPECTIVOS COMPONENTES:
print("---------------------RELATÓRIO----------------------")
print("--------------Grupo A---------------")
Contador = 0
priTotal = []
A3 = 0
Contf = 0
Order = 0
points = 0
while Order < len(gA):
    Contf += 1
    print(f"{Contf}º NOME: {gA[Order]}")
    Order += 1
    print(f"IDADE: {gA[Order]}")
    Order += 1
    points += 1
    print(f"Ano do curso: {gA[Order]}ºano")
    if gA[Order] == 1:
        priTotal.append(1)
    if gA[Order] == 3:
        A3 += 1
    Contador += 1
    Order += 1
print("------------------------------------")
# B. MEDIA DA EQUIPE A:
Media = sum(gAid) / points
print(f"Média da idade do grupo A: {Media:.2f}")
# C. QUANTIDADE DE ALUNOS DO 3 ANO NA EQUIPE A:
print(f"Quant. de Alunos do 3º Ano do Grupo A: {A3}")

print("--------------Grupo B---------------")
B3 = 0
Order1 = 0
points1 = 0
while Order1 < len(gB):
    Contf += 1
    print(f"{Contf}º NOME: {gB[Order1]}")
    Order1 += 1
    print(f"IDADE: {gB[Order1]}")
    Order1 += 1
    points1 += 1
    print(f"Ano do curso: {gB[Order1]}ºano")
    if gB[Order1] == 1:
        priTotal.append(1)
    if gB[Order1] == 3:
        B3 += 1
    Contador += 1
    Order1 += 1
print("------------------------------------")
# B. MEDIA DA EQUIPE B:
Media1 = sum(gBid) / points1
print(f"Média da idade do grupo B: {Media1:.2f}")
# C. QUANTIDADE DE ALUNOS DO 3 ANO NA EQUIPE B:
print(f"Quant. de Alunos do 3º Ano do Grupo B: {B3}")

print("--------------Grupo C---------------")
C3 = 0
Order2 = 0
points2 = 0
while Order2 < len(gC):
    Contf += 1
    print(f"{Contf}º NOME: {gC[Order2]}")
    Order2 += 1
    print(f"IDADE: {gC[Order2]}")
    Order2 += 1
    points2 += 1
    print(f"Ano do curso: {gC[Order2]}ºano")
    if gC[Order2] == 1:
        priTotal.append(1)
    if gC[Order2] == 3:
        C3 += 1
    Contador += 1
    Order2 += 1
print("------------------------------------")
# B. MEDIA DA EQUIPE C:
Media2 = sum(gCid) / points2
print(f"Média da idade do grupo C: {Media2:.2f}")
# C. QUANTIDADE DE ALUNOS DO 3 ANO NA EQUIPE C:
print(f"Quant. de Alunos do 3º Ano do Grupo C: {C3}")

print("--------------Grupo D---------------")
D3 = 0
Order3 = 0
points3 = 0
while Order3 < len(gD):
    Contf += 1
    print(f"{Contf}º NOME: {gD[Order3]}")
    Order3 += 1
    print(f"IDADE: {gD[Order3]}")
    Order3 += 1
    points3 += 1
    print(f"Ano do curso: {gD[Order3]}ºano")
    if gD[Order3] == 1:
        priTotal.append(1)
    if gD[Order3] == 3:
        D3 += 1
    Contador += 1
    Order3 += 1
print("------------------------------------")
# B. MEDIA DA EQUIPE D:
Media3 = sum(gDid) / points3
print(f"Média da idade do grupo D: {Media3:.2f}")
# C. QUANTIDADE DE ALUNOS DO 3 ANO NA EQUIPE D:
print(f"Quant. de Alunos do 3º Ano do Grupo D: {D3}\n")

# D. PORCENTAGEM DOS ESTUDANTES INSCRITOS DO PRIMEIRO ANO:
print("------------PORCENTAGEM-------------")
Porcent = (len(priTotal) / Contador) * 100
print("Numero de primeiro-anistas:", len(priTotal))
print("Total de alunos:", Contador)
print(f"Pocentagem {Porcent:.2f}%")
print("------------------------------------")