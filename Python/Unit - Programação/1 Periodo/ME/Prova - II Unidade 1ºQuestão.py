Prova=[]
Nota=[1.5,1.5,1.5,1.5,2,2]
Cont = 0
while True:
    if Cont == 6:
        break
    R_Prova=str(input(f"Digite a resposta da {Cont+1}º: "))
    if R_Prova == "a":
        Prova.append(R_Prova)
        Cont += 1
    elif R_Prova == "b":
        Prova.append(R_Prova)
        Cont += 1
    elif R_Prova == "c":
        Prova.append(R_Prova)
        Cont += 1
    elif R_Prova == "d":
        Prova.append(R_Prova)
        Cont += 1
    elif R_Prova == "e":
        Prova.append(R_Prova)
        Cont += 1
    else:
        print("Essa alternativas não se encontra nas alternativas desejadas.")

N_Alunos=int(input("Digite o numero de alunos: "))
ContA = 0
L_Aluno = []
L_Matr = []
NotaA = []
MNota = []
ContApro = 0
Contm = 0
while ContA < N_Alunos:
    Matricula = int(input("Digite o numero de matrícula: "))
    Nome = input("Digite o nome do aluno: ")
    L_Matr.append(Matricula)
    L_Aluno.append(Nome)
    Q1 = str(input("Questão 1º: "))
    if Q1 == Prova[0]:
        NotaA.append(Nota[0+Contm])
    Q2 = str(input("Questão 2º: "))
    if Q2 == Prova[1]:
        NotaA.append(Nota[1+Contm])
    Q3 = str(input("Questão 3º: "))
    if Q3 == Prova[2]:
        NotaA.append(Nota[2+Contm])
    Q4 = str(input("Questão 4º: "))
    if Q4 == Prova[3]:
        NotaA.append(Nota[3+Contm])
    Q5 = str(input("Questão 5º: "))
    if Q5 == Prova[4]:
        NotaA.append(Nota[4+Contm])
    Q6 = str(input("Questão 6º: "))
    if Q6 == Prova[5]:
        NotaA.append(Nota[5+Contm])
    ContA += 1
    X = sum(NotaA)
    MNota.append(X)
    if X >= 6:
        ContApro+=1
    NotaA = []
print("")
print("--------------------------------------")
for i in range(0,N_Alunos):
    print(f"Aluno: {L_Aluno[i]}\nNumero de Matricula: {L_Matr[i]}\nNota: {MNota[i]}")
    print("--------------------------------------")
print("------------Gabarito da prova------------")
for i in range(0,6):
    print(f"{i+1}º questão:",Prova[i])

print("")
P = (ContApro/ContA)*100
print(f"Porcentual de alunos aprovados {P}%")
