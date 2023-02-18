from random import randint
#3) Faça um programa em Python para gerar uma lista
#A (10 elementos) e uma lista B (12 elementos) com
#números aleatórios entre 1 (inclusive) e 20
#(inclusive).
#Gere uma lista C apenas com os elementos de A que
#existem no vetor B, sem que haja repetição de
#números.

#Imprima as três listas, cada uma em uma linha, com
#os elementos separados por espaço em branco.

A = []
B = []
C = []

while len(A) != 10:
    r = randint(1,20)
    if r not in A:
        A.append(r)

while len(B) != 12:
    r = randint(1,20)
    if r not in B:
        B.append(r)

for i in range(1,21):
    if i in A and i in B:
        C = C + [i]

print("Lista A:")
for i in range(len(A)):
    print(A[i],end=" ")
print("\nLista B:")
for i in range(len(B)):
    print(B[i],end=" ")
print("\nLista C:")
for i in range(len(C)):
    print(B[i],end=" ")