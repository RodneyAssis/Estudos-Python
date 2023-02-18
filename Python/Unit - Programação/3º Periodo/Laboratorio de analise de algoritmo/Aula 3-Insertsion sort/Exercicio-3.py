"""
1. Utilizando uma linguagem de programação de sua preferência, implementar o
Insertion Sort
Exemplo:
Vetor (ou array) de entrada no algoritmo: [56, 25, 32, 10, 11]
Vetor de Saida (no console): [10, 11, 25, 32, 56]
a. Deve-se comentar o que cada linha implementada significa (ou executa).
"""

# OPÇÃO PARA NUMEROS ALEATORIOS
"""
from random import randint
Lista = []
Escolha = int(input("Escolha a quantidade de números armazenar na lista: "))
Numeros = int(input("Escolha o numero maximo de seleção: "))

while len(Lista) != Escolha:
    Aleatorio = randint(1, Numeros)
    Lista.append(Aleatorio)
"""

Lista = [56, 25, 32, 10, 11]

comp = 0
aux = 1
Cont = 0
print(f"Lista Recebida: {Lista}")
while True:
    if aux > len(Lista) - 1:
        Cont += 1
        aux = 1
        comp = 0
        if Cont == len(Lista)*2:
            break
    if Lista[aux] < Lista[comp]:
        armazenado = Lista[comp]
        Lista.pop(comp)
        Lista.insert(aux, armazenado)
    elif Lista[aux] > Lista[comp]:
        aux += 1
        comp += 1
    elif Lista[aux] == Lista[comp]:
        aux += 1
        comp += 1

print(f"Lista ordenado: {Lista}")
print(len(Lista))
