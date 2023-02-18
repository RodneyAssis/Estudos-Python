#11 - Faça um programa em Python para ler o nome e a respectiva nota de 3 alunos. Determine a maior e a menor nota.
#     Imprima o nome do aluno que obteve a maior nota e o nome do aluno que obteve a menor nota.
#     OBS: Suponha notas diferentes
al1 = str(input("Digite o nome do aluno: "))
n1 = float(input("Nota do {}: ".format(al1)))
al2 = str(input("Digite o nome do aluno: "))
n2 = float(input("Nota do {}: ".format(al2)))
al3 = str(input("Digite o nome do aluno: "))
n3 = float(input("Nota do {}: ".format(al3)))

if (n1 > n2) and (n3 > n2):
    print("A maior nota foi {} do aluno(a) {} e a menor nota foi {} do aluno(a) {}".format(n1, al1, n2, al2))

elif (n1 > n3) and (n2 > n3):
    print("A maior nota foi {} do aluno(a) {} e a menor nota foi {} do aluno(a) {}".format(n1, al1, n3, al3))

elif (n2 > n1) and (n3 > n1):
    print("A maior nota foi {} do aluno(a) {} e a menor nota foi {} do aluno(a) {}".format(n2, al2, n1, al1))

elif (n2 > n3) and (n1 > n3):
    print("A maior nota foi {} do aluno(a) {} e a menor nota foi {} do aluno(a) {}".format(n2, al2, n3, al3))

elif (n3 > n1) and (n2 > n1):
    print("A maior nota foi {} do aluno(a) {} e a menor nota foi {} do aluno(a) {}".format(n3, al3, n1, al1))

else:
    print("A maior nota foi {} do aluno(a) {} e a menor nota foi {} do aluno(a) {}".format(n3, al3, n2, al2))