import random
a=str(input("Digite o nome do aluno: "))
b=str(input("Digite o nome de outro aluno: "))
c=str(input("Digite o nome de outro aluno: "))
d=str(input("Digite o nome de outro aluno: "))
lista=[a,b,c,d]
random.shuffle(lista)

print("Ordem de apresentação",lista)