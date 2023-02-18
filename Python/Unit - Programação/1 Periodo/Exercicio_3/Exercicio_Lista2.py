from random import randint
#2) Faça um programa em Python para gerar uma lista
#VET, com 10 elementos, composto por números
#aleatórios entre 1 (inclusive) e 40 (inclusive), de tal
#forma que não existam números repetidos.

#Imprima a lista VET em uma linha, com os elementos
#separados por espaço em branco.
Vet=[]
Cont = 0
while True:
    Num = randint(1, 40)
    if Num not in Vet:
        Vet.append(Num)
    Cont += 1
    if Cont == 100:
        break

for i in range(1,11):
    print(Vet[i], end=" ")
print("\nfim")
