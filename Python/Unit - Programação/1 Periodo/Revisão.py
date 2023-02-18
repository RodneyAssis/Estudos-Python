import random as r
from time import sleep as s
A = []
B = []
C = []
D = []
dados1 = []
c1 = []
c2 = []
a = 0
b = 0
anog = []
ano1 = []
ano2 = []
ano3 = []
ano4 = []
idG = []
id1 = []
id2 = []
id3 = []
id4 = []
a1 = []
b1 = []
c3 = []
d1 = []
print('------------------ Seja bem vindo ao Mega campeonato escolar. ------------------')
s(1)
for k in range(12):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    ano = int(input('Ano cursado 1º, 2º, 3º: '))
    if ano == 1 or ano == 2 or ano == 3:
        c2.append(2)
    if ano == 1:
        c1.append(1)
    dados = f'Nome: {nome} Idade: {str(idade)} Serie: {str(ano)}'
    serie = f'{ano}'
    anog.append(serie)
    id = f'{idade}'#?
    idG.append(idade)
    dados1.append(dados)
    print('-'*80)
while a < 3:
    b = r.randint(0, 11)
    if dados1[b] not in A:
        A.append(dados1[b])
        id1.append(idG[b])
        ano1.append(anog[b])
        a += 1

a = 0
while a < 3:
    b = r.randint(0, 11)
    if dados1[b] not in A and dados1[b] not in B:
        B.append(dados1[b])
        ano2.append(anog[b])
        id2.append(idG[b])
        a += 1

a = 0
while a < 3:
    b = r.randint(0, 11)
    if dados1[b] not in A and dados1[b] not in B and dados1[b] not in C:
        C.append(dados1[b])
        ano3.append(anog[b])
        id3.append(idG[b])
        a += 1

a = 0
while a < 3:
    b = r.randint(0, 11)
    if dados1[b] not in A and dados1[b] not in B and dados1[b] not in C and dados1[b] not in D:
        D.append(dados1[b])
        ano4.append(anog[b])
        id4.append(idG[b])
        a += 1

a = 0
qtd1 = ano1.count('3')
qtd2 = ano2.count('3')
qtd3 = ano3.count('3')
qtd4 = ano4.count('4')
print('')
print('---------  Grupo A --------- ')
for k in range(0, 3):
    if len(A) > 1:
        print(A[k])
print('')
print(f'Quantidade dos alunos do 3º ano na equipe: {qtd1}')
print(f'Media de idade da Equipe: {sum(id1)/3:.02f} ')
print('')
print('---------  Grupo B --------- ')
for q in range(0, 3):
    if len(B) > 1:
        print(B[q])
print('')
print(f'Quantidade dos alunos do 3º ano na equipe: {qtd2}')
print(f'Media de idade da Equipe: {sum(id2)/3:.02f} ')
print('')
print('---------  Grupo C --------- ')
for w in range(0, 3):
    if len(C) > 1:
        print(C[w])
print('')
print(f'Quantidade dos alunos do 3º ano na equipe: {qtd3}')
print(f'Media de idade da Equipe: {sum(id3)/3:.02f} ')
print('')
print('--------- Grupo D --------- ')
for s in range(0, 3):
    if len(D) > 1:
        print(D[s])
print('')
print(f'Quantidade dos alunos do 3º ano na equipe: {qtd4}')
print(f'Media de idade da Equipe: {sum(id4)/3:.02f} ')
print('')
print('---------------------------------------------------------------------')
print(f'O Percentual de alunos do 1º ano na competição: {(len(c1)/len(c2)*100):.02f}%.')
print('---------------------------------------------------------------------')
