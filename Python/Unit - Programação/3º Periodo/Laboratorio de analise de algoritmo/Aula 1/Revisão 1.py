from random import randint
"""1. Crie um algoritmo que defina um vetor de elementos inteiros de tamanho 7, insira
valores aleatórios neste vetor e calcule a soma dos elementos que ocupam as posições
pares do vetor seguida pelo valor da soma dos elementos que ocupam as suas posições
ímpares. Imprima o resultado no console.
Ex.: [2,0,1,5,9,7,6]
Resposta: 18-12"""

Vetor = []

Par = 0
Impar = 0
for i in range(0, 7):
    Random = randint(1, 100)
    while Random in Vetor:
        Random = randint(1, 100)
        if Random not in Vetor:
            break
    Vetor.append(Random)
    if Vetor.index(Vetor[i]) % 2 == 0:
        Par += Vetor[i]
    else:
        Impar += Vetor[i]

print("Vetor:", Vetor)
print("Par:", Par)
print("Impar:", Impar)
