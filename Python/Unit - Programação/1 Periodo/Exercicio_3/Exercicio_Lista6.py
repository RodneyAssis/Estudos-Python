Nome_Al=[]
Nota_Al=[]

while True:
    Nome=str(input("Digite o nome do aluno: "))
    Nota=float(input("Digite a nota do respectivo aluno: "))
    Nome_Al.append(Nome)
    Nota_Al.append(Nota)
    if nota < 0:
        break

for i in range(len(Nome_Al)):