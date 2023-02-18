import random
LAluno=[]
LIdade=[]
LAno=[]
X=[]
cont = 0
print("--------------------------------")
while cont < 12:
    cont += 1
    Aluno=input("Nome do aluno inscrito: ")
    LAluno.append(Aluno)
    Idade=int(input("Idade do aluno: "))
    LIdade.append(Idade)
    Ano=int(input("Ano de curso do aluno: "))
    while Ano not in (1,2,3):
        if Ano >= 1 and Ano <= 3:
            break
        Ano = int(input("Ano de curso do aluno: "))
    print("--------------------------------")
    LAno.append(Ano)
gA=[]
gAid=[]
gB=[]
gBid=[]
gC=[]
gCid=[]
gD=[]
gDid=[]
LMaster= []
Cont2=-1
Condenovo=0
for i in range(0,12):
    LMaster = LMaster + [LAluno[i],LIdade[i],LAno[i]]

    X= random.randint(1,4)

    if X == 1:
        Cont2 += 1
        gA.append(LMaster[Cont2*3])
        gA.append(LMaster[(Cont2 * 3)+1])
        gAid.append(LMaster[(Cont2 * 3) + 1])
        gA.append(LMaster[(Cont2 * 3)+2])
    elif X == 2:
        Cont2 += 1
        gB.append(LMaster[Cont2*3])
        gB.append(LMaster[(Cont2 * 3)+1])
        gBid.append(LMaster[(Cont2 * 3) + 1])
        gB.append(LMaster[(Cont2 * 3)+2])
    elif X == 3:
        Cont2 += 1
        gC.append(LMaster[Cont2*3])
        gC.append(LMaster[(Cont2 * 3)+1])
        gCid.append(LMaster[(Cont2 * 3) + 1])
        gC.append(LMaster[(Cont2 * 3)+2])
    elif X == 4:
        Cont2 += 1
        gD.append(LMaster[Cont2*3])
        gD.append(LMaster[(Cont2 * 3)+1])
        gDid.append(LMaster[(Cont2 * 3) + 1])
        gD.append(LMaster[(Cont2 * 3)+2])


print("---------------------RELATÓRIO----------------------")
print("--------------Grupo A---------------")
Contador = 0
priTotal = []
A3=0
Contf = 0
Order = 0
points= 0
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
Media = sum(gAid)/points
print(f"Média da idade do grupo A: {Media:.2f}")
print(f"Quant. de Alunos do 3º Ano do Grupo A: {A3}")

print("--------------Grupo B---------------")
B3=0
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
Media1 = sum(gBid)/points1
print(f"Média da idade do grupo B: {Media1:.2f}")
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
Media2 = sum(gCid)/points2
print(f"Média da idade do grupo C: {Media2:.2f}")
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
Media3 = sum(gDid)/points3
print(f"Média da idade do grupo D: {Media3:.2f}")
print(f"Quant. de Alunos do 3º Ano do Grupo D: {D3}\n")

print("------------PORCENTAGEM-------------")
Porcent = (len(priTotal)/Contador)*100
print("Numero de primeiro-anistas:",len(priTotal))
print("Total de alunos:", Contador)
print(f"Pocentagem {Porcent:.2f}%")
print("------------------------------------")
