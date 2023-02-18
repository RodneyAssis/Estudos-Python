import funcoes1
"""Utilizando o conceito de modularização, crie um programa com um dicionário que
mostre a probabilidade de detectar certas partículas subatômicas.
Chave: nomes das partículas | Valor: probabilidades
Chave: nêutron | Valor: 0.55
O programa deverá ter os inputs para criar o dicionário e deverá ter uma função
que receba um dicionário como entrada e que retorne uma lista contendo o nome
da partícula menos provável de ser observada. Em caso de empate, a lista deve
conter todos os empatados.
Trate o código para que não permita inserir valores de tipo incorreto no dicionário.
Trate também a possibilidade de a soma de todas as probabilidades ultrapassarem"""
Dic = {}
while True:
    Nome_Particula = input("Digite o nome da particula:")
    if Nome_Particula == "":
        break
    Probabilidades = float(input("Digite a probabilidade de detecção: "))
    while not 0.0 < Probabilidades <= 1:
        print("Por favor, digite valores entre 0.00 à 1.00:")
        Probabilidades = float(input("Digite a probabilidade de detecção: "))
        if 0.0 < Probabilidades <= 1:
            break
    Dic[Nome_Particula] = Probabilidades
    print(funcoes1.Dicionario(Dic))
